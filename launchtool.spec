Summary:	Runs a command supervising its execution
Name:		launchtool
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Enrico Zini <enrico@debian.org>
Source0:	http://people.debian.org/~enrico/local/source/%{name}_%{version}-1.tar.gz
URL:		http://people.debian.org/~enrico/launchtool.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
launchtool is a tool that runs a user-supplied command and can
supervise its execution in many ways, such as controlling its
environment, blocking signals, logging its output, changing user and
group permissions, limiting resource usage, restarting it if it fails,
running it continuously and turn it into a daemon.

%prep
%setup -q -n %{name}-%{version}

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
