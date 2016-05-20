import os
from cactus.page import Page
from cactus.static import Static


# Make cactus build .htaccess files

def postBuild(site):

    for root, dirs, files in os.walk(site.page_path, topdown=False):
        for name in files:
            if name == '.htaccess':
                full_path = os.path.join(root, name)
                path = os.path.relpath(full_path, site.page_path)
                page = Page(site, path)
                page.build()

    for root, dirs, files in os.walk(site.static_path, topdown=False):
        for name in files:
            if name == '.htaccess':
                full_path = os.path.join(root, name)
                path = os.path.relpath(full_path, site.static_path)
                static = Static(site, path)
                static.build()
