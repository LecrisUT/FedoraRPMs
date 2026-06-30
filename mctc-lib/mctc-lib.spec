Name:           mctc-lib
Version:        0.5.2
Release:        %autorelease
Summary:        Modular computation tool chain library
License:        Apache-2.0
URL:            https://grimme-lab.github.io/mctc-lib/
Source0:        https://github.com/grimme-lab/mctc-lib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(jonquil)
BuildRequires:  pkgconfig(toml-f)
# For docs
BuildRequires:  rubygem-asciidoctor

%description
Common tool chain for working with molecular structure data in various
applications. This library provides a unified way to perform
operations on molecular structure data, like reading and writing to
common geometry file formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Move module files
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/mctc-lib/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/mctc-lib/

%files
%license LICENSE
%doc README.md
%{_bindir}/mctc-convert
%{_mandir}/man1/mctc-convert.1*
%{_libdir}/libmctc-lib*.so.0*

%files devel
%{_fmoddir}/mctc_*.mod
%{_libdir}/pkgconfig/mctc-lib.pc
%{_libdir}/libmctc-lib.so

%changelog
%autochangelog
