Name:           adwaita-fonts
Version:        48.2
Release:        1
Summary:        Adwaita Fonts
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/adwaita-fonts
Source:         https://download.gnome.org/sources/adwaita-fonts/48/%{name}-%{version}.tar.xz

# needed for directory ownership
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildArch:      noarch

%description
Adwaita Sans, a variation of Inter, and Adwaita Mono, Iosevka
customized to match Inter.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
#dir %{_fontsdir}/Adwaita
#{_fontsdir}/Adwaita/AdwaitaMono-Bold.ttf
#{_fontsdir}/Adwaita/AdwaitaMono-BoldItalic.ttf
#{_fontsdir}/Adwaita/AdwaitaMono-Italic.ttf
#{_fontsdir}/Adwaita/AdwaitaMono-Regular.ttf
#{_fontsdir}/Adwaita/AdwaitaSans-Italic.ttf
#{_fontsdir}/Adwaita/AdwaitaSans-Regular.ttf
