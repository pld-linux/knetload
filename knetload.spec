Summary:	KNetLoad - a small network load meter for Kicker
Summary(pl):	KNetLoad - ma³y miernik obci±¿enia sieci dla Kickera
Name:		knetload
Version:	2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://flameeyes.web.ctonet.it/files/%{name}-%{version}.tar.bz2
# Source0-md5:	10d41f1177cfde19408bb20a9a174e10
URL:		http://extragear.kde.org/apps/knetload.php
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNetLoad is a small network load meter for Kicker.

%description -l pl
KNetLoad to ma³y miernik obci±¿enia sieci dla Kickera.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
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
