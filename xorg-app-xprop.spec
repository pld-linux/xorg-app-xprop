Summary:	xprop application - property displayer for X
Summary(pl.UTF-8):	Aplikacja xprop do wyświetlania właściwości dla X
Name:		xorg-app-xprop
Version:	1.2.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xprop-%{version}.tar.bz2
# Source0-md5:	fae3d2fda07684027a643ca783d595cc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xprop utility is for displaying window and font properties in an X
server. One window or font is selected using the command line
arguments or possibly in the case of a window, by clicking on the
desired window. A list of properties is then given, possibly with
formatting information.

%description -l pl.UTF-8
Narzędzie xprop służy do wyświetlania właściwości okien in fontów w
serwerze X. Można wybrać jedno okno lub font przy użyciu argumentów
linii poleceń lub, w przypadku okna, klikając na nie. Następnie
podawana jest lista właściwości, w miarę możliwości wraz z
informacjami o formacie.

%prep
%setup -q -n xprop-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xprop
%{_mandir}/man1/xprop.1*
