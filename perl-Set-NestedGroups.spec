%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	NestedGroups
Summary:	Set::NestedGroups - grouped data eg ACLs, city/state/country etc
Summary(pl):	Set::NestedGroups - pogrupowane dane np. ACL-e, miasta/stany/pañstwa itp
Name:		perl-Set-NestedGroups
Version:	0.01
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Provides:	perl(Set::NestedGroups::Member)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::NestedGroups gives an implementation of nested groups, access
control lists (ACLs) would be one example of nested groups.

%description -l pl
Modu³ Set::NestedGroups udostêpnia implementacjê zagnie¿d¿onych grup.
Przyk³adem takich grup mog± byæ listy kontroli dostêpu (ACL-e).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Set/NestedGroups.pm
%{perl_sitelib}/Set/NestedGroups
%{_mandir}/man3/*
