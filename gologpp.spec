%global commit 78855fc6700a9bfc0e636e9dee63406a22c2eb1a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20191001.%{shortcommit}
Name:           gologpp
Version:        0
Release:        6.%{snapinfo}%{?dist}
Summary:        An implementation-independent GOLOG language

License:        GPLv2+
URL:            https://github.com/MASKOR/gologpp
Source0:        https://github.com/MASKOR/gologpp/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  eclipse-clp-devel < 7
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
An implementation-independent GOLOG language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}


%build
mkdir -p build
cd build
%cmake -DBUILD_TESTS=OFF ..
%make_build
cd -


%install
cd build
%make_install
cd -


%files
%{_libdir}/libgolog++.so.0*
%{_libdir}/libparsegolog++.so.0*
%{_libdir}/libreadylog++.so.0*
%{_datadir}/golog++

%files devel
%{_includedir}/golog++
%{_libdir}/libgolog++.so
%{_libdir}/libparsegolog++.so
%{_libdir}/libreadylog++.so
%{_libdir}/pkgconfig/golog++.pc
%{_libdir}/pkgconfig/parsegolog++.pc
%{_libdir}/pkgconfig/readylog++.pc


%changelog
* Tue Oct 01 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-6.20191001.78855fc
- Update to latest upstream commit

* Thu Sep 26 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-5.20190926.fa418f0
- Update to latest upstream commit
- Remove upstreamed patch

* Wed Sep 25 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-4.20190925.5418adb
- Add patch to fix templated constructors of gologpp::Value

* Wed Sep 25 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-3.20190925.5418adb
- Update to latest upstream commit
- Remove upstreamed patch

* Mon Sep 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-2.20190913.9167798
- Build against eclipse-clp to add readylog support
- Add patch to correctly detect eclipse-clp on Fedora
- Install readylog library

* Fri Sep 13 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-1.20190913.9167798
- Initial package
