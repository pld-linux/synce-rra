Summary:	RRA - SynCE synchronization application
Summary(pl.UTF-8):	RRA - aplikacja SynCE do synchronizacji
Name:		synce-rra
Version:	0.9.1
Release:	4
License:	MIT
Group:		Libraries
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	72742f93f19d5727159989ec80a725f0
Patch0:		%{name}-libmimedir.patch
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libmimedir-vlm-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-librapi2-devel >= 0.9.1
BuildRequires:	synce-libsynce-devel >= 0.9.1
Requires:	synce-librapi2 >= 0.9.1
Requires:	synce-libsynce >= 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RRA is a synchronization application, a part of the SynCE project.

The purpose of the SynCE project is to provide a means of
communication with a Windows CE device from a computer running Linux,
FreeBSD or a similar operating system.

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
Requires:	synce-librapi2-devel >= 0.9.1
Requires:	synce-libsynce-devel >= 0.9.1

%description devel
Header files for RRA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RRA.

%package static
Summary:	Static RRA library
Summary(pl.UTF-8):	Statyczna biblioteka RRA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static RRA library.

%description static -l pl.UTF-8
Statyczna biblioteka RRA.

%prep
%setup -q
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/librra.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%doc lib/README
%attr(755,root,root) %{_libdir}/librra.so
%{_libdir}/librra.la
%{_includedir}/rra
%{_aclocaldir}/rra.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/librra.a
