#
# Conditional build:
%bcond_with tests 	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Application
Summary:	CGI::Application - Framework for building reusable web-applications
Summary(pl):	CGI::Application - Szkielet do tworzenia aplikacji WWW wielokrotnego u¿ytku
Name:		perl-CGI-Application
Version:	3.1
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
# Source0-md5:	9979fc246cfa31b40c202f7bb4c8b87f
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
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
CGI::Application jest przeznaczony do u³atwiania tworzenia z³o¿onych,
daj±cych siê ponownie wykorzystywaæ, aplikacji opartych na WWW. Ten
modu³ implementuje metodologiê, która - je¶li stosowana - sprawi, ¿e
oprogramowanie sieciowe bêdzie prostsze w projektowaniu,
dokumentowaniu, pisaniu i ewoluowaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
