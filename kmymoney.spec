Summary:	The Personal Finances Manager
Name:		kmymoney
Version:	4.7.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		http://techbase.kde.org/Projects/KMyMoney
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kmymoney-3.98.0-fix-desktop-file.patch
#Patch1:		mymoneydatabasemgrtest.patch

BuildRequires:	doxygen
BuildRequires:	perl-Finance-Quote
BuildRequires:	boost-devel
BuildRequires:	gmpxx-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	pkgconfig(aqbanking)
BuildRequires:	pkgconfig(libalkimia)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(libxml-2.0)
Requires:	perl-Finance-Quote
Requires:	gwenhywfar-tools

%description 
KMyMoney Personal Finance Manager.

%files -f %{name}.lang
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
%{_datadir}/appdata/*.xml

#-----------------------------------------------------------------------------

%define kmm_kdchart_major 4
%define libkmm_kdchart %mklibname kmm_kdchart %{kmm_kdchart_major}

%package -n %{libkmm_kdchart}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_kdchart}
KMyMoney library.

%files -n %{libkmm_kdchart}
%{_kde_libdir}/libkmm_kdchart.so.%{kmm_kdchart_major}*

#-----------------------------------------------------------------------------

%define kmm_mymoney_major 4
%define libkmm_mymoney %mklibname kmm_mymoney %{kmm_mymoney_major}

%package -n %{libkmm_mymoney}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_mymoney}
KMyMoney library.

%files -n %{libkmm_mymoney}
%{_kde_libdir}/libkmm_mymoney.so.%{kmm_mymoney_major}*

#-----------------------------------------------------------------------------

%define kmm_plugin_major 4
%define libkmm_plugin %mklibname kmm_plugin %{kmm_plugin_major}

%package -n %{libkmm_plugin}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_plugin}
KMyMoney library.

%files -n %{libkmm_plugin}
%{_kde_libdir}/libkmm_plugin.so.%{kmm_plugin_major}*

#-----------------------------------------------------------------------------

%define kmm_widgets_major 4
%define libkmm_widgets %mklibname kmm_widgets %{kmm_widgets_major}

%package -n %{libkmm_widgets}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_widgets}
KMyMoney library.

%files -n %{libkmm_widgets}
%{_kde_libdir}/libkmm_widgets.so.%{kmm_widgets_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	KMyMoney Development library
Group:		Development/KDE and Qt
Requires:	%{libkmm_kdchart} = %{version}
Requires:	%{libkmm_mymoney} = %{version}
Requires:	%{libkmm_plugin} = %{version}
Requires:	%{libkmm_widgets} = %{version}

%description devel
KMyMoney development files.

%files devel
%{_kde_libdir}/*.so
%{_kde_includedir}/%{name}

#-----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export LIBICAL_BASE=/usr
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html
