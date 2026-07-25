%define upstream_name    MooseX-Types-Common
%define upstream_version 0.001015

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    1

Summary:    No summary found

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/moose/MooseX-Types-Common
Source0:    https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-Common-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires:  perl(namespace::autoclean)
BuildRequires: perl-devel

BuildArch: noarch

%description
A set of commonly-used type constraints that do not ship with Moose by
default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


