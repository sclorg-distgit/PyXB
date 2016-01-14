%global pkg_name PyXB
%{?scl:%scl_package %{pkg_name}}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.2.4
Release:        1.4%{?dist}
Summary:        Python XML Schema Bindings
License:        Apache
URL:            http://pyxb.sourceforge.net/
Source0:        https://github.com/pabigot/pyxb/archive/%{pkg_name}-%{version}.tar.gz
BuildArch:      noarch

BuildArch:      noarch
BuildRequires:  python-devel

%{?scl:Requires: %{scl_prefix}runtime}

%description
PyXB (“pixbee”) is a pure Python package that generates Python source
code for classes that correspond to data structures defined by
XMLSchema.

%package doc
Summary:        PyXB documentation
%{?scl:Requires: %{scl_prefix}runtime}

%description doc
This package contains documentation and examples for PyXB.

%prep
%setup -q -n pyxb-%{pkg_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}%{?_scl_root}
rm -rf %{buildroot}%{python_sitelib}/pyxb/tests

%check
%{__python} setup.py test

%files
%doc LICENSE NOTICE
%{?_scl_root}%{python_sitelib}/*
%{_bindir}/pyxbdump
%{_bindir}/pyxbgen
%{_bindir}/pyxbwsdl

%files doc
%doc doc/* LICENSE NOTICE README.txt examples/*

%changelog
* Fri Jan 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.4-1.4
- Add missing requires on rh-java-common-runtime

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.2.4-1.3
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 1.2.4-1.2
- Mass rebuild 2015-01-09

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.4-1.1
- SCL-ize package

* Mon Oct 20 2014 Michal Srb <msrb@redhat.com> - 1.2.4-1
- Update to official upstream version 1.2.4

* Mon Sep 22 2014 Michal Srb <msrb@redhat.com> - 1.2.4-0.2.gitc494ba3
- Move documentation and examples to subpackage (Resolves: rhbz#1144488)

* Thu Jul 17 2014 Michal Srb <msrb@redhat.com> - 1.2.4-0.1
- Update to prerelease version 1.2.4
- Add python3 subpackage

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-1
- Update to upstream version 1.2.3
- Resolves: rhbz#1086133

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 16 2011 Marek Mahut <mmahut@fedoraproject.org> - 1.1.2-1
- Initial build
