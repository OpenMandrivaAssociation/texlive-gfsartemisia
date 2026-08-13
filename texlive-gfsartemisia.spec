%global tl_name gfsartemisia
%global tl_revision 79618
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A modern Greek font design
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsartemisia
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsartemisia.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsartemisia.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
GFS Artemisia is a relatively modern font, designed as a 'general
purpose' font in the same sense as Times is nowadays treated. The
present version has been provided by the Greek Font Society. The font
supports the Greek and Latin alphabets. LaTeX support is provided, using
the OT1, T1 and LGR encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from gfsartemisia:
Map gfsartemisia.map
TL_DROPIN_EOF
