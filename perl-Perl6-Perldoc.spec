%define upstream_name    Perl6-Perldoc
%define upstream_version 0.000011
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.000011
Release:	2

Summary:	Add a to_xhtml() method to Perl6::Perldoc::Parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl6/Perl6-Perldoc-0.000011.tar.gz

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


