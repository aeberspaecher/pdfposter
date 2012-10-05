Poster template
===============

About
-----

Poster template is a LaTeX template for creating A0 size posters
specifically for scientific conferences. It is designed to work with
pdftex/pdflatex. For this reason, it uses TikZ instead of pstricks.

This template depends on the document class a0poster. A0poster is available
from http://www.ctan.org/tex-archive/macros/latex/contrib/a0poster/.

For a preview, use this direct link:
https://github.com/aeberspaecher/pdfposter/blob/master/pdfposter.pdf?raw=true

Features
--------

- boxes in different colors
- blocks for emphasizing
- customizable:
    - numbers of columns
    - colors
    - ...

How to use
----------

1. Add authors, conference and poster title in ``pdfposter.tex``.
2. Add your poster's contents to ``content.tex``.
3. Configure the ``waf`` build system with ``./waf configure``.
4. Compile with ``./waf build``.

There are some comments in the files that will help you while you're editing.

You can remove all files created by the build with ``./waf distclean``. The
build is removed by ``./waf clean``.

For convenience, ``./waf build --view`` opens the poster in your standard
PDF viewer after it is built.

Known problems
--------------

In case you get an error message such as "! No room for a new \count", add the
following lines to ``pdfposter.tex``::

  \usepackage{etex}
  \reserveinserts{20}

The author needs these lines with TeXlive (http://www.tug.org/texlive/) 2011.
