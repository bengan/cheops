# $Revision: 1.16 $ $Date: 2001-10-01 09:45:40 $
Summary:	Network resources viewer and manager
Summary(pl):	Narz�dzie do wizualizacji i zarz�dzania zasobami sieciowymi
Name:		cheops
Version:	0.61
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Url:		http://www.marko.net/cheops
Source0:	ftp://ftp.marko.net/pub/cheops/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	gtk+-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Cheops aims to be a network "swiss army knife" used for seeing and
accessing network resources. It's written in GTK+ and uses combination
of a variety of network tools (ping, traceroute, halfscan, QueSO).
Provides system adminstrators with a simple interface to identyfying
and accessing their network hardware.

%description -l pl
Cheops ma by� "sieciowym scyzorykiem" u�ywanym do obrazowania i
dost�pu do zasob�w sieciowych. Zosta� napisany przy u�yciu GTK+;
wykorzystuje r�ne narz�dzia sieciowe (ping, traceroute, halfscan,
QueSO), umo�liwiaj�c administratorom prost� identyfikacj� oraz dost�p
do ich sprz�tu sieciowego.

%prep
%setup -q

%build
autoconf
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cheops,%{_datadir}/cheops} \
	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

install cheops ${RPM_BUILD_ROOT}%{_bindir}
install pixmaps/*.xpm cheops.conf services.conf ${RPM_BUILD_ROOT}%{_datadir}/cheops
install plugins/*.so ${RPM_BUILD_ROOT}%{_libdir}/cheops


install %{SOURCE1} ${RPM_BUILD_ROOT}%{_applnkdir}/Network/Misc

gzip -9nf README Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cheops
%dir %{_libdir}/cheops
%attr(755,root,root) %{_libdir}/cheops/*.so
%config	%{_datadir}/cheops/*.conf
%{_datadir}/cheops
%{_applnkdir}/Network/Misc/cheops.desktop
