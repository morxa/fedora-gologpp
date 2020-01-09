%global commit 862730ba38d23aa4d78c52bbd158c4f195369b29
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20200107.%{shortcommit}

%global readylog_commit ecb9065a0e93b2bd91d09b269dd222632ee475ce
%global readylog_shortcommit %(c=%{readylog_commit}; echo ${c:0:7})

Name:           gologpp
Version:        0
Release:        23.%{snapinfo}%{?dist}
Summary:        An implementation-independent GOLOG language

License:        GPLv2+
URL:            https://github.com/MASKOR/gologpp
Source0:        https://github.com/MASKOR/gologpp/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://thofmann.fedorapeople.org/readylog-%{readylog_shortcommit}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  eclipse-clp-devel < 7
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
An implementation-independent GOLOG language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       eclipse-clp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        readylog
Summary:        A ReadyLog interpreter for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description    readylog
The readylog interpreter that can be used as an interpreter in Golog++.

%prep
%autosetup -p1 -n %{name}-%{commit}
%setup -T -D -a 1 -n %{name}-%{commit}


%build
mkdir -p build
cd build
%cmake -DBUILD_TESTS=ON ..
%make_build
cd -


%install
cd build
%make_install
cd -

mkdir -p %{buildroot}%{_datadir}/golog++/semantics/readylog
cp -a readylog/{interpreter,utils} %{buildroot}%{_datadir}/golog++/semantics/readylog

%check
cd build
READYLOG_PL=%{buildroot}%{_datadir}/golog++/semantics/readylog/interpreter
export READYLOG_PL
./readylog-test


%files
%{_bindir}/readylog-test
%{_libdir}/libgolog++.so.0*
%{_libdir}/libparsegolog++.so.0*
%{_libdir}/libreadylog++.so.0*
%dir %{_datadir}/golog++
%dir %{_datadir}/golog++/semantics

%files devel
%{_includedir}/golog++
%{_libdir}/libgolog++.so
%{_libdir}/libparsegolog++.so
%{_libdir}/libreadylog++.so
%{_libdir}/pkgconfig/golog++.pc
%{_libdir}/pkgconfig/parsegolog++.pc
%{_libdir}/pkgconfig/readylog++.pc

%files readylog
%{_datadir}/golog++/semantics/readylog


%changelog
* Thu Jan 09 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-23.20200107.862730b
- Update to latest upstream stable

* Tue Jan 07 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-22.20200107.f20457f
- Update to latest upstream stable

* Tue Jan 07 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-21.20200107.a63bf5c
- Switch to stable version of gologpp

* Thu Jan 02 2020 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-20.20200102.99bee85
- Update to latest upstream commit

* Mon Dec 16 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-19.20191216.ca264d1
- Update to latest upstream commit

* Mon Dec 16 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-18.20191216.26d91a0
- Update to latest upstream commit

* Tue Dec 10 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-17.20191210.d5bb828
- Update to latest upstream commit to include pconc fix

* Wed Nov 27 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-16.20191127.a33e84d
- Update to latest upstream commit

* Mon Nov 25 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-15.20191125.59265c1
- Update to latest upstream commit
- Build and run tests

* Mon Nov 11 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-14.20191111.96625c9
- Update to latest upstream commit

* Tue Nov 05 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-13.20191105.1c96ffc
- Update to latest upstream commit

* Wed Oct 30 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-12.20191030.453d2d4
- Update to latest upstream commit

* Tue Oct 29 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-11.20191022.b0588f0
- Add readylog sub-package

* Tue Oct 29 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-10.20191022.b0588f0
- Add patch to fix non-absolute path to Golog++ boilerplate

* Tue Oct 22 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-9.20191022.b0588f0
- Update to latest upstream commit

* Thu Oct 17 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-8.20191002.e102e4b
- Add Requires: eclipse-clp-devel to devel sub-package

* Wed Oct 02 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-7.20191002.e102e4b
- Update to latest upstream commit to include upstream PR #5

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
