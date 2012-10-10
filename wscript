#!/usr/bin/env python

top = '.'
out = "build"

def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal("Could not find pdflatex")

def build(ctx):
    ctx(
            features = 'tex',
            type     = 'pdflatex', # pdflatex or xelatex
            source   = 'pdfposter.tex', # mandatory, the source
            outs     = 'pdf', # 'pdf' or 'ps pdf'
            prompt   = 0, # 0 for the batch mode
        )

    # add manual dependency such that the presentation is rebuilt if the style
    # package pdfposter.sty changes:
    ctx.add_manual_dependency(ctx.path.find_node('pdfposter.tex'), ctx.path.find_node('pdfposter.sty'))

    if ctx.cmd == 'build':
        if ctx.options.view:
            ctx.exec_command("xdg-open {0}/pdfposter.pdf".format(out))

def options(ctx):
        ctx.add_option("--view", action="store_true", default=False,
                       help='view the PDf after it is built')
