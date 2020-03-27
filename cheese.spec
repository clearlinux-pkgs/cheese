#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cheese
Version  : 3.34.0
Release  : 16
URL      : https://download.gnome.org/sources/cheese/3.34/cheese-3.34.0.tar.xz
Source0  : https://download.gnome.org/sources/cheese/3.34/cheese-3.34.0.tar.xz
Summary  : Take photos and videos with your webcam, with fun graphical effects
Group    : Development/Tools
License  : GPL-2.0
Requires: cheese-bin = %{version}-%{release}
Requires: cheese-data = %{version}-%{release}
Requires: cheese-lib = %{version}-%{release}
Requires: cheese-license = %{version}-%{release}
Requires: cheese-locales = %{version}-%{release}
Requires: cheese-man = %{version}-%{release}
BuildRequires : appstream-glib
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
BuildRequires : pkgconfig(libcanberra-gtk3)

%description
-----------------
Take photos and videos with your webcam, with fun graphical effects

%package bin
Summary: bin components for the cheese package.
Group: Binaries
Requires: cheese-data = %{version}-%{release}
Requires: cheese-license = %{version}-%{release}

%description bin
bin components for the cheese package.


%package data
Summary: data components for the cheese package.
Group: Data

%description data
data components for the cheese package.


%package dev
Summary: dev components for the cheese package.
Group: Development
Requires: cheese-lib = %{version}-%{release}
Requires: cheese-bin = %{version}-%{release}
Requires: cheese-data = %{version}-%{release}
Provides: cheese-devel = %{version}-%{release}
Requires: cheese = %{version}-%{release}
Requires: cheese = %{version}-%{release}

%description dev
dev components for the cheese package.


%package doc
Summary: doc components for the cheese package.
Group: Documentation
Requires: cheese-man = %{version}-%{release}

%description doc
doc components for the cheese package.


%package lib
Summary: lib components for the cheese package.
Group: Libraries
Requires: cheese-data = %{version}-%{release}
Requires: cheese-license = %{version}-%{release}

%description lib
lib components for the cheese package.


%package license
Summary: license components for the cheese package.
Group: Default

%description license
license components for the cheese package.


%package locales
Summary: locales components for the cheese package.
Group: Default

%description locales
locales components for the cheese package.


%package man
Summary: man components for the cheese package.
Group: Default

%description man
man components for the cheese package.


