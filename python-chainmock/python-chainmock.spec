Name:           python-chainmock
Version:        2.0.0
Release:        %autorelease
Summary:        A mocking library for Python and pytest

License:        MIT

URL:            https://chainmock.readthedocs.io/
Source0:        %{pypi_source chainmock}

BuildArch:      noarch

BuildRequires:  python3-devel
# Manually adding the test dependencies because `dev` is too broad
# https://github.com/ollipa/chainmock/issues/43
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%global _description %{expand:
Chainmock is a mocking library for Python and pytest. Under the hood
it uses Python standard library mocks providing an alternative syntax
to create mocks and assertions. Chainmock also comes with some additional
features to make testing faster and more straightforward. The syntax
works especially well with pytest fixtures.
}

%description %_description


%package -n python3-chainmock
Summary:        %{summary}

%description -n python3-chainmock %_description


%prep
%autosetup -p1 -C


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l chainmock


%check
%pytest


%files -n python3-chainmock -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
