# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-text
# catalog-date 2007-03-11 16:56:01 +0100
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-pst-text
Version:	1.00
Release:	8
Summary:	Text and character manipulation in PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-text
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-text.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-text.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-text.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-text is a PSTricks based package for plotting text along a
different path and manipulating characters. It includes the
functionality of the old package pst-char.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-text/pst-text.pro
%{_texmfdistdir}/tex/generic/pst-text/pst-char.tex
%{_texmfdistdir}/tex/generic/pst-text/pst-text.tex
%{_texmfdistdir}/tex/latex/pst-text/pst-char.sty
%{_texmfdistdir}/tex/latex/pst-text/pst-text.sty
%doc %{_texmfdistdir}/doc/generic/pst-text/Changes
%doc %{_texmfdistdir}/doc/generic/pst-text/README
%doc %{_texmfdistdir}/doc/generic/pst-text/pst-text-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-text/pst-text-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-text/pst-text-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-text/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 755483
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 719401
- texlive-pst-text
- texlive-pst-text
- texlive-pst-text
- texlive-pst-text

