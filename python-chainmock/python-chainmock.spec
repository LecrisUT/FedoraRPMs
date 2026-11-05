Name:           python-chainmock
Version:        2.0.0
Release:        %autorelease
Summary:        A mocking library for Python and pytest

License:        MIT

URL:            https://chainmock.readthedocs.io/
# Note: cannot use the pypi source because it lacks the test files
# https://github.com/ollipa/chainmock/issues/44
Source0:        https://github.com/ollipa/chainmock/archive/v%{version}/chainmock-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

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
# Remove the line trying to override our PYTHONPATH
sed -i "/setenv = PYTHONPATH/d" tox.ini
# i_unittest.py does not run properly for some reason
# https://github.com/ollipa/chainmock/issues/45
sed -i "/sh -c 'python tests\/integrations\/i_unittest.py/d" tox.ini


%generate_buildrequires
%pyproject_buildrequires -e pytest-latest


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l chainmock


%check
%tox


%files -n python3-chainmock -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
