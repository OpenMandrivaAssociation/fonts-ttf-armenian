Summary:	Armenian TrueType fonts
Name:		fonts-ttf-armenian
Version:	1.1
Release:	31
License:	Distributable
Group:		System/Fonts/True type
Url:		http://www.freenet.am/armnls/
Source0:	fonts-ttf-armenian-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale

%description
This Package provides free Armenian TrueType fonts.

%prep
%setup -q

%build
# TODO: create a README file

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/TTF/armenian/
cp * %{buildroot}/%{_datadir}/fonts/TTF/armenian
pushd %{buildroot}/%{_datadir}/fonts/TTF/armenian
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/armenian \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-armenian:pri=50

%files
%dir %{_datadir}/fonts/TTF/armenian/
%{_datadir}/fonts/TTF/armenian/*
%{_sysconfdir}/X11/fontpath.d/ttf-armenian:pri=50

