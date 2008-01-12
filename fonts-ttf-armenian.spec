Summary:	Free Armenian TrueType fonts
Name:		fonts-ttf-armenian
Version:	1.1
Release:	%mkrel 15
License:	Distributable
URL:		http://www.freenet.am/armnls/
Group:		System/Fonts/True type

Source0:	fonts-ttf-armenian-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

%description
This Package provides free Armenian TrueType fonts.

%prep

%setup -q

%build
# TODO: create a README file

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/armenian/

/usr/sbin/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
cp * %buildroot/%_datadir/fonts/TTF/armenian/

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/armenian \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-armenian:pri=50


%post
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/fonts/TTF/armenian/
%_datadir/fonts/TTF/armenian/*
%_sysconfdir/X11/fontpath.d/ttf-armenian:pri=50

