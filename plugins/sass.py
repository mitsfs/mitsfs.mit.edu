import os
import pipes


def preBuild(site):
    if site.config.get("debug"):
        options = "--debug-info"
    else:
        options = "-t compressed"
    os.system(
        'sass %s --update %s/scss:%s/css' % (options, pipes.quote(site.path), pipes.quote(site.paths['static']))
    )
