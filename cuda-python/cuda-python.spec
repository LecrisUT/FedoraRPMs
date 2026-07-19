%global cuda_major 13
%global cuda_minor 3

Name:           cuda-python
Version:        13.3.1
Release:        %autorelease
Summary:        Metapackage collection of CUDA Python subpackages
BuildArch:      noarch

License:        Apache-2.0
URL:            https://github.com/NVIDIA/cuda-python
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel


%global _description %{expand:
CUDA Python: Performance meets Productivity
}

%description %_description

%package -n python3-cuda-python
Summary:        %{summary}

%description -n python3-cuda-python %_description


%prep
%autosetup -p1 -n cuda-python-%{version}
cp .git_archival.txt cuda_python/


%generate_buildrequires
cd cuda_python
export CUDA_HOME=%{_prefix}/local/cuda-%{cuda_major}.%{cuda_minor}
%pyproject_buildrequires


%build
cd cuda_python
export CUDA_HOME=%{_prefix}/local/cuda-%{cuda_major}.%{cuda_minor}
%pyproject_wheel


%install
cd cuda_python
%pyproject_install
%pyproject_save_files cuda


%files -n python3-cuda-python -f %{pyproject_files}
%license cuda_python/LICENSE
%doc cuda_python/DESCRIPTION.rst


%changelog
%autochangelog
