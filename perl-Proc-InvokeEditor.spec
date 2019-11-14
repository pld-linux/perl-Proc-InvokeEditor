#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Proc
%define		pnam	InvokeEditor
%include	/usr/lib/rpm/macros.perl
Summary:	Proc::InvokeEditor - Perl extension for starting a text editor
Name:		perl-Proc-InvokeEditor
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Proc/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26595c1e1c80ed64f0fb97cceea7e167
URL:		http://search.cpan.org/dist/Proc-InvokeEditor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Carp::Assert) >= 0.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides the ability to supply some text to an external
text editor, have it edited by the user, and retrieve the results.

The File::Temp module is used to provide secure, safe temporary
files, and File::Temp is set to its highest available level of
security. This may cause problems on some systems where no secure
temporary directory is available.

When the editor is started, no subshell is used. Your path will
be scanned to find the binary to use for each editor if the string
given does not exist as a file, and if a named editor contains whitespace,
eg) if you try to use the editor xemacs -nw, then the string will
be split on whitespace and anything after the editor name will be passed
as arguments to your editor. A shell is not used but this should cover
most simple cases.

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
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
