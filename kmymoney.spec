%define api 5
%define libname %mklibname kmymoney


Summary:	The Personal Finances Manager
Name:		kmymoney
Version:	5.2.2
Release:	1
License:	GPLv2+
Group:		Office
Url:		https://techbase.kde.org/Projects/KMyMoney
Source0:	http://download.kde.org/stable/kmymoney/%{version}/%{name}-%{version}.tar.xz
#Patch1:		kmymoney-5.0.0-missing_include.patch
#Patch2:		kmymoney-5.0.8-buildfix.patch
#Patch3:		kmymoney-5.0.0-workaround_missing_qsql.patch
#Patch4:   Fix-compile-for-Newer-Akonadi-Builds.patch

BuildRequires:	appstream
BuildRequires:	cmake ninja
BuildRequires:	doxygen
BuildRequires:	perl-Finance-Quote
BuildRequires:	boost-devel
BuildRequires:	gmpxx-devel
#BuildRequires:	pkgconfig(aqbanking) >= 6.0.1
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(libxml++-5.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlcipher)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  pkgconfig(python)
BuildRequires:	cmake(gwenhywfar)
#BuildRequires:	cmake(gwengui-qt5)
#BuildRequires:	cmake(gwengui-cpp)
BuildRequires:	cmake(LibIcal)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libalkimia6)
BuildRequires:	cmake(KChart)
BuildRequires:	cmake(Qt6Core) 
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6QmlNetwork)
BuildRequires:  cmake(Qt6Svg) 
BuildRequires:  cmake(Qt6Sql) 
BuildRequires:  cmake(Qt6Xml) 
BuildRequires:  cmake(Qt6Test) 
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(PlasmaActivities)
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
BuildRequires:	cmake(QGpgmeQt6)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qtbase-sql-postgresql
BuildRequires:	qt6-qtbase-sql-odbc
BuildRequires:	qt6-qtbase-sql-mariadb
BuildRequires:	qt6-qtbase-sql-firebird
BuildRequires:	opensp-devel

Requires:	perl-Finance-Quote
Requires:	gwenhywfar-tools
Requires:	%{libname} = %{EVRD}

%description
KMyMoney Personal Finance Manager.

%files -f %{name}.lang
%{_bindir}/kmymoney
%{_datadir}/applications/org.kde.kmymoney.desktop
%{_datadir}/checkprinting/check-3-part-template.html
%{_datadir}/checkprinting/check_template.html
%{_datadir}/checkprinting/check_template_green_linen.html
%{_datadir}/config.kcfg/kmymoney.kcfg
%{_datadir}/kconf_update/kmymoney.upd
%{_datadir}/metainfo/org.kde.kmymoney.appdata.xml
%{_datadir}/mime/packages/x-kmymoney.xml
%{_iconsdir}/hicolor/*x*/apps/kmymoney.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kmymoney.png
%{_mandir}/man1/kmymoney.1.*
#---------------------------------------------------------------------------
%define kmm_csvimportercore_major 5
%define libkmm_csvimportercore %mklibname kmm_csvimportercore %{kmm_csvimportercore_major}

%define kmm_mymoney_major 5
%define libkmm_mymoney %mklibname kmm_mymoney %{kmm_mymoney_major}

%define kmm_icons_major 5
%define libkmm_icons %mklibname kmm_icons %{kmm_icons_major}

%define kmm_plugin_major 5
%define libkmm_plugin %mklibname kmm_plugin %{kmm_plugin_major}

%define kmm_widgets_major 5
%define libkmm_widgets %mklibname kmm_widgets %{kmm_widgets_major}

%define kmm_payeeidentifier_major 5
%define libkmm_payeeidentifier %mklibname kmm_payeeidentifier %{kmm_payeeidentifier_major}

%define kmm_menus_major 5
%define libkmm_menus %mklibname kmm_menus %{kmm_menus_major}

%define kmm_models_major 5
%define libkmm_models %mklibname kmm_models %{kmm_models_major}

