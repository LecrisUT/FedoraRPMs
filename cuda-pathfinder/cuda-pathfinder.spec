Name:           cuda-pathfinder
Version:        1.5.6
Release:        %autorelease
Summary:        Pathfinder for CUDA components
BuildArch:      noarch

License:        Apache-2.0
URL:            https://github.com/NVIDIA/cuda-python
Source:         %{url}/archive/refs/tags/cuda-pathfinder-v%{version}.tar.gz

BuildRequires:  python3-devel


%global _description %{expand:
Pathfinder for CUDA components
}

%description %_description

%package -n python3-cuda-pathfinder
Summary:        %{summary}

%description -n python3-cuda-pathfinder %_description


%prep
%autosetup -p1 -n cuda-python-cuda-pathfinder-v%{version}


%generate_buildrequires
cd cuda_pathfinder
%pyproject_buildrequires


%build
cd cuda_pathfinder
%pyproject_wheel


%install
cd cuda_pathfinder
%pyproject_install
%pyproject_save_files cuda


%files -n python3-cuda-pathfinder -f %{pyproject_files}
%license cuda_pathfinder/LICENSE
%doc cuda_pathfinder/DESCRIPTION.rst


%changelog
%autochangelog
