%define		pkg	retry
Summary:	Abstraction for exponential and custom retry strategies for failed operations
Name:		nodejs-%{pkg}
Version:	0.6.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/tim-kos/retry
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	1f8567a864418f39263a4f6f81eac30e
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstraction for exponential and custom retry strategies for failed operations.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json *.js lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md License equation.gif
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
