Name:           koneko
Version:        1.0.1
Release:        %autorelease
Summary:        oneko, but for the KDE Wayland compositor
URL:            https://codeberg.org/snowkat/koneko
# Licensed under MIT-0 OR CC0-1.0, but the latter is only permissable for content
License:        MIT-0
BuildArch:      noarch

%global         forgeurl %{url}
%global         tag0     v%{version}
%forgemeta

Source0:        %forgesource

BuildRequires:  make
BuildRequires:  qt6-qtshadertools
BuildRequires:  kf6-kpackage
BuildRequires:  kwin

# For directory ownership and to work in general
Requires:       kwin

%description
koneko is a KWin Script with the goal of emulating oneko-sakura in a way that's
usable on Wayland.


%prep
%forgeautosetup -p1


%build
%make_build clean-qsb
%make_build qsb


%install
# Cannot use %%make_install here because we want to use kwin-wayland path instead
%make_build PKGFLAGS="--type KWin/Script --packageroot %{buildroot}%{_datadir}/kwin-wayland/scripts" install


%files
%license LICENSE.MIT0
%doc README.md
%{_datadir}/kwin-wayland/scripts/xyz.datagirl.koneko/


%changelog
%autochangelog
