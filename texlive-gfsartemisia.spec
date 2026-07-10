%global tl_name gfsartemisia
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A modern Greek font design
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsartemisia
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsartemisia.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsartemisia.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
GFS Artemisia is a relatively modern font, designed as a 'general
purpose' font in the same sense as Times is nowadays treated. The
present version has been provided by the Greek Font Society. The font
supports the Greek and Latin alphabets. LaTeX support is provided, using
the OT1, T1 and LGR encodings.

