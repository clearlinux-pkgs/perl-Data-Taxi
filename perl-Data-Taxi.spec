#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Taxi
Version  : 0.96
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Data-Taxi-0.96.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Data-Taxi-0.96.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Taxi-perl = %{version}-%{release}
Requires: perl(Debug::ShowStuff)
BuildRequires : buildreq-cpan
BuildRequires : perl(Debug::ShowStuff)
BuildRequires : perl(String::Util)
BuildRequires : perl(Tie::IxHash)

%description
Data::Taxi version 0.96
=========================
NAME
Data::Taxi - Taint-aware, XML-ish data serialization

%package dev
Summary: dev components for the perl-Data-Taxi package.
Group: Development
Provides: perl-Data-Taxi-devel = %{version}-%{release}
Requires: perl-Data-Taxi = %{version}-%{release}

%description dev
dev components for the perl-Data-Taxi package.


%package perl
Summary: perl components for the perl-Data-Taxi package.
Group: Default
Requires: perl-Data-Taxi = %{version}-%{release}

%description perl
perl components for the perl-Data-Taxi package.


%prep
%setup -q -n Data-Taxi-0.96
cd %{_builddir}/Data-Taxi-0.96

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Taxi.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Data/Taxi.pm
