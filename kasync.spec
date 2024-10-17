%define major 0
%define libname %mklibname KAsync
%define devname %mklibname KAsync -d
# Doesn't follow usual versioning schemes yet -- always unstable for now
%define stable unstable
%define git 20230809

Name:		kasync
Version:	0.3.1
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kasync/-/archive/master/kasync-master.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/kasync/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary:	KDE library for writing asynchronous code
URL: https://kde.org/
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
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
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
