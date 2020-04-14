# it seems upstream released tarballs have svn suffix even for stable versions
%global ver_suffix svn808

Name:		dream
Version:	2.2
Release:	3%{?dist}
Summary:	A software radio for AM and Digital Radio Mondiale (DRM)
License:	GPLv2+
URL:		https://sourceforge.net/projects/drm/
Source0:	https://sourceforge.net/projects/drm/files/dream/%{version}/dream_%{version}.orig.tar.gz
Source1:	dream.desktop
Patch0:		dream-2.2-use-system-libs.patch
Patch1:		dream-2.2-hamlib-4-fix.patch
BuildRequires:	gcc-c++, hamlib-devel, dos2unix, pulseaudio-libs-devel
BuildRequires:	libpcap-devel, gpsd-devel, libsndfile-devel, speexdsp-devel, fftw-devel
BuildRequires:	opus-devel, faad2-devel, qwt-qt5-devel, qt5-qtwebkit-devel
BuildRequires:	desktop-file-utils, libpcap-devel
BuildRequires:	faac-devel > 1.29.9.2-3
Requires:	hicolor-icon-theme

%description
Dream is a software implementation of a Digital Radio Mondiale (DRM) receiver.
With Dream, DRM broadcasts can be received with a modified analog
receiver (SW, MW, LW) and a PC with a sound card.

%prep
%autosetup -p1 -n dream-%{version}

# convert CRLF to LF
dos2unix dream.pro

%build
OUT_PWD="%{_prefix}" %{qmake_qt5} ./dream.pro
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

# icon
install -Dpm 0644 src/GUI-QT/res/MainIcon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/dream.svg

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{S:1}

%files
%license COPYING
%doc AUTHORS README NEWS TODO ChangeLog
%{_bindir}/dream
%{_datadir}/icons/hicolor/scalable/apps/dream.svg
%{_datadir}/applications/dream.desktop
%{_mandir}/man1/*

%changelog
* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-3
- Dropped unneeded qt5-devel build requires
- Fixed build with hamlib-4
- Rebuilt with hamlib-4

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.2-1
- Release 2.2

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-5
- Built with qwt-qt5

* Wed Oct 24 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-4
- Added minimal version to build require for faac (DRM enabled version)

* Wed Oct 24 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-3
- Built with libpcap

* Tue Oct 23 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-2
- Enabled faac DRM
- Built with Qt5

* Sat Oct  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-1
- Initial version
