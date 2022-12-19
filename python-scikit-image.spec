Summary:	Image processing in Python
Name:		python-scikit-image
Version:	0.19.3
Release:	1
#Source0:	https://github.com/scikit-image/scikit-image/archive/refs/tags/v%{version}/scikit-image-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/s/scikit-image/scikit-image-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://scikit-image.org/

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
# for tests
BuildRequires:	python3dist(imageio)
BuildRequires:	python3dist(matplotlib)
BuildRequires:	python3dist(networkx)
BuildRequires:	python3dist(pillow)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(tifffile)
BuildRequires:	python3dist(pywavelets)

%description
This is a collection of image processing algorithms for Python.

%files
%license LICENSE.txt
%doc CONTRIBUTORS.txt RELEASE.txt
%{_bindir}/*
%{py_platsitedir}/skimage
%{py_platsitedir}/scikit_image*-info/

#---------------------------------------------------------------------------

%prep
%autosetup -n scikit-image-%{version}

%build
%py_build

%install
%py_install

