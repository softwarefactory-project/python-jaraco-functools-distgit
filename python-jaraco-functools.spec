%global sum     Additional functools in the spirit of stdlib's functools.
%global uname   jaraco.functools

Name:           python-jaraco-functools
Version:        1.15.2
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/jaraco/%{uname}
Source0:        https://github.com/jaraco/%{uname}/archive/%{version}.tar.gz

BuildArch:      noarch


%description
%{sum}

%package -n python2-jaraco-functools
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools_scm

Requires:       python-setuptools
Requires:       python2-more-itertools
Requires:       python2-backports-functools-lru-cache
Requires:       python-six


%description -n python2-jaraco-functools
%{sum}


%prep
%autosetup -n %{uname}-%{version}

# Remove setuptools_scm min version requirements
sed -i "s|setuptools_scm>=.*|setuptools_scm',|" setup.py


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py build


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py install --skip-build --root %{buildroot}
rm %{buildroot}%{python2_sitelib}/*-nspkg.pth


%files
%doc CHANGES.rst


%files -n python2-jaraco-functools
%{python2_sitelib}/jaraco.functools-%{version}-py*.egg-info
%{python2_sitelib}/jaraco/functools.py*


%changelog
* Thu Mar 16 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 1.15.2-1
- Initial packaging
