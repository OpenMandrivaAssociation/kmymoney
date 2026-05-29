Summary:	The Personal Finances Manager
Name:		kmymoney
Version:	5.2.0
Release:	2
License:	GPLv2+
Group:		Office
Url:		https://techbase.kde.org/Projects/KMyMoney
Source0:	http://download.kde.org/stable/kmymoney/%{version}/%{name}-%{version}.tar.xz
#Patch1:		kmymoney-5.0.0-missing_include.patch
#Patch2:		kmymoney-5.0.8-buildfix.patch
#Patch3:		kmymoney-5.0.0-workaround_missing_qsql.patch
#Patch4:   Fix-compile-for-Newer-Akonadi-Builds.patch

BuildSystem:    cmake
BuildOption:    -DBUILD_WITH_QT6:BOOL=ON

BuildRequires:	doxygen
BuildRequires:	perl-Finance-Quote
BuildRequires:	boost-devel
BuildRequires:	gmpxx-devel
BuildRequires:	pkgconfig(aqbanking) >= 6.0.1
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlcipher)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  pkgconfig(python)
BuildRequires:	cmake(gwenhywfar)
BuildRequires:	cmake(gwengui-qt5)
BuildRequires:	cmake(gwengui-cpp)
BuildRequires:	cmake(LibIcal)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(LibAlkimia5)
BuildRequires:	cmake(KChart)
BuildRequires:	cmake(Qt6Core) 
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets) 
BuildRequires:  cmake(Qt6Svg) 
BuildRequires:  cmake(Qt6Sql) 
BuildRequires:  cmake(Qt6Xml) 
BuildRequires:  cmake(Qt6Test) 
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(KF6IdentityManagement)
BuildRequires:	cmake(KF6Kross)
BuildRequires:	cmake(KF6KrossUi)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6Akonadi)
BuildRequires:	cmake(KF6Activities)

Requires:	perl-Finance-Quote
Requires:	gwenhywfar-tools

%description
KMyMoney Personal Finance Manager.

