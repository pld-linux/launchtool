Summary:	Runs a command supervising its execution
Summary(pl):	Uruchamianie poleceñ z nadzorowaniem ich wykonywania
Name:		launchtool
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Enrico Zini <enrico@debian.org>
Source0:	http://people.debian.org/~enrico/local/source/%{name}_%{version}-1.tar.gz
# Source0-md5:	0b1ba89f6d5ed64e6948a7c9ae6645a4
URL:		http://people.debian.org/~enrico/launchtool.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
launchtool is a tool that runs a user-supplied command and can
supervise its execution in many ways, such as controlling its
environment, blocking signals, logging its output, changing user and
group permissions, limiting resource usage, restarting it if it fails,
running it continuously and turn it into a daemon.

%description -l pl
launchtool jest narzêdziem, które uruchamia podane polecenie i mo¿e
nadzorowaæ jego wykonywanie na wiele sposobów, takich jak kontrola
jego ¶rodowiska, blokowanie sygna³ów, logowanie wyj¶cia, zmiana
uprawnieñ u¿ytkownika i grupy, ograniczanie u¿ycia zasobów, restart w
przypadku niepowodzenia, uruchamianie bez przerwy i zamiana w demona.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -D launchtool.1 $RPM_BUILD_ROOT%{_mandir}/man1/launchtool.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
