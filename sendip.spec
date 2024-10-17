%define name sendip
%define version 2.5
%define release 9

Summary: 	A command line tool to allow sending arbitrary IP packets
Name:    	%name
Version: 	%version
Release: 	%release
License: 	GPLv2
Group: 		Networking/Other
Source: 	http://www.earth.li/projectpurple/files/%name-%version.tar.gz
Patch0:		http://ftp.debian.org/debian/pool/main/s/sendip/sendip_2.5-2.diff.gz
URL: 		https://www.earth.li/projectpurple/progs/sendip.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
A command line tool to send arbitrary IP packets. It has a large number of
command line options to specify the content of every header of a NTP, BGP,
RIP, RIPng, TCP, UDP, ICMP, or raw IPv4 or IPv6 packet.  It also allows any 
data to be added to the packet.

%prep
%setup -q 
%patch0 -p1

%build
%make PREFIX=%_prefix

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make PREFIX=$RPM_BUILD_ROOT/usr MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install LIBDIR=$RPM_BUILD_ROOT/%_libdir/sendip

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/man1/sendip.1*
%{_bindir}/sendip
%{_libdir}/sendip/*.so
%doc README CHANGES LICENSE TODO



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.5-8mdv2010.0
+ Revision: 433691
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.5-7mdv2009.0
+ Revision: 260624
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.5-6mdv2009.0
+ Revision: 252312
- rebuild

* Wed Mar 05 2008 Gustavo De Nardin <gustavodn@mandriva.com> 2.5-4mdv2008.1
+ Revision: 179350
- fixed license tag
- set correct PREFIX when building, so it looks for modules in the right place, and actually works

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.5-3mdv2008.1
+ Revision: 127170
- kill re-definition of %%buildroot on Pixel's request
- import sendip


* Wed Apr 05 2006 Erwan Velu <velu@seanodes.com> 2.5-3mdk
- Fixing libdir for x86_64

* Mon Mar 20 2006 Erwan Velu <velu@seanodes.com> 2.5-2mdk
- Using debian's patch to make it compile cleanly
- mkrel

* Wed Jan 12 2004 Erwan Velu <velu@seanodes.com> 2.5-1mdk
- Initial mdk package


