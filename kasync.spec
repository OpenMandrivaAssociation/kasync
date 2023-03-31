%define major 0
%define libname %mklibname KAsync %{major}
%define devname %mklibname KAsync -d
# Doesn't follow usual versioning schemes yet -- always unstable for now
%define stable unstable

Name:		kasync
Version:	0.3.0
Release:	2
Source0:	http://download.kde.org/%{stable}/kasync/%{version}/src/%{name}-%{version}.tar.xz
Summary:	KDE library for writing asynchronous code
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)

%description
KAsync helps writing composable asynchronous code using a continuation
based approach.

%package -n %{libname}
Summary: KDE library for writing asynchronous code
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KAsync helps writing composable asynchronous code using a continuation
based approach.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
