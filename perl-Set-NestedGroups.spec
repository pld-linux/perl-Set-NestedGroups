%include	/usr/lib/rpm/macros.perl
Summary:	Set-NestedGroups perl module
Summary(pl):	Modu³ perla Set-NestedGroups
Name:		perl-Set-NestedGroups
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Set/Set-NestedGroups-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Set/NestedGroups
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Set/NestedGroups.pm
%{perl_sitelib}/Set/NestedGroups
%{perl_sitearch}/auto/Set/NestedGroups

%{_mandir}/man3/*