%prep
%setup -q -n cheese-3.34.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568125712
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/cheese
cp COPYING %{buildroot}/usr/share/package-licenses/cheese/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang cheese

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cheese

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Cheese-3.0.typelib
/usr/share/applications/org.gnome.Cheese.desktop
/usr/share/dbus-1/services/org.gnome.Cheese.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Cheese.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Cheese-symbolic.svg
/usr/share/metainfo/org.gnome.Cheese.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/cheese/cheese-avatar-chooser.h
/usr/include/cheese/cheese-avatar-widget.h
/usr/include/cheese/cheese-camera-device-monitor.h
/usr/include/cheese/cheese-camera-device.h
/usr/include/cheese/cheese-camera.h
/usr/include/cheese/cheese-effect.h
/usr/include/cheese/cheese-gtk.h
/usr/include/cheese/cheese-resource.h
/usr/include/cheese/cheese-widget.h
/usr/include/cheese/cheese.h
/usr/lib64/libcheese-gtk.so
/usr/lib64/libcheese.so
/usr/lib64/pkgconfig/cheese-gtk.pc
/usr/lib64/pkgconfig/cheese.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/cheese/CheeseAvatarChooser.html
/usr/share/gtk-doc/html/cheese/CheeseAvatarWidget.html
/usr/share/gtk-doc/html/cheese/CheeseCamera.html
/usr/share/gtk-doc/html/cheese/CheeseCameraDevice.html
/usr/share/gtk-doc/html/cheese/CheeseCameraDeviceMonitor.html
/usr/share/gtk-doc/html/cheese/CheeseEffect.html
/usr/share/gtk-doc/html/cheese/CheeseFileUtil.html
/usr/share/gtk-doc/html/cheese/CheeseFlash.html
/usr/share/gtk-doc/html/cheese/CheeseWidget.html
/usr/share/gtk-doc/html/cheese/annotation-glossary.html
/usr/share/gtk-doc/html/cheese/api-index-deprecated.html
/usr/share/gtk-doc/html/cheese/api-index-full.html
/usr/share/gtk-doc/html/cheese/cheese-Initializing-libcheese-gtk.html
/usr/share/gtk-doc/html/cheese/cheese-Initializing-libcheese.html
/usr/share/gtk-doc/html/cheese/cheese-overview.html
/usr/share/gtk-doc/html/cheese/cheese.devhelp2
/usr/share/gtk-doc/html/cheese/cheese.html
/usr/share/gtk-doc/html/cheese/cheese_architecture.png
/usr/share/gtk-doc/html/cheese/home.png
/usr/share/gtk-doc/html/cheese/index.html
/usr/share/gtk-doc/html/cheese/left-insensitive.png
/usr/share/gtk-doc/html/cheese/left.png
/usr/share/gtk-doc/html/cheese/libcheese-gtk.html
/usr/share/gtk-doc/html/cheese/libcheese.html
/usr/share/gtk-doc/html/cheese/object-tree.html
/usr/share/gtk-doc/html/cheese/right-insensitive.png
/usr/share/gtk-doc/html/cheese/right.png
/usr/share/gtk-doc/html/cheese/running-cheese.html
/usr/share/gtk-doc/html/cheese/style.css
/usr/share/gtk-doc/html/cheese/up-insensitive.png
/usr/share/gtk-doc/html/cheese/up.png
/usr/share/help/C/cheese/burst-mode.page
/usr/share/help/C/cheese/effects-apply.page
/usr/share/help/C/cheese/figures/cheese.png
/usr/share/help/C/cheese/figures/effects.png
/usr/share/help/C/cheese/figures/image-properties.png
/usr/share/help/C/cheese/index.page
/usr/share/help/C/cheese/introduction.page
/usr/share/help/C/cheese/legal.xml
/usr/share/help/C/cheese/photo-delete.page
/usr/share/help/C/cheese/photo-save.page
/usr/share/help/C/cheese/photo-take.page
/usr/share/help/C/cheese/photo-view.page
/usr/share/help/C/cheese/pref-countdown.page
/usr/share/help/C/cheese/pref-flash.page
/usr/share/help/C/cheese/pref-fullscreen.page
/usr/share/help/C/cheese/pref-image-properties.page
/usr/share/help/C/cheese/pref-resolution.page
/usr/share/help/C/cheese/video-record.page
/usr/share/help/ca/cheese/burst-mode.page
/usr/share/help/ca/cheese/effects-apply.page
/usr/share/help/ca/cheese/figures/cheese.png
/usr/share/help/ca/cheese/figures/effects.png
/usr/share/help/ca/cheese/figures/image-properties.png
/usr/share/help/ca/cheese/index.page
/usr/share/help/ca/cheese/introduction.page
/usr/share/help/ca/cheese/legal.xml
/usr/share/help/ca/cheese/photo-delete.page
/usr/share/help/ca/cheese/photo-save.page
/usr/share/help/ca/cheese/photo-take.page
/usr/share/help/ca/cheese/photo-view.page
/usr/share/help/ca/cheese/pref-countdown.page
/usr/share/help/ca/cheese/pref-flash.page
/usr/share/help/ca/cheese/pref-fullscreen.page
/usr/share/help/ca/cheese/pref-image-properties.page
/usr/share/help/ca/cheese/pref-resolution.page
/usr/share/help/ca/cheese/video-record.page
/usr/share/help/cs/cheese/burst-mode.page
/usr/share/help/cs/cheese/effects-apply.page
/usr/share/help/cs/cheese/figures/cheese.png
/usr/share/help/cs/cheese/figures/effects.png
/usr/share/help/cs/cheese/figures/image-properties.png
/usr/share/help/cs/cheese/index.page
/usr/share/help/cs/cheese/introduction.page
/usr/share/help/cs/cheese/legal.xml
/usr/share/help/cs/cheese/photo-delete.page
/usr/share/help/cs/cheese/photo-save.page
/usr/share/help/cs/cheese/photo-take.page
/usr/share/help/cs/cheese/photo-view.page
/usr/share/help/cs/cheese/pref-countdown.page
/usr/share/help/cs/cheese/pref-flash.page
/usr/share/help/cs/cheese/pref-fullscreen.page
/usr/share/help/cs/cheese/pref-image-properties.page
/usr/share/help/cs/cheese/pref-resolution.page
/usr/share/help/cs/cheese/video-record.page
/usr/share/help/de/cheese/burst-mode.page
/usr/share/help/de/cheese/effects-apply.page
/usr/share/help/de/cheese/figures/cheese.png
/usr/share/help/de/cheese/figures/effects.png
/usr/share/help/de/cheese/figures/image-properties.png
/usr/share/help/de/cheese/index.page
/usr/share/help/de/cheese/introduction.page
/usr/share/help/de/cheese/legal.xml
/usr/share/help/de/cheese/photo-delete.page
/usr/share/help/de/cheese/photo-save.page
/usr/share/help/de/cheese/photo-take.page
/usr/share/help/de/cheese/photo-view.page
/usr/share/help/de/cheese/pref-countdown.page
/usr/share/help/de/cheese/pref-flash.page
/usr/share/help/de/cheese/pref-fullscreen.page
/usr/share/help/de/cheese/pref-image-properties.page
/usr/share/help/de/cheese/pref-resolution.page
/usr/share/help/de/cheese/video-record.page
/usr/share/help/el/cheese/burst-mode.page
/usr/share/help/el/cheese/effects-apply.page
/usr/share/help/el/cheese/figures/cheese.png
/usr/share/help/el/cheese/figures/effects.png
/usr/share/help/el/cheese/figures/image-properties.png
/usr/share/help/el/cheese/index.page
/usr/share/help/el/cheese/introduction.page
/usr/share/help/el/cheese/legal.xml
/usr/share/help/el/cheese/photo-delete.page
/usr/share/help/el/cheese/photo-save.page
/usr/share/help/el/cheese/photo-take.page
/usr/share/help/el/cheese/photo-view.page
/usr/share/help/el/cheese/pref-countdown.page
/usr/share/help/el/cheese/pref-flash.page
/usr/share/help/el/cheese/pref-fullscreen.page
/usr/share/help/el/cheese/pref-image-properties.page
/usr/share/help/el/cheese/pref-resolution.page
/usr/share/help/el/cheese/video-record.page
/usr/share/help/es/cheese/burst-mode.page
/usr/share/help/es/cheese/effects-apply.page
/usr/share/help/es/cheese/figures/cheese.png
/usr/share/help/es/cheese/figures/effects.png
/usr/share/help/es/cheese/figures/image-properties.png
/usr/share/help/es/cheese/index.page
/usr/share/help/es/cheese/introduction.page
/usr/share/help/es/cheese/legal.xml
/usr/share/help/es/cheese/photo-delete.page
/usr/share/help/es/cheese/photo-save.page
/usr/share/help/es/cheese/photo-take.page
/usr/share/help/es/cheese/photo-view.page
/usr/share/help/es/cheese/pref-countdown.page
/usr/share/help/es/cheese/pref-flash.page
/usr/share/help/es/cheese/pref-fullscreen.page
/usr/share/help/es/cheese/pref-image-properties.page
/usr/share/help/es/cheese/pref-resolution.page
/usr/share/help/es/cheese/video-record.page
/usr/share/help/fi/cheese/burst-mode.page
/usr/share/help/fi/cheese/effects-apply.page
/usr/share/help/fi/cheese/figures/cheese.png
/usr/share/help/fi/cheese/figures/effects.png
/usr/share/help/fi/cheese/figures/image-properties.png
/usr/share/help/fi/cheese/index.page
/usr/share/help/fi/cheese/introduction.page
/usr/share/help/fi/cheese/legal.xml
/usr/share/help/fi/cheese/photo-delete.page
/usr/share/help/fi/cheese/photo-save.page
/usr/share/help/fi/cheese/photo-take.page
/usr/share/help/fi/cheese/photo-view.page
/usr/share/help/fi/cheese/pref-countdown.page
/usr/share/help/fi/cheese/pref-flash.page
/usr/share/help/fi/cheese/pref-fullscreen.page
/usr/share/help/fi/cheese/pref-image-properties.page
/usr/share/help/fi/cheese/pref-resolution.page
/usr/share/help/fi/cheese/video-record.page
/usr/share/help/fr/cheese/burst-mode.page
/usr/share/help/fr/cheese/effects-apply.page
/usr/share/help/fr/cheese/figures/cheese.png
/usr/share/help/fr/cheese/figures/effects.png
/usr/share/help/fr/cheese/figures/image-properties.png
/usr/share/help/fr/cheese/index.page
/usr/share/help/fr/cheese/introduction.page
/usr/share/help/fr/cheese/legal.xml
/usr/share/help/fr/cheese/photo-delete.page
/usr/share/help/fr/cheese/photo-save.page
/usr/share/help/fr/cheese/photo-take.page
/usr/share/help/fr/cheese/photo-view.page
/usr/share/help/fr/cheese/pref-countdown.page
/usr/share/help/fr/cheese/pref-flash.page
/usr/share/help/fr/cheese/pref-fullscreen.page
/usr/share/help/fr/cheese/pref-image-properties.page
/usr/share/help/fr/cheese/pref-resolution.page
/usr/share/help/fr/cheese/video-record.page
/usr/share/help/gl/cheese/burst-mode.page
/usr/share/help/gl/cheese/effects-apply.page
/usr/share/help/gl/cheese/figures/cheese.png
/usr/share/help/gl/cheese/figures/effects.png
/usr/share/help/gl/cheese/figures/image-properties.png
/usr/share/help/gl/cheese/index.page
/usr/share/help/gl/cheese/introduction.page
/usr/share/help/gl/cheese/legal.xml
/usr/share/help/gl/cheese/photo-delete.page
/usr/share/help/gl/cheese/photo-save.page
/usr/share/help/gl/cheese/photo-take.page
/usr/share/help/gl/cheese/photo-view.page
/usr/share/help/gl/cheese/pref-countdown.page
/usr/share/help/gl/cheese/pref-flash.page
/usr/share/help/gl/cheese/pref-fullscreen.page
/usr/share/help/gl/cheese/pref-image-properties.page
/usr/share/help/gl/cheese/pref-resolution.page
/usr/share/help/gl/cheese/video-record.page
/usr/share/help/hu/cheese/burst-mode.page
/usr/share/help/hu/cheese/effects-apply.page
/usr/share/help/hu/cheese/figures/cheese.png
/usr/share/help/hu/cheese/figures/effects.png
/usr/share/help/hu/cheese/figures/image-properties.png
/usr/share/help/hu/cheese/index.page
/usr/share/help/hu/cheese/introduction.page
/usr/share/help/hu/cheese/legal.xml
/usr/share/help/hu/cheese/photo-delete.page
/usr/share/help/hu/cheese/photo-save.page
/usr/share/help/hu/cheese/photo-take.page
/usr/share/help/hu/cheese/photo-view.page
/usr/share/help/hu/cheese/pref-countdown.page
/usr/share/help/hu/cheese/pref-flash.page
/usr/share/help/hu/cheese/pref-fullscreen.page
/usr/share/help/hu/cheese/pref-image-properties.page
/usr/share/help/hu/cheese/pref-resolution.page
/usr/share/help/hu/cheese/video-record.page
/usr/share/help/id/cheese/burst-mode.page
/usr/share/help/id/cheese/effects-apply.page
/usr/share/help/id/cheese/figures/cheese.png
/usr/share/help/id/cheese/figures/effects.png
/usr/share/help/id/cheese/figures/image-properties.png
/usr/share/help/id/cheese/index.page
/usr/share/help/id/cheese/introduction.page
/usr/share/help/id/cheese/legal.xml
/usr/share/help/id/cheese/photo-delete.page
/usr/share/help/id/cheese/photo-save.page
/usr/share/help/id/cheese/photo-take.page
/usr/share/help/id/cheese/photo-view.page
/usr/share/help/id/cheese/pref-countdown.page
/usr/share/help/id/cheese/pref-flash.page
/usr/share/help/id/cheese/pref-fullscreen.page
/usr/share/help/id/cheese/pref-image-properties.page
/usr/share/help/id/cheese/pref-resolution.page
/usr/share/help/id/cheese/video-record.page
/usr/share/help/ko/cheese/burst-mode.page
/usr/share/help/ko/cheese/effects-apply.page
/usr/share/help/ko/cheese/figures/cheese.png
/usr/share/help/ko/cheese/figures/effects.png
/usr/share/help/ko/cheese/figures/image-properties.png
/usr/share/help/ko/cheese/index.page
/usr/share/help/ko/cheese/introduction.page
/usr/share/help/ko/cheese/legal.xml
/usr/share/help/ko/cheese/photo-delete.page
/usr/share/help/ko/cheese/photo-save.page
/usr/share/help/ko/cheese/photo-take.page
/usr/share/help/ko/cheese/photo-view.page
/usr/share/help/ko/cheese/pref-countdown.page
/usr/share/help/ko/cheese/pref-flash.page
/usr/share/help/ko/cheese/pref-fullscreen.page
/usr/share/help/ko/cheese/pref-image-properties.page
/usr/share/help/ko/cheese/pref-resolution.page
/usr/share/help/ko/cheese/video-record.page
/usr/share/help/nl/cheese/burst-mode.page
/usr/share/help/nl/cheese/effects-apply.page
/usr/share/help/nl/cheese/figures/cheese.png
/usr/share/help/nl/cheese/figures/effects.png
/usr/share/help/nl/cheese/figures/image-properties.png
/usr/share/help/nl/cheese/index.page
/usr/share/help/nl/cheese/introduction.page
/usr/share/help/nl/cheese/legal.xml
/usr/share/help/nl/cheese/photo-delete.page
/usr/share/help/nl/cheese/photo-save.page
/usr/share/help/nl/cheese/photo-take.page
/usr/share/help/nl/cheese/photo-view.page
/usr/share/help/nl/cheese/pref-countdown.page
/usr/share/help/nl/cheese/pref-flash.page
/usr/share/help/nl/cheese/pref-fullscreen.page
/usr/share/help/nl/cheese/pref-image-properties.page
/usr/share/help/nl/cheese/pref-resolution.page
/usr/share/help/nl/cheese/video-record.page
/usr/share/help/pl/cheese/burst-mode.page
/usr/share/help/pl/cheese/effects-apply.page
/usr/share/help/pl/cheese/figures/cheese.png
/usr/share/help/pl/cheese/figures/effects.png
/usr/share/help/pl/cheese/figures/image-properties.png
/usr/share/help/pl/cheese/index.page
/usr/share/help/pl/cheese/introduction.page
/usr/share/help/pl/cheese/legal.xml
/usr/share/help/pl/cheese/photo-delete.page
/usr/share/help/pl/cheese/photo-save.page
/usr/share/help/pl/cheese/photo-take.page
/usr/share/help/pl/cheese/photo-view.page
/usr/share/help/pl/cheese/pref-countdown.page
/usr/share/help/pl/cheese/pref-flash.page
/usr/share/help/pl/cheese/pref-fullscreen.page
/usr/share/help/pl/cheese/pref-image-properties.page
/usr/share/help/pl/cheese/pref-resolution.page
/usr/share/help/pl/cheese/video-record.page
/usr/share/help/pt_BR/cheese/burst-mode.page
/usr/share/help/pt_BR/cheese/effects-apply.page
/usr/share/help/pt_BR/cheese/figures/cheese.png
/usr/share/help/pt_BR/cheese/figures/effects.png
/usr/share/help/pt_BR/cheese/figures/image-properties.png
/usr/share/help/pt_BR/cheese/index.page
/usr/share/help/pt_BR/cheese/introduction.page
/usr/share/help/pt_BR/cheese/legal.xml
/usr/share/help/pt_BR/cheese/photo-delete.page
/usr/share/help/pt_BR/cheese/photo-save.page
/usr/share/help/pt_BR/cheese/photo-take.page
/usr/share/help/pt_BR/cheese/photo-view.page
/usr/share/help/pt_BR/cheese/pref-countdown.page
/usr/share/help/pt_BR/cheese/pref-flash.page
/usr/share/help/pt_BR/cheese/pref-fullscreen.page
/usr/share/help/pt_BR/cheese/pref-image-properties.page
/usr/share/help/pt_BR/cheese/pref-resolution.page
/usr/share/help/pt_BR/cheese/video-record.page
/usr/share/help/ru/cheese/burst-mode.page
/usr/share/help/ru/cheese/effects-apply.page
/usr/share/help/ru/cheese/figures/cheese.png
/usr/share/help/ru/cheese/figures/effects.png
/usr/share/help/ru/cheese/figures/image-properties.png
/usr/share/help/ru/cheese/index.page
/usr/share/help/ru/cheese/introduction.page
/usr/share/help/ru/cheese/legal.xml
/usr/share/help/ru/cheese/photo-delete.page
/usr/share/help/ru/cheese/photo-save.page
/usr/share/help/ru/cheese/photo-take.page
/usr/share/help/ru/cheese/photo-view.page
/usr/share/help/ru/cheese/pref-countdown.page
/usr/share/help/ru/cheese/pref-flash.page
/usr/share/help/ru/cheese/pref-fullscreen.page
/usr/share/help/ru/cheese/pref-image-properties.page
/usr/share/help/ru/cheese/pref-resolution.page
/usr/share/help/ru/cheese/video-record.page
/usr/share/help/sl/cheese/burst-mode.page
/usr/share/help/sl/cheese/effects-apply.page
/usr/share/help/sl/cheese/figures/cheese.png
/usr/share/help/sl/cheese/figures/effects.png
/usr/share/help/sl/cheese/figures/image-properties.png
/usr/share/help/sl/cheese/index.page
/usr/share/help/sl/cheese/introduction.page
/usr/share/help/sl/cheese/legal.xml
/usr/share/help/sl/cheese/photo-delete.page
/usr/share/help/sl/cheese/photo-save.page
/usr/share/help/sl/cheese/photo-take.page
/usr/share/help/sl/cheese/photo-view.page
/usr/share/help/sl/cheese/pref-countdown.page
/usr/share/help/sl/cheese/pref-flash.page
/usr/share/help/sl/cheese/pref-fullscreen.page
/usr/share/help/sl/cheese/pref-image-properties.page
/usr/share/help/sl/cheese/pref-resolution.page
/usr/share/help/sl/cheese/video-record.page
/usr/share/help/sv/cheese/burst-mode.page
/usr/share/help/sv/cheese/effects-apply.page
/usr/share/help/sv/cheese/figures/cheese.png
/usr/share/help/sv/cheese/figures/effects.png
/usr/share/help/sv/cheese/figures/image-properties.png
/usr/share/help/sv/cheese/index.page
/usr/share/help/sv/cheese/introduction.page
/usr/share/help/sv/cheese/legal.xml
/usr/share/help/sv/cheese/photo-delete.page
/usr/share/help/sv/cheese/photo-save.page
/usr/share/help/sv/cheese/photo-take.page
/usr/share/help/sv/cheese/photo-view.page
/usr/share/help/sv/cheese/pref-countdown.page
/usr/share/help/sv/cheese/pref-flash.page
/usr/share/help/sv/cheese/pref-fullscreen.page
/usr/share/help/sv/cheese/pref-image-properties.page
/usr/share/help/sv/cheese/pref-resolution.page
/usr/share/help/sv/cheese/video-record.page
/usr/share/help/zh_CN/cheese/burst-mode.page
/usr/share/help/zh_CN/cheese/effects-apply.page
/usr/share/help/zh_CN/cheese/figures/cheese.png
/usr/share/help/zh_CN/cheese/figures/effects.png
/usr/share/help/zh_CN/cheese/figures/image-properties.png
/usr/share/help/zh_CN/cheese/index.page
/usr/share/help/zh_CN/cheese/introduction.page
/usr/share/help/zh_CN/cheese/legal.xml
/usr/share/help/zh_CN/cheese/photo-delete.page
/usr/share/help/zh_CN/cheese/photo-save.page
/usr/share/help/zh_CN/cheese/photo-take.page
/usr/share/help/zh_CN/cheese/photo-view.page
/usr/share/help/zh_CN/cheese/pref-countdown.page
/usr/share/help/zh_CN/cheese/pref-flash.page
/usr/share/help/zh_CN/cheese/pref-fullscreen.page
/usr/share/help/zh_CN/cheese/pref-image-properties.page
/usr/share/help/zh_CN/cheese/pref-resolution.page
/usr/share/help/zh_CN/cheese/video-record.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcheese-gtk.so.25
/usr/lib64/libcheese-gtk.so.25.1.4
/usr/lib64/libcheese.so.8
/usr/lib64/libcheese.so.8.0.14

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cheese/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cheese.1

%files locales -f cheese.lang
%defattr(-,root,root,-)

