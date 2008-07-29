%define name sendip
%define version 2.5
%define release %mkrel 6

Summary: 	A command line tool to allow sending arbitrary IP packets
Name:    	%name
Version: 	%version
Release: 	%release
License: 	GPLv2
Group: 		Networking/Other
Source: 	http://www.earth.li/projectpurple/files/%name-%version.tar.gz
Patch0:		http://ftp.debian.org/debian/pool/main/s/sendip/sendip_2.5-2.diff.gz
URL: 		http://www.earth.li/projectpurple/progs/sendip.html
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

