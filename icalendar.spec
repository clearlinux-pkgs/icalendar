#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icalendar
Version  : 4.0.7
Release  : 36
URL      : https://files.pythonhosted.org/packages/58/b8/9aa7963f442b2a8bfdfc40eab8bc399c5eaac5711b8919c52122e4903544/icalendar-4.0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/b8/9aa7963f442b2a8bfdfc40eab8bc399c5eaac5711b8919c52122e4903544/icalendar-4.0.7.tar.gz
Summary  : iCalendar parser/generator
Group    : Development/Tools
License  : BSD-2-Clause
Requires: icalendar-bin = %{version}-%{release}
Requires: icalendar-license = %{version}-%{release}
Requires: icalendar-python = %{version}-%{release}
Requires: icalendar-python3 = %{version}-%{release}
Requires: python-dateutil
Requires: pytz
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : pytz
BuildRequires : tox
BuildRequires : virtualenv

%description
Internet Calendaring and Scheduling (iCalendar) for Python
        ==========================================================
        
        The `icalendar`_ package is a `RFC 5545`_ compatible parser/generator for iCalendar
        files.
        
        ----

%package bin
Summary: bin components for the icalendar package.
Group: Binaries
Requires: icalendar-license = %{version}-%{release}

%description bin
bin components for the icalendar package.


%package license
Summary: license components for the icalendar package.
Group: Default

%description license
license components for the icalendar package.


%package python
Summary: python components for the icalendar package.
Group: Default
Requires: icalendar-python3 = %{version}-%{release}

%description python
python components for the icalendar package.


%package python3
Summary: python3 components for the icalendar package.
Group: Default
Requires: python3-core
Provides: pypi(icalendar)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)

%description python3
python3 components for the icalendar package.


%prep
%setup -q -n icalendar-4.0.7
cd %{_builddir}/icalendar-4.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599598486
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/icalendar
cp %{_builddir}/icalendar-4.0.7/LICENSE.rst %{buildroot}/usr/share/package-licenses/icalendar/2615805ee0a7d616a284264feb385df7f0791482
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/icalendar

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/icalendar/2615805ee0a7d616a284264feb385df7f0791482

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
