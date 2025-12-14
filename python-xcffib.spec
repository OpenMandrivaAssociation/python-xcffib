Name:		python-xcffib 
Version:	1.12.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
Summary:	xcffib is the XCB binding for Python 
URL:		https://github.com/tych0/xcffib
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(cffi)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  x11-server-xvfb
BuildRequires:  xeyes
Requires:  python%{pyver}dist(cffi)
BuildSystem:	python
BuildArch:	noarch

%description
xcffib is the XCB binding for Python 

%files
%{py_sitedir}/xcffib
%{py_sitedir}/xcffib-*.*-info
