%define upstream_name    Perl6-Perldoc
%define upstream_version v0.0.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Add a to_xhtml() method to Perl6::Perldoc::Parser
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl6/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Filter::Simple)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module preprocesses your code from the point at which the module is
first used, stripping out any Perl 6 documentation (as specified in
Synopsis 26).

This means that, so long as your program starts with:

    use Perl6::Perldoc;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/perldoc2text
/usr/bin/perldoc2xhtml
/usr/share/man/man1/perldoc2text.1.lzma
/usr/share/man/man1/perldoc2xhtml.1.lzma

