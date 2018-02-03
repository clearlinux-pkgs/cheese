#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cheese
Version  : 3.26.0
Release  : 5
URL      : https://download.gnome.org/sources/cheese/3.26/cheese-3.26.0.tar.xz
Source0  : https://download.gnome.org/sources/cheese/3.26/cheese-3.26.0.tar.xz
Summary  : Cheese webcam utilities
Group    : Development/Tools
License  : GPL-2.0
Requires: cheese-bin
Requires: cheese-data
Requires: cheese-lib
Requires: cheese-doc
Requires: cheese-locales
BuildRequires : docbook-xml
BuildRequires : gdk-pixbuf
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(clutter-gst-3.0)
BuildRequires : pkgconfig(clutter-gtk-1.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : sed

%description
-----------------
Take photos and videos with your webcam, with fun graphical effects

%package bin
Summary: bin components for the cheese package.
Group: Binaries
Requires: cheese-data

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
Requires: cheese-lib
Requires: cheese-bin
Requires: cheese-data
Provides: cheese-devel

%description dev
dev components for the cheese package.


%package doc
Summary: doc components for the cheese package.
Group: Documentation

%description doc
doc components for the cheese package.


%package lib
Summary: lib components for the cheese package.
Group: Libraries
Requires: cheese-data

%description lib
lib components for the cheese package.


%package locales
Summary: locales components for the cheese package.
Group: Default

%description locales
locales components for the cheese package.


%prep
%setup -q -n cheese-3.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517619939
%configure --disable-static --disable-schemas-compile
make

%install
export SOURCE_DATE_EPOCH=1517619939
rm -rf %{buildroot}
%make_install
%find_lang cheese

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cheese

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Cheese-3.0.typelib
/usr/share/appdata/org.gnome.Cheese.appdata.xml
/usr/share/applications/org.gnome.Cheese.desktop
/usr/share/dbus-1/services/org.gnome.Cheese.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
/usr/share/icons/hicolor/16x16/apps/org.gnome.Cheese.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Cheese.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.Cheese.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.Cheese.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Cheese.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Cheese.png
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Cheese-symbolic.svg

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
%defattr(-,root,root,-)
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
/usr/share/help/C/cheese/figures/cheese-delete.png
/usr/share/help/C/cheese/figures/cheese-effects.png
/usr/share/help/C/cheese/figures/cheese-introduction.png
/usr/share/help/C/cheese/figures/cheese-record.png
/usr/share/help/C/cheese/figures/cheese-save.png
/usr/share/help/C/cheese/figures/cheese-take.png
/usr/share/help/C/cheese/figures/cheese.png
/usr/share/help/C/cheese/figures/effects.png
/usr/share/help/C/cheese/figures/image-properties.png
/usr/share/help/C/cheese/figures/settings.png
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
/usr/share/help/ca/cheese/figures/cheese-delete.png
/usr/share/help/ca/cheese/figures/cheese-effects.png
/usr/share/help/ca/cheese/figures/cheese-introduction.png
/usr/share/help/ca/cheese/figures/cheese-record.png
/usr/share/help/ca/cheese/figures/cheese-save.png
/usr/share/help/ca/cheese/figures/cheese-take.png
/usr/share/help/ca/cheese/figures/cheese.png
/usr/share/help/ca/cheese/figures/effects.png
/usr/share/help/ca/cheese/figures/image-properties.png
/usr/share/help/ca/cheese/figures/settings.png
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
/usr/share/help/cs/cheese/figures/cheese-delete.png
/usr/share/help/cs/cheese/figures/cheese-effects.png
/usr/share/help/cs/cheese/figures/cheese-introduction.png
/usr/share/help/cs/cheese/figures/cheese-record.png
/usr/share/help/cs/cheese/figures/cheese-save.png
/usr/share/help/cs/cheese/figures/cheese-take.png
/usr/share/help/cs/cheese/figures/cheese.png
/usr/share/help/cs/cheese/figures/effects.png
/usr/share/help/cs/cheese/figures/image-properties.png
/usr/share/help/cs/cheese/figures/settings.png
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
/usr/share/help/de/cheese/figures/cheese-delete.png
/usr/share/help/de/cheese/figures/cheese-effects.png
/usr/share/help/de/cheese/figures/cheese-introduction.png
/usr/share/help/de/cheese/figures/cheese-record.png
/usr/share/help/de/cheese/figures/cheese-save.png
/usr/share/help/de/cheese/figures/cheese-take.png
/usr/share/help/de/cheese/figures/cheese.png
/usr/share/help/de/cheese/figures/effects.png
/usr/share/help/de/cheese/figures/image-properties.png
/usr/share/help/de/cheese/figures/settings.png
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
/usr/share/help/el/cheese/figures/cheese-delete.png
/usr/share/help/el/cheese/figures/cheese-effects.png
/usr/share/help/el/cheese/figures/cheese-introduction.png
/usr/share/help/el/cheese/figures/cheese-record.png
/usr/share/help/el/cheese/figures/cheese-save.png
/usr/share/help/el/cheese/figures/cheese-take.png
/usr/share/help/el/cheese/figures/cheese.png
/usr/share/help/el/cheese/figures/effects.png
/usr/share/help/el/cheese/figures/image-properties.png
/usr/share/help/el/cheese/figures/settings.png
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
/usr/share/help/es/cheese/figures/cheese-delete.png
/usr/share/help/es/cheese/figures/cheese-effects.png
/usr/share/help/es/cheese/figures/cheese-introduction.png
/usr/share/help/es/cheese/figures/cheese-record.png
/usr/share/help/es/cheese/figures/cheese-save.png
/usr/share/help/es/cheese/figures/cheese-take.png
/usr/share/help/es/cheese/figures/cheese.png
/usr/share/help/es/cheese/figures/effects.png
/usr/share/help/es/cheese/figures/image-properties.png
/usr/share/help/es/cheese/figures/settings.png
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
/usr/share/help/fi/cheese/figures/cheese-delete.png
/usr/share/help/fi/cheese/figures/cheese-effects.png
/usr/share/help/fi/cheese/figures/cheese-introduction.png
/usr/share/help/fi/cheese/figures/cheese-record.png
/usr/share/help/fi/cheese/figures/cheese-save.png
/usr/share/help/fi/cheese/figures/cheese-take.png
/usr/share/help/fi/cheese/figures/cheese.png
/usr/share/help/fi/cheese/figures/effects.png
/usr/share/help/fi/cheese/figures/image-properties.png
/usr/share/help/fi/cheese/figures/settings.png
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
/usr/share/help/fr/cheese/figures/cheese-delete.png
/usr/share/help/fr/cheese/figures/cheese-effects.png
/usr/share/help/fr/cheese/figures/cheese-introduction.png
/usr/share/help/fr/cheese/figures/cheese-record.png
/usr/share/help/fr/cheese/figures/cheese-save.png
/usr/share/help/fr/cheese/figures/cheese-take.png
/usr/share/help/fr/cheese/figures/cheese.png
/usr/share/help/fr/cheese/figures/effects.png
/usr/share/help/fr/cheese/figures/image-properties.png
/usr/share/help/fr/cheese/figures/settings.png
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
/usr/share/help/gl/cheese/figures/cheese-delete.png
/usr/share/help/gl/cheese/figures/cheese-effects.png
/usr/share/help/gl/cheese/figures/cheese-introduction.png
/usr/share/help/gl/cheese/figures/cheese-record.png
/usr/share/help/gl/cheese/figures/cheese-save.png
/usr/share/help/gl/cheese/figures/cheese-take.png
/usr/share/help/gl/cheese/figures/cheese.png
/usr/share/help/gl/cheese/figures/effects.png
/usr/share/help/gl/cheese/figures/image-properties.png
/usr/share/help/gl/cheese/figures/settings.png
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
/usr/share/help/hu/cheese/figures/cheese-delete.png
/usr/share/help/hu/cheese/figures/cheese-effects.png
/usr/share/help/hu/cheese/figures/cheese-introduction.png
/usr/share/help/hu/cheese/figures/cheese-record.png
/usr/share/help/hu/cheese/figures/cheese-save.png
/usr/share/help/hu/cheese/figures/cheese-take.png
/usr/share/help/hu/cheese/figures/cheese.png
/usr/share/help/hu/cheese/figures/effects.png
/usr/share/help/hu/cheese/figures/image-properties.png
/usr/share/help/hu/cheese/figures/settings.png
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
/usr/share/help/id/cheese/figures/cheese-delete.png
/usr/share/help/id/cheese/figures/cheese-effects.png
/usr/share/help/id/cheese/figures/cheese-introduction.png
/usr/share/help/id/cheese/figures/cheese-record.png
/usr/share/help/id/cheese/figures/cheese-save.png
/usr/share/help/id/cheese/figures/cheese-take.png
/usr/share/help/id/cheese/figures/cheese.png
/usr/share/help/id/cheese/figures/effects.png
/usr/share/help/id/cheese/figures/image-properties.png
/usr/share/help/id/cheese/figures/settings.png
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
/usr/share/help/ko/cheese/figures/cheese-delete.png
/usr/share/help/ko/cheese/figures/cheese-effects.png
/usr/share/help/ko/cheese/figures/cheese-introduction.png
/usr/share/help/ko/cheese/figures/cheese-record.png
/usr/share/help/ko/cheese/figures/cheese-save.png
/usr/share/help/ko/cheese/figures/cheese-take.png
/usr/share/help/ko/cheese/figures/cheese.png
/usr/share/help/ko/cheese/figures/effects.png
/usr/share/help/ko/cheese/figures/image-properties.png
/usr/share/help/ko/cheese/figures/settings.png
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
/usr/share/help/nl/cheese/figures/cheese-delete.png
/usr/share/help/nl/cheese/figures/cheese-effects.png
/usr/share/help/nl/cheese/figures/cheese-introduction.png
/usr/share/help/nl/cheese/figures/cheese-record.png
/usr/share/help/nl/cheese/figures/cheese-save.png
/usr/share/help/nl/cheese/figures/cheese-take.png
/usr/share/help/nl/cheese/figures/cheese.png
/usr/share/help/nl/cheese/figures/effects.png
/usr/share/help/nl/cheese/figures/image-properties.png
/usr/share/help/nl/cheese/figures/settings.png
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
/usr/share/help/pl/cheese/figures/cheese-delete.png
/usr/share/help/pl/cheese/figures/cheese-effects.png
/usr/share/help/pl/cheese/figures/cheese-introduction.png
/usr/share/help/pl/cheese/figures/cheese-record.png
/usr/share/help/pl/cheese/figures/cheese-save.png
/usr/share/help/pl/cheese/figures/cheese-take.png
/usr/share/help/pl/cheese/figures/cheese.png
/usr/share/help/pl/cheese/figures/effects.png
/usr/share/help/pl/cheese/figures/image-properties.png
/usr/share/help/pl/cheese/figures/settings.png
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
/usr/share/help/pt_BR/cheese/figures/cheese-delete.png
/usr/share/help/pt_BR/cheese/figures/cheese-effects.png
/usr/share/help/pt_BR/cheese/figures/cheese-introduction.png
/usr/share/help/pt_BR/cheese/figures/cheese-record.png
/usr/share/help/pt_BR/cheese/figures/cheese-save.png
/usr/share/help/pt_BR/cheese/figures/cheese-take.png
/usr/share/help/pt_BR/cheese/figures/cheese.png
/usr/share/help/pt_BR/cheese/figures/effects.png
/usr/share/help/pt_BR/cheese/figures/image-properties.png
/usr/share/help/pt_BR/cheese/figures/settings.png
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
/usr/share/help/ru/cheese/figures/cheese-delete.png
/usr/share/help/ru/cheese/figures/cheese-effects.png
/usr/share/help/ru/cheese/figures/cheese-introduction.png
/usr/share/help/ru/cheese/figures/cheese-record.png
/usr/share/help/ru/cheese/figures/cheese-save.png
/usr/share/help/ru/cheese/figures/cheese-take.png
/usr/share/help/ru/cheese/figures/cheese.png
/usr/share/help/ru/cheese/figures/effects.png
/usr/share/help/ru/cheese/figures/image-properties.png
/usr/share/help/ru/cheese/figures/settings.png
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
/usr/share/help/sl/cheese/figures/cheese-delete.png
/usr/share/help/sl/cheese/figures/cheese-effects.png
/usr/share/help/sl/cheese/figures/cheese-introduction.png
/usr/share/help/sl/cheese/figures/cheese-record.png
/usr/share/help/sl/cheese/figures/cheese-save.png
/usr/share/help/sl/cheese/figures/cheese-take.png
/usr/share/help/sl/cheese/figures/cheese.png
/usr/share/help/sl/cheese/figures/effects.png
/usr/share/help/sl/cheese/figures/image-properties.png
/usr/share/help/sl/cheese/figures/settings.png
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
/usr/share/help/sv/cheese/figures/cheese-delete.png
/usr/share/help/sv/cheese/figures/cheese-effects.png
/usr/share/help/sv/cheese/figures/cheese-introduction.png
/usr/share/help/sv/cheese/figures/cheese-record.png
/usr/share/help/sv/cheese/figures/cheese-save.png
/usr/share/help/sv/cheese/figures/cheese-take.png
/usr/share/help/sv/cheese/figures/cheese.png
/usr/share/help/sv/cheese/figures/effects.png
/usr/share/help/sv/cheese/figures/image-properties.png
/usr/share/help/sv/cheese/figures/settings.png
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
/usr/share/help/zh_CN/cheese/figures/cheese-delete.png
/usr/share/help/zh_CN/cheese/figures/cheese-effects.png
/usr/share/help/zh_CN/cheese/figures/cheese-introduction.png
/usr/share/help/zh_CN/cheese/figures/cheese-record.png
/usr/share/help/zh_CN/cheese/figures/cheese-save.png
/usr/share/help/zh_CN/cheese/figures/cheese-take.png
/usr/share/help/zh_CN/cheese/figures/cheese.png
/usr/share/help/zh_CN/cheese/figures/effects.png
/usr/share/help/zh_CN/cheese/figures/image-properties.png
/usr/share/help/zh_CN/cheese/figures/settings.png
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
/usr/lib64/libcheese-gtk.so.25.0.9
/usr/lib64/libcheese.so.8
/usr/lib64/libcheese.so.8.0.9

%files locales -f cheese.lang
%defattr(-,root,root,-)

