Name:           compat-libmediaart0
Version:        0.7.0
Release:        1%{?dist}
Summary:        Compat package with libmediaart 0.7 libraries

License:        LGPLv2+
URL:            https://github.com/curlybeast/libmediaart
Source0:        https://download.gnome.org/sources/libmediaart/0.7/libmediaart-%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  vala-tools vala-devel

# Explicitly conflict with older libmediaart packages that ship libraries
# with the same soname as this compat package
Conflicts: libmediaart < 1.9

%description
Compatibility package with libmediaart 0.7 librarires.


%prep
%setup -q -n libmediaart-%{version}


%build
%configure --disable-static \
  --enable-gdkpixbuf \
  --disable-qt
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete -print

rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_datadir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING.LESSER
%{_libdir}/libmediaart-1.0.so.*


%changelog
* Thu Oct 20 2016 Kalev Lember <klember@redhat.com> - 0.7.0-1
- Initial libmediaart 0.7 compat package
