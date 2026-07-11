%global tl_name menukeys
%global tl_revision 79013

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6.3
Release:	%{tl_revision}.1
Summary:	Format menu sequences, paths and keystrokes from lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/menukeys
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/menukeys.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is designed to format menu sequences, paths and keyboard
shortcuts automatically. There are several predefined styles and one can
define one's own styles in a flexible way.

