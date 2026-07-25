%define upstream_name    Perl6-Perldoc
%define upstream_version 0.000013
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Add a to_xhtml() method to Perl6::Perldoc::Parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Perl6-Perldoc
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Perldoc-0.000013.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Filter::Simple)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
This module preprocesses your code from the point at which the module is
first used, stripping out any Perl 6 documentation (as specified in
Synopsis 26).

This means that, so long as your program starts with:

    use Perl6::Perldoc;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml MYMETA.yml README
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*


