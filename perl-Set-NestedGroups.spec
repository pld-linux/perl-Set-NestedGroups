%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	NestedGroups
Summary:	Set-NestedGroups perl module
Summary(pl):	Modu³ perla Set-NestedGroups
Name:		perl-Set-NestedGroups
Version:	0.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Provides:	perl(Set::NestedGroups::Member)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set-NestedGroups perl module.

%description -l pl
Modu³ perla Set-NestedGroups.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
