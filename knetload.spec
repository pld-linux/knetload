Summary:	KNetLoad is a small network load meter for Kicker
Name:		knetload
Version:	2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://flameeyes.web.ctonet.it/files/%{name}-%{version}.tar.bz2
# Source0-md5:	10d41f1177cfde19408bb20a9a174e10
URL:		http://extragear.kde.org/apps/knetload.php
#BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML
%define		_prefix		/usr/X11R6

%description
KNetLoad is a small network load meter for Kicker.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_appsdir="%{_applnkdir}"; export kde_appsdir
#CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
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
#%doc AUTHORS ChangeLog README TODO
#%attr(755,root,root) %{_bindir}/*
