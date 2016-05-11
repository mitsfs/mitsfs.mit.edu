import os
from shutil import copyfile

JS_FILES = {"calendar_js": {"src": "static/scheduler/calendar.js",
            "dest": [
                "scheduler/ical.js",
                "scheduler/dhtmlxscheduler.js",
                "scheduler/dhtmlxscheduler_multisource.js",
                "scheduler/dhtmlxscheduler_recurring.js",
                "scheduler/dhtmlxscheduler_ical.js",
                "scheduler/dhtmlxscheduler_tooltip.js",
                "scheduler/dhtmlxscheduler_mitsfs.js", ]}}

JS_ASSETS = {}


def preBuild(site):
    global JS_ASSETS
    js_root = os.path.join(site._path, "js")
    for name, d in JS_FILES.items():
        JS_ASSETS[name] = []
        if site.config.get("debug"):
            for file in d["dest"]:
                static_js_path = os.path.join("static", file)
                copyfile(os.path.join(js_root, file), os.path.join(site._path, static_js_path))
                JS_ASSETS[name].append(os.path.join('/', static_js_path))
        else:
            with open(os.path.join(site._path, d["src"]), "w") as f:
                JS_ASSETS[name].append(os.path.join('/', d["src"]))
                for file in d["dest"]:
                    with open(os.path.join(js_root, file), "r") as old:
                        f.write(old.read())


def preBuildPage(site, page, context, data):
    if page.path in ['hours.html', 'keyholders/door-schedule/week.html']:
        context['js_assets'] = JS_ASSETS

    return context, data
