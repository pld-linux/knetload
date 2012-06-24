Summary:	KNetLoad - a small network load meter for Kicker
Summary(pl.UTF-8):   KNetLoad - mały miernik obciążenia sieci dla Kickera
Name:		knetload
Version:	2.3
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://flameeyes.web.ctonet.it/files/%{name}-%{version}.tar.bz2
# Source0-md5:	10d41f1177cfde19408bb20a9a174e10
URL:		http://extragear.kde.org/apps/knetload.php
BuildRequires:	arts-devel
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	doxygen
Requires:	graphviz
Requires:	libxml2-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNetLoad is a small network load meter for Kicker.

%description -l pl.UTF-8
KNetLoad to mały miernik obciążenia sieci dla Kickera.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/%{name}
