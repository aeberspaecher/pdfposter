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
3. Compile with ``pdflatex pdfposter.tex``.

There are some comments in the files that will help you while you're editing.
