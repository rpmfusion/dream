Name:		dream
Version:	2.2
Release:	12%{?dist}
Summary:	A software radio for AM and Digital Radio Mondiale (DRM)
License:	GPLv2+
URL:		https://sourceforge.net/projects/drm/
Source0:	https://sourceforge.net/projects/drm/files/dream/%{version}/dream_%{version}.orig.tar.gz
Source1:	dream.desktop
Patch0:		dream-2.2-use-system-libs.patch

# https://sourceforge.net/p/drm/tickets/233/
Patch1:		dream-2.2-hamlib-4-fix.patch
# https://sourceforge.net/p/drm/tickets/234/
Patch2:		dream-2.2-gpsd-3.20-fix.patch
# https://sourceforge.net/p/drm/tickets/235/
Patch3:		dream-2.2-gpsd-3.23-fix.patch
Patch4:     dream-2.2-fix-qwttext.patch
BuildRequires:	gcc-c++
BuildRequires:	hamlib-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	libpcap-devel
BuildRequires:	gpsd-devel
BuildRequires:	libsndfile-devel
BuildRequires:	speexdsp-devel
BuildRequires:	fftw-devel
BuildRequires:	opus-devel
BuildRequires:	faad2-devel
BuildRequires:	qwt-qt5-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libpcap-devel
BuildRequires:	faac-devel > 1.29.9.2-3
# for future new release
#BuildRequires:	fdk-aac-free-devel
#BuildRequires:	SoapySDR-devel
Requires:	hicolor-icon-theme

%description
Dream is a software implementation of a Digital Radio Mondiale (DRM) receiver.
With Dream, DRM broadcasts can be received with a modified analog
receiver (SW, MW, LW) and a PC with a sound card.

%prep
%autosetup -p1 -n dream-%{version}

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
* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 2.2-12
- rebuilt

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 17 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-10
- Fixed FTBFS
  Resolves: rfbz#5697

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-6
- Fixed FTBFS
  Resolves: rfbz#5697

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Leigh Scott <leigh123linux@gmail.com> - 2.2-4
- Rebuilt

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
