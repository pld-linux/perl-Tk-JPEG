#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	JPEG
Summary:	Tk::JPEG Perl module - JPEG loader for Tk::Photo
Summary(pl):	Modu³ Perla Tk::JPEG - obs³uga JPEG-ów dla Tk::Photo
Name:		perl-Tk-JPEG
Version:	2.014
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f697bc351548160491c7e06949250c86
Patch0:		%{name}-system.patch
BuildRequires:	libjpeg-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Tk >= 800.015
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::JPEG Perl extension which supplies JPEG format loader for Photo
image type.

%description -l pl
Rozszerzenie Perla Tk::JPEG pozwalaj±ce na odczyt plików JPEG do typu
obrazu Photo.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1
rm -f jpeg/Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install jpeg/README README-jpeg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README-jpeg
%attr(755,root,root) %{_bindir}/tkjpeg
%{perl_vendorarch}/Tk/JPEG.pm
%dir %{perl_vendorarch}/auto/Tk/JPEG
%{perl_vendorarch}/auto/Tk/JPEG/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/JPEG/*.so
%{_mandir}/man[13]/*
