#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cheese
Version  : 41.0
Release  : 22
URL      : https://download.gnome.org/sources/cheese/41/cheese-41.0.tar.xz
Source0  : https://download.gnome.org/sources/cheese/41/cheese-41.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gdk-pixbuf
BuildRequires : gsettings-desktop-schemas-dev
BuildRequires : gtk-doc
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(clutter-gst-3.0)
BuildRequires : pkgconfig(clutter-gtk-1.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gnome-video-effects)
BuildRequires : pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires : pkgconfig(libcanberra)

%description
-----------------
Take photos and videos with your webcam, with fun graphical effects

%prep
%setup -q -n cheese-41.0
cd %{_builddir}/cheese-41.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642355739
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/cheese
cp %{_builddir}/cheese-41.0/COPYING %{buildroot}/usr/share/package-licenses/cheese/1f199f2dcc0341653fc919334d9c26d0d2098f93
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
