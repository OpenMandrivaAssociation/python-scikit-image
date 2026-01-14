%define module scikit-image
%define oname scikit_image

Name:		python-scikit-image
Summary:	Image processing in Python
Version:	0.26.0
Release:	1
Source0:	https://github.com/scikit-image/scikit-image/archive/refs/tags/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/s/scikit-image/scikit_image-%%{version}.tar.gz
# (upstream)
# https://github.com/scikit-image/scikit-image/pull/6428
#Patch0:		python-scikit-image-0.3.19_fix-doc_install.patch
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://scikit-image.org/
BuildSystem:	python
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(imageio)
BuildRequires:	python%{pyver}dist(lazy-loader)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(networkx)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pythran)
BuildRequires:	python%{pyver}dist(pywavelets)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tifffile)
BuildRequires:	python%{pyver}dist(wheel)
# for tests
BuildRequires:	python%{pyver}dist(matplotlib)
BuildRequires:	python%{pyver}dist(pytest)
Requires:	python%{pyver}dist(imageio)

%description
This is a collection of image processing algorithms for Python.

%prep
%autosetup -n %{module}-%{version} -p1
sed -Ei "1{s@/usr/bin/env python\$@%{_bindir}/python3@}" src/skimage/_build_utils/*.py
chmod -x src/skimage/measure/{__init__,_find_contours}.py
# we dont do code conformance testing
rm -rf tests/conftest.py

%build
export LDFLAGS="%{ldflags} -lpython%{pyver}"
%py_build

%install
%py_install

%files
%license LICENSE.txt
%{python_sitearch}/skimage
%{python_sitearch}/skimage2
%{python_sitearch}/%{oname}-%{version}.dist-info

