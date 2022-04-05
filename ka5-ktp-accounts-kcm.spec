#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	21.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		ktp-accounts-kcm
Summary:	ktp-accounts-kcm
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7c535edd60e6567069fab8e5971c4c1c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel >= 0.9.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Control Module for managing Telepathy Accounts.

%description -l pl.UTF-8
Moduł kontroli KDE do zarządzania kontami Telepathy.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libktpaccountskcminternal.so.*.*.*
%ghost %{_libdir}/libktpaccountskcminternal.so.9
%dir %{_libdir}/qt5/plugins/kaccounts/ui
%attr(755,root,root) %{_libdir}/qt5/plugins/kaccounts/ui/ktpaccountskcm_plugin_kaccounts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_gabble.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_haze.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_idle.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_morse.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_salut.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_sipe.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktpaccountskcm_plugin_sunshine.so
%dir %{_datadir}/accounts/providers/kde
%{_datadir}/accounts/providers/kde/ktp-gadugadu.provider
%{_datadir}/accounts/providers/kde/ktp-generic.provider
%{_datadir}/accounts/providers/kde/ktp-haze-aim.provider
%{_datadir}/accounts/providers/kde/ktp-haze-icq.provider
%{_datadir}/accounts/providers/kde/ktp-haze-sametime.provider
%{_datadir}/accounts/providers/kde/ktp-haze-skypeweb.provider
%{_datadir}/accounts/providers/kde/ktp-haze-yahoo.provider
%{_datadir}/accounts/providers/kde/ktp-jabber.provider
%{_datadir}/accounts/providers/kde/ktp-kde-talk.provider
%{_datadir}/accounts/providers/kde/ktp-morse-telegram.provider
%{_datadir}/accounts/providers/kde/ktp-salut.provider
%{_datadir}/accounts/providers/kde/ktp-sipe-haze.provider
%{_datadir}/accounts/providers/kde/ktp-sipe.provider
%dir %{_datadir}/accounts/services/kde
%{_datadir}/accounts/services/kde/google-im.service
%{_datadir}/accounts/services/kde/ktp-generic-im.service
%{_datadir}/accounts/services/kde/ktp-haze-aim-im.service
%{_datadir}/accounts/services/kde/ktp-haze-gadugadu-im.service
%{_datadir}/accounts/services/kde/ktp-haze-icq-im.service
%{_datadir}/accounts/services/kde/ktp-haze-sametime-im.service
%{_datadir}/accounts/services/kde/ktp-haze-skypeweb-im.service
%{_datadir}/accounts/services/kde/ktp-haze-yahoo-im.service
%{_datadir}/accounts/services/kde/ktp-jabber-im.service
%{_datadir}/accounts/services/kde/ktp-kde-talk-im.service
%{_datadir}/accounts/services/kde/ktp-morse-telegram-im.service
%{_datadir}/accounts/services/kde/ktp-salut-im.service
%{_datadir}/accounts/services/kde/ktp-sipe-haze-im.service
%{_datadir}/accounts/services/kde/ktp-sipe-im.service
%{_datadir}/kservices5/ktpaccountskcm_plugin_gabble.desktop
%{_datadir}/kservices5/ktpaccountskcm_plugin_haze.desktop
%{_datadir}/kservices5/ktpaccountskcm_plugin_idle.desktop
%{_datadir}/kservices5/ktpaccountskcm_plugin_morse.desktop
%{_datadir}/kservices5/ktpaccountskcm_plugin_salut.desktop
%{_datadir}/kservices5/ktpaccountskcm_plugin_sipe.desktop
%{_datadir}/kservices5/ktpaccountskcm_plugin_sunshine.desktop
%{_datadir}/kservicetypes5/ktpaccountskcminternal-accountuiplugin.desktop
%{_datadir}/telepathy/profiles