%define kmm_settings_major 5
%define libkmm_settings %mklibname kmm_settings %{kmm_settings_major}

%define kmm_printer_major 5
%define libkmm_printer %mklibname kmm_printer %{kmm_printer_major}


%package -n %{libname}
Summary:	Shared library for %{name}

Obsoletes:	%{libkmm_mymoney}
Obsoletes:	%{libkmm_plugin}
Obsoletes:	%{libkmm_widgets}
Obsoletes:	%{libkmm_payeeidentifier}
Obsoletes:      %{libkmm_csvimportercore}
Obsoletes:      %{libkmm_icons}
Obsoletes:	%{libkmm_menus}
Obsoletes:	%{libkmm_models}
Obsoletes:	%{libkmm_settings}
Obsoletes:	%{libkmm_printer}

%description -n %{libname}
This package contains the shared library files.

%files -n %{libname}
%{_libdir}/qt6/plugins/kmymoney_plugins/
%{_libdir}/qt6/plugins/sqldrivers/qsqlcipher.so

%{_libdir}/libkmm_base_dialogs.so.%{api}*
%{_libdir}/libkmm_base_widgets.so.%{api}*
%{_libdir}/libkmm_codec.so.%{api}*
%{_libdir}/libkmm_csvimportercore.so.%{api}*
%{_libdir}/libkmm_extended_dialogs.so.%{api}*
%{_libdir}/libkmm_gpgfile.so.%{api}*
%{_libdir}/libkmm_icons.so.%{api}*
%{_libdir}/libkmm_keychain.so.%{api}*
%{_libdir}/libkmm_menuactionexchanger.so.%{api}*
%{_libdir}/libkmm_menus.so.%{api}*
%{_libdir}/libkmm_models.so.%{api}*
%{_libdir}/libkmm_mymoney.so.%{api}*
%{_libdir}/libkmm_payeeidentifier.so.%{api}*
%{_libdir}/libkmm_plugin.so.%{api}*
%{_libdir}/libkmm_printer.so.%{api}*
%{_libdir}/libkmm_selections.so.%{api}*
%{_libdir}/libkmm_settings.so.%{api}*
%{_libdir}/libkmm_templates.so.%{api}*
%{_libdir}/libkmm_webconnect.so.%{api}*
%{_libdir}/libkmm_widgets.so.%{api}*
%{_libdir}/libkmm_wizard.so.%{api}*
%{_libdir}/libkmm_yesno.so.%{api}*
%{_libdir}/libonlinetask_interfaces.so.%{api}*

%package devel
Summary:	KMyMoney Development library
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
%description devel
KMyMoney development files.

%files devel
%{_libdir}/libkmm_base_dialogs.so
%{_libdir}/libkmm_base_widgets.so
%{_libdir}/libkmm_codec.so
%{_libdir}/libkmm_csvimportercore.so
%{_libdir}/libkmm_extended_dialogs.so
%{_libdir}/libkmm_gpgfile.so
%{_libdir}/libkmm_icons.so
%{_libdir}/libkmm_keychain.so
%{_libdir}/libkmm_menuactionexchanger.so
%{_libdir}/libkmm_menus.so
%{_libdir}/libkmm_models.so
%{_libdir}/libkmm_mymoney.so
%{_libdir}/libkmm_payeeidentifier.so
%{_libdir}/libkmm_plugin.so
%{_libdir}/libkmm_printer.so
%{_libdir}/libkmm_selections.so
%{_libdir}/libkmm_settings.so
%{_libdir}/libkmm_templates.so
%{_libdir}/libkmm_webconnect.so
%{_libdir}/libkmm_widgets.so
%{_libdir}/libkmm_wizard.so
%{_libdir}/libkmm_yesno.so
%{_libdir}/libonlinetask_interfaces.so
%{_includedir}/%{name}/

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export LIBICAL_BASE=/usr
%cmake \
	-DENABLE_WEBENGINE=1 \
	-DBUILD_WITH_QT6:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-html --with-man

