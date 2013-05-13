Summary:	The Personal Finances Manager
Name:		kmymoney
Version:	4.6.3
Release:	2
Source0:	http://switch.dl.sourceforge.net/project/kmymoney2/KMyMoney-KDE4/%{version}/kmymoney-%{version}.tar.bz2
Patch0:    	kmymoney-3.98.0-fix-desktop-file.patch
Patch1:    	mymoneydatabasemgrtest.patch
Patch2:		kmymoney-4.6.3-gmp-5.1.0.patch
License:	GPLv2+
Group:		Office
Url:		http://techbase.kde.org/Projects/KMyMoney
BuildRequires:	kdepimlibs4-devel
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(aqbanking)
BuildRequires:	libxml++2.6-devel
BuildRequires:	boost-devel
BuildRequires:	perl-Finance-Quote
BuildRequires:	doxygen
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	fdupes
BuildRequires:	libalkimia-devel
BuildRequires:	gmpxx-devel
Requires:	perl-Finance-Quote

%description 
KMyMoney Personal Finance Manager.

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_appsdir}/*
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_datadir}/config/*
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop
%{_datadir}/mime/packages/*.xml
%{_kde_mandir}/man1/*

#-----------------------------------------------------------------------------

%define kmm_kdchart_major 4
%define libkmm_kdchart %mklibname kmm_kdchart %{kmm_kdchart_major}

%package -n %{libkmm_kdchart}
Summary: KMyMoney library
Group: System/Libraries

%description -n %{libkmm_kdchart}
KMyMoney library.

%files -n %{libkmm_kdchart}
%defattr(-,root,root)
%{_kde_libdir}/libkmm_kdchart.so.%{kmm_kdchart_major}*

#-----------------------------------------------------------------------------

%define kmm_mymoney_major 4
%define libkmm_mymoney %mklibname kmm_mymoney %{kmm_mymoney_major}

%package -n %{libkmm_mymoney}
Summary: KMyMoney library
Group: System/Libraries

%description -n %{libkmm_mymoney}
KMyMoney library.

%files -n %{libkmm_mymoney}
%defattr(-,root,root)
%{_kde_libdir}/libkmm_mymoney.so.%{kmm_mymoney_major}*

#-----------------------------------------------------------------------------

%define kmm_plugin_major 4
%define libkmm_plugin %mklibname kmm_plugin %{kmm_plugin_major}

%package -n %{libkmm_plugin}
Summary: KMyMoney library
Group: System/Libraries

%description -n %{libkmm_plugin}
KMyMoney library.

%files -n %{libkmm_plugin}
%defattr(-,root,root)
%{_kde_libdir}/libkmm_plugin.so.%{kmm_plugin_major}*

#-----------------------------------------------------------------------------

%define kmm_widgets_major 4
%define libkmm_widgets %mklibname kmm_widgets %{kmm_widgets_major}

%package -n %{libkmm_widgets}
Summary: KMyMoney library
Group: System/Libraries

%description -n %{libkmm_widgets}
KMyMoney library.

%files -n %{libkmm_widgets}
%defattr(-,root,root)
%{_kde_libdir}/libkmm_widgets.so.%{kmm_widgets_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: KMyMoney Development library
Group: Development/KDE and Qt
Requires: %{libkmm_kdchart} = %{version}
Requires: %{libkmm_mymoney} = %{version}
Requires: %{libkmm_plugin} = %{version}
Requires: %{libkmm_widgets} = %{version}

%description devel
KMyMoney development files.

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so
%{_kde_includedir}/%{name}

#-----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
export LIBICAL_BASE=/usr
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.6.1-2mdv2012.0
+ Revision: 812842
- Remove now bad libgmp-devel requires (#65714)

* Mon Jan 16 2012 Bernhard Rosenkraenzer <bero@bero.eu> 4.6.1-1
+ Revision: 761830
- Update to 4.6.1

  + Thomas Spuhler <tspuhler@mandriva.org>
    - adding source 4.6.0
    - upgrade to 4.6.0

  + Sergey Zhemoitel <serg@mandriva.org>
    - patch russian translate

* Wed May 11 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 4.5.3-2
+ Revision: 673693
- Rebuild

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 4.5.3-1
+ Revision: 637619
- new version 4.5.3

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 4.5.2-1mdv2011.0
+ Revision: 624700
- update to new version 4.5.2
- re-enalbe aqbanking

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 4.5.1-1mdv2011.0
+ Revision: 598723
- new version 4.5.1

* Tue Sep 14 2010 Thomas Spuhler <tspuhler@mandriva.org> 4.5-2mdv2011.0
+ Revision: 578136
- patch 1 needed to connect to MySQL
- added patch 1 to make it connect to MySQL

* Tue Aug 17 2010 Funda Wang <fwang@mandriva.org> 4.5-1mdv2011.0
+ Revision: 570987
- New version 4.5

* Wed Jun 16 2010 Funda Wang <fwang@mandriva.org> 3.98.1-1mdv2011.0
+ Revision: 548129
- New version 3.98.1

* Thu Jun 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.98.0-2mdv2010.1
+ Revision: 547008
- Fix menu entry for KMymoney

* Sun May 16 2010 Funda Wang <fwang@mandriva.org> 3.98.0-1mdv2010.1
+ Revision: 544880
- 3.98.0 final

* Tue Apr 27 2010 Funda Wang <fwang@mandriva.org> 3.97.2-1.1119473.1mdv2010.1
+ Revision: 539538
- New snapshot

  + Sandro Cazzaniga <kharec@mandriva.org>
    - clean mixed-use-of-spaces-and-tabs

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 3.97.1-2.1114730.1mdv2010.1
+ Revision: 534710
- new snapshot

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - new upstream release 3.97.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean file list

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 3.97.0-1mdv2010.1
+ Revision: 530397
- New version 3.97.0

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 3.96.1-1mdv2010.1
+ Revision: 508917
- 3.96.1

* Mon Feb 15 2010 Funda Wang <fwang@mandriva.org> 3.96.0-2mdv2010.1
+ Revision: 506233
- install en doc to correct dir

* Mon Feb 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.0-1mdv2010.1
+ Revision: 506175
- Fix file list
- Update to Beta2

* Thu Feb 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.0-0.1088392.2mdv2010.1
+ Revision: 504249
- push in release

* Wed Feb 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.0-0.1088392.1mdv2010.1
+ Revision: 503987
- This does not need to go on testing in cooker as this will not go on stable release before next stable version of kmymoney

  + Funda Wang <fwang@mandriva.org>
    - New snapshot

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 3.95.0-0.1075755.1mdv2010.1
+ Revision: 492471
- update summary
- add remind on uploading for myself
- import kmymoney

