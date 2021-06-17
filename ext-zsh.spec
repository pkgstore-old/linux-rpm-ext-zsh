%global app                     zsh
%global d_conf                  %{_sysconfdir}/%{app}
%global release_prefix          100

Name:                           ext-zsh
Version:                        1.0.6
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure Zsh
License:                        MIT

Source10:                       %{app}rc.grml

Requires:                       zsh

%description
META-package for install and configure Zsh.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_conf}/%{app}rc.grml


%files
%config %{d_conf}/%{app}rc.grml


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.6-100
- UPD: Move to GitHub.
- UPD: License.
- UPD: "zshrc.grml".

* Thu Jun 25 2020 Package Store <pkgstore@pm.me> - 1.0.5-100
- NEW: v1.0.5.

* Mon Dec 02 2019 Package Store <pkgstore@pm.me> - 1.0.4-100
- NEW: v1.0.4.

* Mon Nov 18 2019 Package Store <pkgstore@pm.me> - 1.0.3-100
- NEW: v1.0.3.
- UPD: zshrc file.

* Mon Nov 11 2019 Package Store <pkgstore@pm.me> - 1.0.2-100
- NEW: v1.0.2.
- UPD: zshrc file.

* Thu Oct 10 2019 Package Store <pkgstore@pm.me> - 1.0.1-100
- NEW: v1.0.1.
- UPD: zshrc file.

* Thu Jul 18 2019 Package Store <pkgstore@pm.me> - 1.0.0-100
- Initial build.
