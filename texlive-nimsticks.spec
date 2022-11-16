Name:		texlive-nimsticks
Version:	64118
Release:	1
Summary:	Draws sticks for games of multi-pile Nim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nimsticks
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nimsticks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nimsticks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nimsticks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides commands \drawnimstick to draw a
single nim stick and \nimgame which represents games of
multi-pile Nim. Nim sticks are drawn with a little random
wobble so they look 'thrown together' and not too regular. The
package also provides options to customise the size and colour
of the sticks, and flexibility to draw heaps of different
objects.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nimsticks
%{_texmfdistdir}/tex/latex/nimsticks
%doc %{_texmfdistdir}/doc/latex/nimsticks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
