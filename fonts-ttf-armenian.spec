Summary:	Armenian TrueType fonts
Name:		fonts-ttf-armenian
Version:	1.1
Release:	%mkrel 23
License:	Distributable
URL:		http://www.freenet.am/armnls/
Group:		System/Fonts/True type

Source0:	fonts-ttf-armenian-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	mkfontscale

%description
This Package provides free Armenian TrueType fonts.

%prep
%setup -q

%build
# TODO: create a README file

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/armenian/
cp * %buildroot/%_datadir/fonts/TTF/armenian
pushd %buildroot/%_datadir/fonts/TTF/armenian
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/armenian \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-armenian:pri=50


%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/fonts/TTF/armenian/
%_datadir/fonts/TTF/armenian/*
%_sysconfdir/X11/fontpath.d/ttf-armenian:pri=50



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-23mdv2011.0
+ Revision: 675409
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-22
+ Revision: 675173
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-21
+ Revision: 664322
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 1.1-20mdv2011.0
+ Revision: 605815
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1-19mdv2010.1
+ Revision: 494120
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.1-18mdv2009.1
+ Revision: 351041
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1-17mdv2009.0
+ Revision: 220858
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1-16mdv2008.1
+ Revision: 170835
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.1-15mdv2008.1
+ Revision: 149741
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1-14mdv2008.0
+ Revision: 48738
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:10:35 (52884)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:13:57 (52821)
- import fonts-ttf-armenian-1.1-12mdk

* Tue Feb 07 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1-12mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