%files -f %{name}.lang
%{_kde6_bindir}/*
%{_kde6_libdir}/qt5/plugins/kmymoney
%{_kde6_libdir}/qt5/plugins/sqldrivers/qsqlcipher.so
%{_kde6_datadir}/config.kcfg/*.kcfg
%{_kde6_applicationsdir}/*.desktop
%{_kde6_iconsdir}/*/*/*/*
%{_kde6_services}/*.desktop
#{_kde6_servicetypes}/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/kbanking
%{_datadir}/kmymoney
%{_datadir}/kxmlgui5/*
%{_datadir}/kconf_update/*
%{_datadir}/checkprinting
%{_datadir}/metainfo/org.kde.kmymoney.appdata.xml
%{_mandir}/man1/%{name}.1*
#-----------------------------------------------------------------------------

%define kmm_csvimportercore_major 5
%define libkmm_csvimportercore %mklibname kmm_csvimportercore %{kmm_csvimportercore_major}

%package -n %{libkmm_csvimportercore}
Summary:        KMyMoney library
Group:          System/Libraries

%description -n %{libkmm_csvimportercore}
KMyMoney library.

%files -n %{libkmm_csvimportercore}
%{_kde6_libdir}/libkmm_csvimportercore.so.%{kmm_csvimportercore_major}*


#-----------------------------------------------------------------------------

%define kmm_mymoney_major 5
%define libkmm_mymoney %mklibname kmm_mymoney %{kmm_mymoney_major}

%package -n %{libkmm_mymoney}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_mymoney}
KMyMoney library.

%files -n %{libkmm_mymoney}
%{_kde6_libdir}/libkmm_mymoney.so.%{kmm_mymoney_major}*

#-----------------------------------------------------------------------------

%define kmm_icons_major 5
%define libkmm_icons %mklibname kmm_icons %{kmm_icons_major}

%package -n %{libkmm_icons}
Summary:        KMyMoney library
Group:          System/Libraries

%description -n %{libkmm_icons}
KMyMoney library.

%files -n %{libkmm_icons}
%{_kde6_libdir}/libkmm_icons.so.%{kmm_icons_major}*

#-----------------------------------------------------------------------------

%define kmm_plugin_major 5
%define libkmm_plugin %mklibname kmm_plugin %{kmm_plugin_major}

%package -n %{libkmm_plugin}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_plugin}
KMyMoney library.

%files -n %{libkmm_plugin}
%{_kde6_libdir}/libkmm_plugin.so.%{kmm_plugin_major}*

#-----------------------------------------------------------------------------

%define kmm_widgets_major 5
%define libkmm_widgets %mklibname kmm_widgets %{kmm_widgets_major}

%package -n %{libkmm_widgets}
Summary:	KMyMoney library
Group:		System/Libraries

%description -n %{libkmm_widgets}
KMyMoney library.

%files -n %{libkmm_widgets}
%{_kde6_libdir}/libkmm_widgets.so.%{kmm_widgets_major}*

#-----------------------------------------------------------------------------

%define kmm_payeeidentifier_major 5
%define libkmm_payeeidentifier %mklibname kmm_payeeidentifier %{kmm_payeeidentifier_major}

%package -n %{libkmm_payeeidentifier}
Summary: KMyMoney library
Group: System/Libraries

%description -n %{libkmm_payeeidentifier}
KMyMoney library.

%files -n %{libkmm_payeeidentifier}
%{_kde6_libdir}/libkmm_payeeidentifier.so.%{kmm_payeeidentifier_major}*

#-----------------------------------------------------------------------------

%define kmm_menus_major 5
%define libkmm_menus %mklibname kmm_menus %{kmm_menus_major}

%package -n %{libkmm_menus}
Summary:        KMyMoney library
Group:          System/Libraries

%description -n %{libkmm_menus}
KMyMoney library.

%files -n %{libkmm_menus}
%{_kde6_libdir}/libkmm_menus.so.%{kmm_menus_major}*

#-----------------------------------------------------------------------------


%define kmm_models_major 5
%define libkmm_models %mklibname kmm_models %{kmm_models_major}

%package -n %{libkmm_models}
Summary:        KMyMoney library
Group:          System/Libraries

%description -n %{libkmm_models}
KMyMoney library.

%files -n %{libkmm_models}
%{_kde6_libdir}/libkmm_models.so.%{kmm_models_major}*

#-----------------------------------------------------------------------------


%define kmm_settings_major 5
%define libkmm_settings %mklibname kmm_settings %{kmm_settings_major}

%package -n %{libkmm_settings}
Summary:        KMyMoney library
Group:          System/Libraries

%description -n %{libkmm_settings}
KMyMoney library.

%files -n %{libkmm_settings}
%{_kde6_libdir}/libkmm_settings.so.%{kmm_settings_major}*

#-----------------------------------------------------------------------------
%define kmm_printer_major 5
%define libkmm_printer %mklibname kmm_printer %{kmm_printer_major}

%package -n %{libkmm_printer}
Summary:        KMyMoney library
Group:          System/Libraries

%description -n %{libkmm_printer}
KMyMoney library.

%files -n %{libkmm_printer}
%{_kde6_libdir}/libkmm_printer.so.%{kmm_printer_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	KMyMoney Development library
Group:		Development/KDE and Qt
Requires:	%{libkmm_mymoney} = %{version}
Requires:	%{libkmm_plugin} = %{version}
Requires:	%{libkmm_widgets} = %{version}
Requires:	%{libkmm_payeeidentifier} = %{version}
Requires:       %{libkmm_csvimportercore} = %{version}
Requires:       %{libkmm_icons} = %{version}
Requires:       %{libkmm_menus} = %{version}
Requires:       %{libkmm_models} = %{version}
Requires:       %{libkmm_settings} = %{version}
Requires:       %{libkmm_printer} = %{version}
%description devel
KMyMoney development files.

%files devel
%{_kde6_libdir}/libkmm_menus.so
%{_kde6_libdir}/libkmm_models.so
%{_kde6_libdir}/libkmm_settings.so
%{_kde6_libdir}/libkmm_mymoney.so
%{_kde6_libdir}/libkmm_payeeidentifier.so
%{_kde6_libdir}/libkmm_plugin.so
%{_kde6_libdir}/libkmm_widgets.so
%{_kde6_libdir}/libkmm_icons.so
%{_kde6_libdir}/libkmm_csvimportercore.so
%{_kde6_libdir}/libkmm_printer.so

%{_kde6_includedir}/%{name}

#-----------------------------------------------------------------------------

# %install -a
# %find_lang %{name} --with-html --with-man


