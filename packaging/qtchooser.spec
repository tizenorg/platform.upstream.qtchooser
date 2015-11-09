
%define git g97962d2

Name: qtchooser
Summary: Qt Chooser
Version: 26
Release: 3%{?dist}

License: LGPLv2 or GPLv3
URL: http://macieira.org/qtchooser
Source0: http://macieira.org/qtchooser/qtchooser-%{version}-%{git}.tar.gz
Source1: macros.qmake
Requires: qt-default

%description
%{summary}


%prep
%setup -q -n qtchooser-%{version}-%{git}


%build
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
cp %SOURCE1 %{buildroot}%{_sysconfdir}/rpm/macros.qmake

# Add configuration file for qt4
echo "%{_libdir}/qt4/bin" > %{buildroot}%{_sysconfdir}/xdg/qtchooser/4.conf
echo "%{_libdir}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/4.conf

# Add configuration file for qt5
echo "%{_libdir}/qt5/bin" > %{buildroot}%{_sysconfdir}/xdg/qtchooser/5.conf
echo "%{_libdir}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/5.conf

## env vars
#QT_SELECT
#QTCHOOSER_RUNTOOL

%files
%defattr(-,root,root,-)
%doc LGPL_EXCEPTION.txt LICENSE.GPL LICENSE.LGPL
%dir %{_sysconfdir}/xdg/qtchooser
%{_sysconfdir}/rpm/macros.qmake
%{_sysconfdir}/xdg/qtchooser/5.conf
%{_sysconfdir}/xdg/qtchooser/4.conf
%{_bindir}/qtchooser
%{_bindir}/assistant
%{_bindir}/designer
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_bindir}/moc
%{_bindir}/pixeltool
%{_bindir}/qcollectiongenerator
%{_bindir}/qdbus
%{_bindir}/qdbuscpp2xml
%{_bindir}/qdbusviewer
%{_bindir}/qdbusxml2cpp
%{_bindir}/qdoc
%{_bindir}/qdoc3
%{_bindir}/qglinfo
%{_bindir}/qhelpconverter
%{_bindir}/qhelpgenerator
%{_bindir}/qmake
%{_bindir}/qml1plugindump
%{_bindir}/qmlbundle
%{_bindir}/qmlmin
%{_bindir}/qmlplugindump
%{_bindir}/qmlprofiler
%{_bindir}/qmlscene
%{_bindir}/qmltestrunner
%{_bindir}/qmlviewer
%{_bindir}/qtconfig
%{_bindir}/rcc
%{_bindir}/uic
%{_bindir}/uic3
%{_bindir}/xmlpatterns
%{_bindir}/xmlpatternsvalidator

