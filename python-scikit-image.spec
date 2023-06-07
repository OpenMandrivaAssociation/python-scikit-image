Summary:	Image processing in Python
Name:		python-scikit-image
Version:	0.21.0
Release:	1
Source0:	https://github.com/scikit-image/scikit-image/archive/refs/tags/v%{version}/scikit-image-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/s/scikit-image/scikit_image-%{version}.tar.gz
# (upstream)
# https://github.com/scikit-image/scikit-image/pull/6428
#Patch0:		python-scikit-image-0.3.19_fix-doc_install.patch
License:	BSD
Group:		Development/Python
Url:		https://scikit-image.org/

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pythran)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# for tests
BuildRequires:	python%{pyver}dist(imageio)
BuildRequires:	python%{pyver}dist(matplotlib)
BuildRequires:	python%{pyver}dist(networkx)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(tifffile)
BuildRequires:	python%{pyver}dist(pywavelets)

%description
This is a collection of image processing algorithms for Python.

%files
%license LICENSE.txt
%doc CONTRIBUTORS.txt RELEASE.txt
#{_bindir}/*
%{py_platsitedir}/skimage
%{py_platsitedir}/scikit_image*-info/

#---------------------------------------------------------------------------

%prep
%autosetup -n scikit-image-%{version}

%build
%py_build

%install
%py_install

