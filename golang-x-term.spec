# Run tests in check section
%bcond_with check

# https://github.com/golang/term
%global goipath		golang.org/x/term
%global forgeurl	https://github.com/golang/term
Version:		0.24.0

%gometa

Summary:	Go terminal and console support
Name:		golang-x-term

Release:	1
Source0:	https://github.com/golang/term/archive/v%{version}/term-%{version}.tar.gz
URL:		https://github.com/golang/term
License:	BSD with advertising
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
This package provides terminal and console support packages for Go.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n term-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

