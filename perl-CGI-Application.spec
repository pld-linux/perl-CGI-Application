#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Application
Summary:	CGI::Application - Framework for building reusable web-applications
Summary(pl):	CGI::Application - Szkielet do tworzenia aplikacji WWW wielokrotnego u¿ytku
Name:		perl-CGI-Application
Version:	2.5
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-CGI
BuildRequires:	perl-HTML-Template
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application is intended to make it easier to create
sophisticated, reusable web-based applications. This module implements
a methodology which, if followed, will make your web software easier
to design, easier to document, easier to write, and easier to evolve.

%description -l pl
CGI::Application jest przeznaczony do u³atwiania tworzenia z³o¿onych,
daj±cych siê ponownie wykorzystywaæ, aplikacji opartych na WWW. Ten
modu³ implementuje metodologiê, która - je¶li stosowana - sprawi, ¿e
oprogramowanie sieciowe bêdzie prostsze w projektowaniu,
dokumentowaniu, pisaniu i ewoluowaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README Changes
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
