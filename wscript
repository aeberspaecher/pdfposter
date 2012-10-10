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

    ctx.add_post_fun(post)  # copy PDF, possibly view also

    # add manual dependency such that the presentation is rebuilt if the style
    # package pdfposter.sty changes:
    ctx.add_manual_dependency(ctx.path.find_node('pdfposter.tex'), ctx.path.find_node('pdfposter.sty'))

def post(ctx):
    print("Copy PDF file to top directory")
    ctx.exec_command("cp {0}/pdfposter.pdf".format(out) + " {0}".format(top))
    if ctx.options.view:
        print("Open PDF file in default PDF viewer")
        ctx.exec_command("xdg-open {0}/pdfposter.pdf".format(out))

def options(ctx):
        ctx.add_option("--view", action="store_true", default=False,
                       help='view the PDf after it is built')
