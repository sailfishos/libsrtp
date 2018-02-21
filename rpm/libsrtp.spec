Name:           libsrtp
Version:        2.1.0
Release:        0
Summary:        Secure Real-Time Transport Protocol (SRTP) library v2
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/cisco/libsrtp

Source:         https://github.com/cisco/libsrtp/archive/%name-%version.tar.gz
BuildRequires:  pkgconfig(openssl) >= 1.0.1

%description
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is
specified in RFC 3711. More information about the SRTP protocol
itself can be found on the Secure RTP page.

%package devel
Summary:        Development files for the Secure Real-Time Transport Protocol (SRTP) library v2
Group:          Development/Libraries/C and C++
Requires:       %{name} = %version

%description devel
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

This subpackage contains the development headers.

%prep
%setup -qn libsrtp-%version/%{name}

%build
%configure --enable-openssl
make shared_library %{?_smp_mflags}

%install
%make_install

%post   
/sbin/ldconfig || :

%postun 
/sbin/ldconfig || :

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_libdir}/libsrtp2.so.1

%files devel
%defattr(-,root,root)
%dir %{_includedir}/srtp2/
%{_includedir}/srtp2/*.h
%{_libdir}/libsrtp2.so
%{_libdir}/pkgconfig/libsrtp2.pc

