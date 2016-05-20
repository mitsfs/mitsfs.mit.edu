
MINUTES = ["latest", "2016", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1992"]

ORDER = 10


def preBuildPage(site, page, context, data):
    if page.path == "minutes.html":
        context['minutes'] = MINUTES
    return context, data


import os


def postBuild(site):
    path = os.path.join(site.build_path, 'minutes/archive')
    os.symlink("/mit/mitsfs/www/minutes", path)
