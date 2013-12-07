# revision 19469
# category Package
# catalog-ctan /fonts/greek/gfs/gfsartemisia
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-gfsartemisia
Version:	1.0
Release:	6
Summary:	A modern Greek font design
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsartemisia
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsartemisia.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsartemisia.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
GFS Artemisia is a relatively modern font, designed as a
'general purpose' font in the same sense as Times is nowadays
treated. The present version has been provided by the Greek
Font Society. The font supports the Greek and Latin alphabets.
LaTeX support is provided, using the OT1, T1 and LGR encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisia.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiadenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiaec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiaecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiael.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiaelsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiamath.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisianumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiasc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiatabnums.enc
%{_texmfdistdir}/fonts/map/dvips/gfsartemisia/gfsartemisia.map
%{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisia.otf
%{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisiaBold.otf
%{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisiaBoldIt.otf
%{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisiaIt.otf
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiadenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiadenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiamath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiamath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisianumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisianumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiatabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiatabnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiab6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiab6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabo6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiai6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiai6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiao6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiao6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiarg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiarg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasco6r.tfm
%{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiab8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiab9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiadenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiai8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiai9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiamath8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisianumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiao8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiao9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiarg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiarg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiatabnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiab6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiabi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiabo6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiai6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiao6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiarg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiasc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiasco6a.vf
%{_texmfdistdir}/tex/latex/gfsartemisia/gfsartemisia-euler.sty
%{_texmfdistdir}/tex/latex/gfsartemisia/gfsartemisia.sty
%{_texmfdistdir}/tex/latex/gfsartemisia/lgrartemisia.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/lgrartemisiaeuler.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/ot1artemisia.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/ot1artemisiaeuler.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/t1artemisia.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/t1artemisiaeuler.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/uartemisiaeulernums.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/uartemisianums.fd
%doc %{_texmfdistdir}/doc/fonts/gfsartemisia/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfsartemisia/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfsartemisia/README
%doc %{_texmfdistdir}/doc/fonts/gfsartemisia/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/gfsartemisia/gfsartemisia.pdf
%doc %{_texmfdistdir}/doc/fonts/gfsartemisia/gfsartemisia.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752266
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718543
- texlive-gfsartemisia
- texlive-gfsartemisia
- texlive-gfsartemisia
- texlive-gfsartemisia

