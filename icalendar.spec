#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icalendar
Version  : 3.11.7
Release  : 5
URL      : http://pypi.debian.net/icalendar/icalendar-3.11.7.tar.gz
Source0  : http://pypi.debian.net/icalendar/icalendar-3.11.7.tar.gz
Summary  : iCalendar parser/generator
Group    : Development/Tools
License  : BSD-2-Clause
Requires: icalendar-python3
Requires: icalendar-python
Requires: python-dateutil
Requires: pytz
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Internet Calendaring and Scheduling (iCalendar) for Python
        ==========================================================
        
        The `icalendar`_ package is a parser/generator of iCalendar files for use
        with Python.
        
        ----

%package python
Summary: python components for the icalendar package.
Group: Default
Requires: icalendar-python3

%description python
python components for the icalendar package.


%package python3
Summary: python3 components for the icalendar package.
Group: Default
Requires: python3-core

%description python3
python3 components for the icalendar package.


%prep
%setup -q -n icalendar-3.11.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507155127
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
