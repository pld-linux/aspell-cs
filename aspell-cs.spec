Summary:	Czech dictionary for aspell
Summary(pl):	Czeski s³ownik dla aspella
Name:		aspell-cs
Version:	0.51
%define	subv	0
Release:	1
Epoch:		1
License:	GPL (?)
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/cs/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	4be28bef4385ef46e80547ce8cdc4535
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Czech dictionary (i.e. word list) for aspell.

%description -l pl
Czeski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

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
%doc README Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*
