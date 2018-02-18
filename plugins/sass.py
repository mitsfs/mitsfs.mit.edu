import subprocess
import pipes


def preBuild(site):
    if site.config.get("debug"):
        options = ["--debug-info"]
    else:
        options = ["-t", "compressed"]
    subprocess.check_call(['sass'] +
                          options +
                          ['--update',
                           '%s/scss:%s/css' % (pipes.quote(site.path), pipes.quote(site.paths['static']))
    ])
