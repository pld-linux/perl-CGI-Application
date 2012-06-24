#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Application
Summary:	CGI::Application - Framework for building reusable web-applications
#Summary(pl):	CGI::Application - Szkielet do budowania [?] aplikacji WWW
Name:		perl-CGI-Application
Version:	2.5
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-CGI
BuildRequires:	perl-HTML-Template
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application is intended to make it easier to create sophisticated,
reusable web-based applications.  This module implements a methodology
which, if followed, will make your web software easier to design, easier
to document, easier to write, and easier to evolve.

# %description -l pl
# FIXME
# CGI::Application jest przeznaczony do u�atwiania tworzenia z�o�onych,
# [ jak przet�umaczy� ,,reusable''? ] aplikacji opartych na WWW.  Ten modu�
# implementuje metodologi�, kt�ra -- je�li stosowana -- sprawi, �e Twoje
# oprogramowanie sieciowe b�dzie prostrze w projektowaniu, dokumentowaniu,
# pisaniu i ewoluowaniu.

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
