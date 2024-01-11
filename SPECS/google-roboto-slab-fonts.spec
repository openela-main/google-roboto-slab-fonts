%global commit0 90abd17b4f97671435798b6147b698aa9087612f

Version:       1.100263
Release:       0.17.20150923git%{?dist}
URL:           https://www.google.com/fonts/specimen/Roboto+Slab

%global foundry           google
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE.txt

%global fontfamily        Roboto Slab
%global fontsummary       Google Roboto Slab fonts
%global fonts             *.ttf
%global fontconfs         %{SOURCE5}
%global fontdescription   %{expand:
Roboto has a dual nature. It has a mechanical skeleton and the forms are
largely geometric. At the same time, the font features friendly and open
curves. While some grotesks distort their letterforms to force a rigid
rhythm, Roboto doesn't compromise, allowing letters to be settled into
their natural width. This makes for a more natural reading rhythm more
commonly found in humanist and serif types.

This is the Roboto Slab family, which can be used alongside the normal
Roboto family and the Roboto Condensed family.}

# There are no tar archive so let's pick all the individual source files from github
Source0:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Regular.ttf
Source1:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Bold.ttf
Source2:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Light.ttf
Source3:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/RobotoSlab-Thin.ttf
Source4:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotoslab/LICENSE.txt
Source5:       64-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com>
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com>
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.15.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.14.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.13.20150923git
- Update fontconfig DTD id in conf file

* Thu Mar 12 2020 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.12.20150923git
- Convert to new fonts packaging guidelines

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.11.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.10.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.9.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.8.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.7.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.6.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.5.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.100263-0.4.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.3.20150923git
- Follow https://fedoraproject.org/wiki/Packaging:SourceURL#Commit_Revision

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.2.20150923
- Fix metainfo file validation by adding <p> </p>
- use %%license macro

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.100263-0.1.20150923
- Initial package
