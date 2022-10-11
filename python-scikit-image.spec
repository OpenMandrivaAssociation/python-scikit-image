%define module	 scikit-image
%define fname %(n=%{module}; echo ${n:0:1})

Summary:	Image processing in Python
Name:		python-%{module}
Version:	0.18.3
Release:	3
#Source0:	https://github.com/scikit-image/scikit-image/archive/refs/tags/v%{version}/%{module}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/%{fname}/%{module}/%{module}-%{version}.tar.gz
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
%{python3_sitearch}/skimage
%{python3_sitearch}/scikit_image-%{version}-py%{python_version}.egg-info/

#---------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

