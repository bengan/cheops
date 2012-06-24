Summary:	Network resources viewer and manager
Summary(pl.UTF-8):   Narzędzie do wizualizacji i zarządzania zasobami sieciowymi
Name:		cheops
Version:	0.61
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.marko.net/pub/cheops/%{name}-%{version}.tar.gz
# Source0-md5:	efd4254e3b36b3936a7ebbadf71e28e6
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.marko.net/cheops/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	ucd-snmp-devel >= 4.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheops aims to be a network "swiss army knife" used for seeing and
accessing network resources. It's written in GTK+ and uses combination
of a variety of network tools (ping, traceroute, halfscan, QueSO).
Provides system administrators with a simple interface to identifying
and accessing their network hardware.

%description -l pl.UTF-8
Cheops ma być "sieciowym scyzorykiem" używanym do obrazowania i
dostępu do zasobów sieciowych. Został napisany przy użyciu GTK+;
wykorzystuje różne narzędzia sieciowe (ping, traceroute, halfscan,
QueSO), umożliwiając administratorom prostą identyfikację oraz dostęp
do ich sprzętu sieciowego.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cheops,%{_datadir}/cheops} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

install cheops $RPM_BUILD_ROOT%{_bindir}
install pixmaps/*.xpm cheops.conf services.conf $RPM_BUILD_ROOT%{_datadir}/cheops
install plugins/*.so $RPM_BUILD_ROOT%{_libdir}/cheops

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/cheops
%dir %{_libdir}/cheops
%attr(755,root,root) %{_libdir}/cheops/*.so
%dir %{_datadir}/cheops
%config	%{_datadir}/cheops/*.conf
%{_datadir}/cheops/*.xpm
%{_applnkdir}/Network/Misc/cheops.desktop
%{_pixmapsdir}/*
