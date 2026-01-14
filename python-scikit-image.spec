%define module scikit-image
%define oname scikit_image
# tests are too flaky and lots of them require network access.
%bcond tests 0

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
%if %{with tests}
BuildRequires:	python%{pyver}dist(matplotlib)
BuildRequires:	python%{pyver}dist(pytest)
%endif

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

%if %{with tests}
%check
# Fake matplotlibrc
mkdir -p matplotlib
touch matplotlib/matplotlibrc
# For test data
export XDG_CACHE_HOME=$PWD
export XDG_CONFIG_HOME=$PWD
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
# flaky test
skiptests+="test_wrap_around"
skiptests+=" or test_structural_similarity_dtype"
skiptests+=" or test_ellipse_parameter_stability"
skiptests+=" or test_thresholds_dask_compatibility"
skiptests+=" or test_io"
skiptests+=" or test_mpl_imshow"
skiptests+=" or test_random_walker"
# deselect tests that require network data
pytest -m "not network " -k "not $skiptests" \
  --deselect="skimage/io/tests/test_pil.py::test_imsave_filelike" \
  --deselect="skimage/io/tests/test_pil.py::test_all_mono" \
  --deselect="skimage/data/tests/test_data.py::test_download_all_with_pooch" \
  --deselect="skimage/data/tests/test_data.py::test_eagle" \
  --deselect="skimage/data/tests/test_data.py::test_brain_3d" \
  --deselect="skimage/data/tests/test_data.py::test_cells_3d" \
  --deselect="skimage/data/tests/test_data.py::test_kidney_3d_multichannel" \
  --deselect="skimage/data/tests/test_data.py::test_lily_multichannel" \
  --deselect="skimage/data/tests/test_data.py::test_skin" \
  --deselect="skimage/data/tests/test_data.py::test_vortex" \
  --deselect="skimage/measure/tests/test_blur_effect.py::test_blur_effect_3d" \
  --deselect="skimage/registration/tests/test_masked_phase_cross_correlation.py::test_masked_registration_3d_contiguous_mask" \
  --deselect="skimage/io/tests/test_imageio.py::TestSave::test_imsave_roundtrip[shape1-uint16]" \
  --deselect="skimage/measure/tests/test_fit.py::test_ellipse_parameter_stability" \
  --deselect="skimage/util/tests/test_regular_grid.py::test_regular_grid_2d_8" \
  --deselect="skimage/util/tests/test_regular_grid.py::test_regular_grid_3d_8" \
  --deselect="skimage/io/tests/test_imageio.py::TestSave::test_imsave_roundtrip[shape1-uint16]" \
  --deselect="skimage/io/tests/test_pil.py::test_all_mono" \
  --deselect="skimage/measure/tests/test_moments.py::test_analytical_moments_calculation[3-1-float32]" \
  --deselect="skimage/graph/tests/test_rag.py::test_reproducibility" \
  --deselect="skimage/measure/tests/test_moments.py::test_analytical_moments_calculation[2-1-float32]" \
%endif

%files
%license LICENSE.txt
%{python_sitearch}/skimage
%{python_sitearch}/%{oname}-%{version}.dist-info

