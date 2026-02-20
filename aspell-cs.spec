Summary:	Czech dictionary for aspell
Summary(cs.UTF-8):	Česká data pro aspell
Summary(pl.UTF-8):	Czeski słownik dla aspella
Name:		aspell-cs
Version:	20040614
%define	subv	1
Release:	2
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/cs/aspell6-cs-%{version}-%{subv}.tar.bz2
# Source0-md5:	50f0c2b7b6fcfe47bb647ad8993d2fe8
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Czech dictionary (i.e. word list) for aspell.

%description -l cs.UTF-8
Česká data pro aspell.

%description -l pl.UTF-8
Czeski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-cs-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
