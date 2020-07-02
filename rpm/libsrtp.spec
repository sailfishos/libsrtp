Name:           libsrtp
Version:        2.3.0
Release:        1
Summary:        An implementation of the Secure Real-time Transport Protocol (SRTP)
License:        BSD
Url:            https://github.com/cisco/libsrtp
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(openssl) >= 1.0.1

%description
This package provides an implementation of the Secure Real-time
Transport Protocol (SRTP), the Universal Security Transform (UST), and
a supporting cryptographic kernel.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%configure --enable-openssl
make shared_library %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/%{name}2.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/srtp2/
%{_libdir}/%{name}2.so
%{_libdir}/pkgconfig/%{name}2.pc

%files doc
%defattr(-,root,root,-)
%doc CHANGES README.md
