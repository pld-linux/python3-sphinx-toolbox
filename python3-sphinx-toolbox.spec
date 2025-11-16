Summary:	Box of handy tools for Sphinx
Summary(pl.UTF-8):	Zestaw przydatnych narzędzi dla Sphinksa
Name:		python3-sphinx-toolbox
Version:	4.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-toolbox/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_toolbox/sphinx_toolbox-%{version}.tar.gz
# Source0-md5:	13543d3ef8012fb821ddf1227cf7931e
Patch0:		deps.patch
URL:		https://github.com/sphinx-toolbox/sphinx-toolbox
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-whey
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Box of handy tools for Sphinx.

%description -l pl.UTF-8
Zestaw przydatnych narzędzi dla Sphinksa.

%prep
%setup -q -n sphinx_toolbox-%{version}
%patch -P0 -p1

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%dir %{py3_sitescriptdir}/sphinx_toolbox
%{py3_sitescriptdir}/sphinx_toolbox/*.py
%{py3_sitescriptdir}/sphinx_toolbox/__pycache__
%{py3_sitescriptdir}/sphinx_toolbox/py.typed
%dir %{py3_sitescriptdir}/sphinx_toolbox/github
%{py3_sitescriptdir}/sphinx_toolbox/github/*.py
%{py3_sitescriptdir}/sphinx_toolbox/github/__pycache__
%dir %{py3_sitescriptdir}/sphinx_toolbox/latex
%{py3_sitescriptdir}/sphinx_toolbox/latex/*.py
%{py3_sitescriptdir}/sphinx_toolbox/latex/__pycache__
%dir %{py3_sitescriptdir}/sphinx_toolbox/more_autodoc
%{py3_sitescriptdir}/sphinx_toolbox/more_autodoc/*.py
%{py3_sitescriptdir}/sphinx_toolbox/more_autodoc/__pycache__
%dir %{py3_sitescriptdir}/sphinx_toolbox/more_autosummary
%{py3_sitescriptdir}/sphinx_toolbox/more_autosummary/*.py
%{py3_sitescriptdir}/sphinx_toolbox/more_autosummary/__pycache__
%dir %{py3_sitescriptdir}/sphinx_toolbox/tweaks
%{py3_sitescriptdir}/sphinx_toolbox/tweaks/*.py
%{py3_sitescriptdir}/sphinx_toolbox/tweaks/__pycache__
%{py3_sitescriptdir}/sphinx_toolbox-%{version}.dist-info
