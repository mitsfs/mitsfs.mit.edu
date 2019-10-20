
MINUTES = ["latest",
           "2019"]

ORDER = 10


def preBuildPage(site, page, context, data):
    if page.path == "minutes.html":
        context['minutes'] = MINUTES
    return context, data


import os


def postBuild(site):
    path = os.path.join(site.build_path, 'minutes/archive')
    os.symlink("/mit/mitsfs/www/minutes", path)
