Name: qtchooser
Summary: Qt Chooser
Group: Base/Libraries
Version: 39
Release: 0
License: LGPL-2.1+ or GPL-3.0
URL: http://macieira.org/qtchooser
Source0: %{name}-%{version}.tar.bz2
Source1: qtchooser-rpmlintrc
Source2: macros.qmake
Source1001: %{name}.manifest
Requires: qt-default

%description
The qtchooser package contains a wrapper used to select between Qt binary versions. It is only needed if both Qt4 and Qt5 are installed for access via the /usr/bin directory.

%prep
%setup -q -n %{name}-%{version}.tar.bz2
cp %{SOURCE1001} .

%build
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
cp %SOURCE2 %{buildroot}%{_sysconfdir}/rpm/macros.qmake

mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser

# Add configuration file for qt5
echo "%{_libdir}/qt5/bin" > %{buildroot}%{_sysconfdir}/xdg/qtchooser/5.conf
echo "%{_libdir}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/5.conf


%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%doc LGPL_EXCEPTION.txt LICENSE.GPL LICENSE.LGPL
%dir %{_sysconfdir}/xdg/qtchooser
%{_sysconfdir}/rpm/macros.qmake
%{_sysconfdir}/xdg/qtchooser/5.conf
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
%{_bindir}/qtpaths
%{_bindir}/qml
%{_bindir}/qml1plugindump
%{_bindir}/qmlbundle
%{_bindir}/qmlmin
%{_bindir}/qmlplugindump
%{_bindir}/qmlprofiler
%{_bindir}/qmlscene
%{_bindir}/qmltestrunner
%{_bindir}/qmlviewer
%{_bindir}/qmlimportscanner
%{_bindir}/qtconfig
%{_bindir}/qtdiag
%{_bindir}/rcc
%{_bindir}/uic
%{_bindir}/uic3
%{_bindir}/xmlpatterns
%{_bindir}/xmlpatternsvalidator
%{_datadir}/man/man1/qtchooser.1.gz
