%global commit 453d2d4e326dc615b0bdb182fce581b01bec1a9b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20191030.%{shortcommit}
Name:           gologpp
Version:        0
Release:        12.%{snapinfo}%{?dist}
Summary:        An implementation-independent GOLOG language

License:        GPLv2+
URL:            https://github.com/MASKOR/gologpp
Source0:        https://github.com/MASKOR/gologpp/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://thofmann.fedorapeople.org/readylog.tar.gz

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
%cmake -DBUILD_TESTS=OFF ..
%make_build
cd -


%install
cd build
%make_install
cd -

mkdir -p %{buildroot}%{_datadir}/golog++/semantics/readylog
cp -a readylog/{interpreter,utils} %{buildroot}%{_datadir}/golog++/semantics/readylog


%files
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
