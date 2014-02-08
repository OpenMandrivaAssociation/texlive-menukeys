# revision 25919
# category Package
# catalog-ctan /macros/latex/contrib/menukeys
# catalog-date 2012-04-11 11:11:10 +0200
# catalog-license lppl1.2
# catalog-version 1.1b
Name:		texlive-menukeys
Version:	1.1b
Release:	2
Summary:	Format menu sequences, paths and keystrokes from lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/menukeys
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows easy input and formatting of menu sequences,
using menus set with commands such as \menu{Extras > Settings >
General}, paths using a command like
\path{macros/latex/contrib/menukeys} and short cuts such aas
\keys{\ctrl + C}. The output is highly configurable by
providing different styles and colour themes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/menukeys/menukeys.sty
%doc %{_texmfdistdir}/doc/latex/menukeys/README
%doc %{_texmfdistdir}/doc/latex/menukeys/menukeys.pdf
#- source
%doc %{_texmfdistdir}/source/latex/menukeys/menukeys.dtx
%doc %{_texmfdistdir}/source/latex/menukeys/menukeys.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-1
+ Revision: 804940
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 790682
- Update to latest release.

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 783052
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 780495
- Import texlive-menukeys
- Import texlive-menukeys

