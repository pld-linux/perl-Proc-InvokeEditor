#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Proc
%define		pnam	InvokeEditor
Summary:	Proc::InvokeEditor - Perl extension for starting a text editor
Summary(pl.UTF-8):	Proc::InvokeEditor - rozszerzenie Perla do uruchamiania edytora tekstu
Name:		perl-Proc-InvokeEditor
Version:	1.13
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Proc/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26595c1e1c80ed64f0fb97cceea7e167
URL:		https://metacpan.org/dist/Proc-InvokeEditor
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Carp-Assert >= 0.11
BuildRequires:	perl-Test-Simple >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides the ability to supply some text to an external
text editor, have it edited by the user, and retrieve the results.

%description -l pl.UTF-8
Ten moduł pozwala na przekazanie tekstu do zewnętrznego edytora w celu
edycji przez użytkownika, a następnie odebrania wyniku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Proc/InvokeEditor.pm
%{_mandir}/man3/Proc::InvokeEditor.3pm*
%{_examplesdir}/%{name}-%{version}
