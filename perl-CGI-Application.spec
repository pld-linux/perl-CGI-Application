#
# Conditional build:
%bcond_with tests 	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Application
Summary:	CGI::Application - framework for building reusable web-applications
Summary(pl):	CGI::Application - szkielet do tworzenia aplikacji WWW wielokrotnego u�ytku
Name:		perl-CGI-Application
Version:	3.22
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cff5d3381c1d7f50c3ad3525045e063b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Module-Build >= 0.20
%if %{with tests}
BuildRequires:	perl-CGI
BuildRequires:	perl-HTML-Template
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-build >= 4.3-0.20030515.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application is intended to make it easier to create
sophisticated, reusable web-based applications. This module implements
a methodology which, if followed, will make your web software easier
to design, easier to document, easier to write, and easier to evolve.

%description -l pl
CGI::Application jest przeznaczony do u�atwiania tworzenia z�o�onych,
daj�cych si� ponownie wykorzystywa�, aplikacji opartych na WWW. Ten
modu� implementuje metodologi�, kt�ra - je�li stosowana - sprawi, �e
oprogramowanie sieciowe b�dzie prostsze w projektowaniu,
dokumentowaniu, pisaniu i ewoluowaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL Makefile.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README Changes
%{perl_vendorlib}/CGI/*.pm
%{perl_vendorlib}/CGI/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
