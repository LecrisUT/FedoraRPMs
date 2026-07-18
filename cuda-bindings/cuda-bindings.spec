%global cuda_major 13
%global cuda_minor 3

# TODO: Find a way to keep the debug symbols
%global debug_package %{nil}

Name:           cuda-bindings
Version:        %{cuda_major}.3.1
Release:        %autorelease
Summary:        Python bindings for CUDA

License:        Apache-2.0
URL:            https://github.com/NVIDIA/cuda-python
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-c++
# Cuda dependencies
BuildRequires:  cuda-cudart-devel-%{cuda_major}-%{cuda_minor}
BuildRequires:  libnvvm-%{cuda_major}-%{cuda_minor}
BuildRequires:  cuda-nvrtc-devel-%{cuda_major}-%{cuda_minor}
BuildRequires:  cuda-profiler-api-%{cuda_major}-%{cuda_minor}
BuildRequires:  cuda-crt-%{cuda_major}-%{cuda_minor}
BuildRequires:  libcufile-devel-%{cuda_major}-%{cuda_minor}


%global _description %{expand:
Python bindings for CUDA
}

%description %_description

%package -n python3-cuda-bindings
Summary:        %{summary}

%description -n python3-cuda-bindings %_description


%prep
%autosetup -p1 -n cuda-python-%{version}


%generate_buildrequires
cd cuda_bindings
%pyproject_buildrequires


%build
cd cuda_bindings
export CUDA_HOME=%{_prefix}/local/cuda-%{cuda_major}.%{cuda_minor}
%pyproject_wheel


%install
cd cuda_bindings
%pyproject_install
%pyproject_save_files cuda


%files -n python3-cuda-bindings -f %{pyproject_files}
%license cuda_bindings/LICENSE
%doc cuda_bindings/README.md


%changelog
%autochangelog
