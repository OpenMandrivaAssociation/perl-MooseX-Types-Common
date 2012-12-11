%define upstream_name    MooseX-Types-Common
%define upstream_version 0.001008

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

BuildArch: noarch

%description
A set of commonly-used type constraints that do not ship with Moose by
default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.1.2-2mdv2011.0
+ Revision: 655137
- rebuild for updated spec-helper

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 510080
- update to 0.001002

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.1-1mdv2010.1
+ Revision: 486308
- update to 0.001001

* Fri Dec 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 473275
- adding missing buildrequires:
- import perl-MooseX-Types-Common


* Fri Dec 04 2009 cpan2dist 0.001000-1mdv
- initial mdv release, generated with cpan2dist
