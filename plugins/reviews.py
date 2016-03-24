import os
import sys
import fileinput
from shutil import copyfile

REVIEW_PATH = 'reviews/'
REVIEWS = {}

ORDER = -100


def preBuild(site):

    global REVIEWS

    review_path = os.path.join(site._path, site.config.get("review_path"))

    review_page_path = os.path.join(site.page_path, REVIEW_PATH)
    if not os.path.isdir(review_page_path):
        os.mkdir(review_page_path)

    if not review_path:
        raise "Must assign a review_path key in config"

    for file in os.listdir(review_path):
        if file.endswith(".txt") and file != 'template.txt':
            new_file = file.replace(".txt", ".html")
            old_full_path = os.path.join(review_path, file)
            new_full_path = os.path.join(review_page_path, new_file)
            copyfile(old_full_path, new_full_path)
            # Edit reivew files for templating
            for i, line in enumerate(fileinput.input(new_full_path, inplace=1)):
                if i == 5:
                    sys.stdout.write('{% extends "review.html" %}\n{% block review %}')
                elif i < 8 and line == "\n":
                    pass
                else:
                    sys.stdout.write(line)

            with open(new_full_path, "a") as myfile:
                myfile.write("{% endblock %}")

            context = {"path": os.path.join('/', REVIEW_PATH, new_file)}
            with open(old_full_path, 'r') as f:
                for line in f:
                    if line == "\n":
                        break
                    else:
                        try:
                            k, v = line.split(": ", 1)
                            context[k.lower()] = v.strip()
                        except ValueError:
                            print(file + " has error parsing line " + line)

            REVIEWS[new_file] = context


def sort_by_review(r):
    if 'reviewed' not in r:
        print("Review: " + str(r) + " is missing 'reviewed key'")
    return r['reviewed']


def preBuildPage(site, page, context, data):
    """
    Add the list of reviews to every page context so we can
    access them from wherever on the site.
    """
    if page.path == "reviews.html":
        context['reviews'] = sorted(REVIEWS.values(), key=sort_by_review, reverse=True)

    if page.path.startswith(REVIEW_PATH):
        r_path = page.path.split('/')[-1]
        if r_path in REVIEWS:
            context.update(REVIEWS[r_path])

    return context, data
