import os
import pipes

def preBuild(site):
    os.system(
        'sass -t compressed --update %s/scss:%s/css' % (pipes.quote(site.path), pipes.quote(site.paths['static']))
    )
