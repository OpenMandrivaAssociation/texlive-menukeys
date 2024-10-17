Name:		texlive-menukeys
Version:	64314
Release:	2
Summary:	Format menu sequences, paths and keystrokes from lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/menukeys
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/menukeys
%doc %{_texmfdistdir}/doc/latex/menukeys
#- source
%doc %{_texmfdistdir}/source/latex/menukeys

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
