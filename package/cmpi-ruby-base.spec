#
# spec file for package cmpi-ruby-base (Version 0.0.1)
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           cmpi-ruby-base
Url:            http://en.opensuse.org/Software_Management/CIM
License:        LGPL-2.1
Group:          System/Management
AutoReqProv:    on
Version:        0.0.1
Release:        2
Summary:        Base CMPI CIM providers
Source0:        %{name}-%{version}.tar.bz2
Requires:       cmpi-bindings-ruby
Requires:       cim-server
PreReq:         cmpi-provider-register
BuildRequires:  sblim-sfcb
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define mofdir /usr/share/mof/%{name}
%define cmpidir /usr/share/cmpi

%description
Set of CIM providers modeling base CIs of a Linux system


%prep
%setup -n %{name}

%build

%install
make install DESTDIR=%{buildroot}

%pre
if [ $1 -gt 1 ]; then
 /usr/sbin/cmpi-provider-register -r -x -d %{mofdir}
fi

%post
/usr/sbin/cmpi-provider-register -d %{mofdir}

%preun
if [ "$1" = "0" ] ; then
 /usr/sbin/cmpi-provider-register -r -d %{mofdir}
fi 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{cmpidir}
%{cmpidir}
%dir %{mofdir}
%{mofdir}

%changelog
