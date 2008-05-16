Summary:	Remote Replication Agent Connection protocol library
Summary(pl.UTF-8):	RRA - aplikacja SynCE do synchronizacji
Name:		synce-rra
Version:	0.11.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/librra-%{version}.tar.gz
# Source0-md5:	1dff577a2b1ac85a69768de555d05ee7
Patch0:		%{name}-libmimedir.patch
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libmimedir-vlm-devel
BuildRequires:	libtool
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-librapi2-devel >= %{version}
BuildRequires:	synce-libsynce-devel >= %{version}
%requires_eq_to	synce-librapi2 synce-librapi2-devel
%requires_eq_to	synce-libsynce synce-libsynce-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed

%description
SynCE is a project for connecting to devices running Windows CE or
Pocket PC.

RRA implements the Remote Replication Agent Connection protocol for
synchronising objects between a Windows CE device and other computer.

%description -l pl.UTF-8
RRA to aplikacja do synchronizacji będąca częścią projektu SynCE.

Celem projektu SynCE jest dostarczenie środków do komunikacji z
urządzeniami opartymi na Windows CE z komputera z Linuksem, FreeBSD
lub podobnym systemem operacyjnym.

%package devel
Summary:	Header files for RRA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RRA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmimedir-vlm-devel
Requires:	synce-librapi2-devel >= %{version}
Requires:	synce-libsynce-devel >= %{version}

%description devel
Header files for RRA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RRA.

%package static
Summary:	Static RRA library
Summary(pl.UTF-8):	Statyczna biblioteka RRA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static RRA library.

%description static -l pl.UTF-8
Statyczna biblioteka RRA.

%package -n python-pyrra
Summary:	Python binding for RRA library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki RRA
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pyrra
Python binding for RRA library.

%description -n python-pyrra -l pl.UTF-8
Wiązanie Pythona do biblioteki RRA.

%prep
%setup -q -n librra-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{py_sitedir}/pyrra.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/synce-matchmaker
%attr(755,root,root) %{_bindir}/rra-appointment-from-vevent
%attr(755,root,root) %{_bindir}/rra-appointment-to-vevent
%attr(755,root,root) %{_bindir}/rra-contact-from-vcard
%attr(755,root,root) %{_bindir}/rra-contact-to-vcard
%attr(755,root,root) %{_bindir}/rra-decode
%attr(755,root,root) %{_bindir}/rra-delete
%attr(755,root,root) %{_bindir}/rra-get-data
%attr(755,root,root) %{_bindir}/rra-get-ids
%attr(755,root,root) %{_bindir}/rra-get-recurring-appointments
%attr(755,root,root) %{_bindir}/rra-get-types
%attr(755,root,root) %{_bindir}/rra-put-data
%attr(755,root,root) %{_bindir}/rra-subscribe
%attr(755,root,root) %{_bindir}/rra-task-from-vtodo
%attr(755,root,root) %{_bindir}/rra-task-to-vtodo
%attr(755,root,root) %{_bindir}/rra-timezone
%attr(755,root,root) %{_libdir}/librra.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librra.so.0
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%doc lib/README
%attr(755,root,root) %{_libdir}/librra.so
%{_libdir}/librra.la
%{_includedir}/rra
%{_pkgconfigdir}/librra.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librra.a

%files -n python-pyrra
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyrra.so
