# revision 33151
# category Package
# catalog-ctan /macros/latex/contrib/menukeys
# catalog-date 2014-03-10 08:48:40 +0100
# catalog-license lppl1.2
# catalog-version 1.3
Name:		texlive-menukeys
Version:	1.30
Release:	1
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
\path{macros/latex/contrib/menukeys} and short cuts such as
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
