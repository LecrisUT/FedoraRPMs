%global cuda_major 13
%global cuda_minor 3

# TODO: Find a way to keep the debug symbols
%global debug_package %{nil}

Name:           cuda-core
Version:        1.1.0
Release:        %autorelease
Summary:        Pythonic CUDA module

License:        Apache-2.0
URL:            https://github.com/NVIDIA/cuda-python
Source:         %{url}/archive/refs/tags/cuda-core-v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-c++
# Cuda dependencies
BuildRequires:  cuda-cudart-devel-%{cuda_major}-%{cuda_minor}
BuildRequires:  cuda-nvrtc-devel-%{cuda_major}-%{cuda_minor}
BuildRequires:  cuda-profiler-api-%{cuda_major}-%{cuda_minor}


%global _description %{expand:
cuda.core: pythonic CUDA module
}

%description %_description

%package -n python3-cuda-core
Summary:        %{summary}

%description -n python3-cuda-core %_description


%prep
%autosetup -p1 -n cuda-python-cuda-core-v%{version}


%generate_buildrequires
cd cuda_core
export CUDA_HOME=%{_prefix}/local/cuda-%{cuda_major}.%{cuda_minor}
%pyproject_buildrequires


%build
cd cuda_core
export CUDA_HOME=%{_prefix}/local/cuda-%{cuda_major}.%{cuda_minor}
%pyproject_wheel


%install
cd cuda_core
%pyproject_install
%pyproject_save_files cuda


%files -n python3-cuda-core -f %{pyproject_files}
%license cuda_core/LICENSE
%doc cuda_core/README.md


%changelog
%autochangelog
