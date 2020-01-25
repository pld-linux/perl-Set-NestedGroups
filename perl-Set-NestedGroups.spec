#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	Set
%define		pnam	NestedGroups
Summary:	Set::NestedGroups - grouped data eg ACLs, city/state/country etc
Summary(pl.UTF-8):	Set::NestedGroups - pogrupowane dane np. ACL-e, miasta/stany/państwa itp
Name:		perl-Set-NestedGroups
Version:	0.01
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25fb922eb8f2227716badbcb8a89202c
URL:		http://search.cpan.org/dist/Set-NestedGroups/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Set::NestedGroups::Member)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::NestedGroups gives an implementation of nested groups, access
control lists (ACLs) would be one example of nested groups.

%description -l pl.UTF-8
Moduł Set::NestedGroups udostępnia implementację zagnieżdżonych grup.
Przykładem takich grup mogą być listy kontroli dostępu (ACL-e).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Set/NestedGroups.pm
%{perl_vendorlib}/Set/NestedGroups
%{_mandir}/man3/*
