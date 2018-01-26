Name: 		helloworld
Version:	1.0
Release:	1%{?dist}
Summary:	Hello World RPM Package

Group:		Applications/System
License:	Public

Prefix: /usr/local/bin
Provides: hello-world.sh
URL: http://www.xxx.com
BuildRoot: %{builddir}/%{name}-root
BuildArchitectures: noarch
%description
Display hello world message

%prep
%build
%install
pwd
echo "RPM_BUILD_ROOT:" $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
cd $RPM_BUILD_ROOT/usr/local/bin/
cp ~/hello-world.sh .
%clean
%files
%defattr(-,root,root)
/usr/local/bin/hello-world.sh

%post
echo cat /usr/local/bin/hello-world.sh
cat /usr/local/bin/hello-world.sh
