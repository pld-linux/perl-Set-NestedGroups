%include	/usr/lib/rpm/macros.perl
Summary:	Set-NestedGroups perl module
Summary(pl):	Modu³ perla Set-NestedGroups
Name:		perl-Set-NestedGroups
Version:	0.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Set/Set-NestedGroups-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Provides:	perl(Set::NestedGroups::Member)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set-NestedGroups perl module.

%description -l pl
Modu³ perla Set-NestedGroups.

%prep
%setup -q -n Set-NestedGroups-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Set/NestedGroups.pm
%{perl_sitelib}/Set/NestedGroups
%{_mandir}/man3/*
