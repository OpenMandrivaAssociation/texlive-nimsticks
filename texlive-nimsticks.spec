%global tl_name nimsticks
%global tl_revision 64118

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.1
Release:	%{tl_revision}.1
Summary:	Draws sticks for games of multi-pile Nim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/nimsticks
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nimsticks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nimsticks.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nimsticks.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides commands \drawnimstick to draw a single nim
stick and \nimgame which represents games of multi-pile Nim. Nim sticks
are drawn with a little random wobble so they look 'thrown together' and
not too regular. The package also provides options to customise the size
and colour of the sticks, and flexibility to draw heaps of different
objects.

