import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Patient, Page

def populate():
    # First, we will create list of dictionaries containing the pages
    # we want to add into each patient.
    # The we will create a dictionary of dictionaries for our patients.
    # This might seem a little be confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title": "Official Python Tutorial",
         "note": "http://docs.python.org/2/tutorial/","views":256},
        {"title": "How to Think like a Computer Scientist",
         "note": "http://www.greenteapress.com/thinkpython/", "views":128},
        {"title": "Learn Python in 10 Minutes",
         "note": "http://www.korokithakis.net/tutorials/python/", "views":64}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "note": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/","views":32},
        {"title": "Django Rocks",
         "note": "http://www.djangorocks.com/","views":16},
        {"title": "How to Tango with Django",
         "note": "http://www.tangowithdjango.com/", "views":8}]

    other_pages = [
        {"title": "Bottle",
         "note": "http://bottlepy.org/docs/dev/", "views": 4},
        {"title": "Flask",
         "note": "http://flask.pocoo.org", "views": 2}]

    user_groups = [
        {"title": "ChiPy",
         "note": "http://www.chipy.org", "views": 512},
        {"title": "Chicago Pythonistas",
         "note": "http://www.meetup.com/ChicagoPythonistas/", "views": 1024}]

    cats = {"Tim Warners-Lee": {"pages": python_pages, "views": 128, "likes": 64},
            "Thomas Jenkins": {"pages": django_pages, "views": 64, "likes": 32},
            "Mathew Cobenian": {"pages": other_pages, "views": 32, "likes": 16},
            "Paul Maripadavil":{"pages": user_groups, "views": 16, "likes":8}}

    # If you want to add more catergories or pages
    # add them to the dictionaries above

    # The code below goes through the cats dictionary, then adds each patient,
    # and then adds all the associated pages for that patient
    # if your are using Python 2.x then use cats.iteritiems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly

    for cat, cat_data in cats.items():
        #c = add_cat(cat,views,likes)
        # Updated the population script to pass through the specific values for views and likes
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["note"], p["views"])

    #Print out the patients we have added
    for c in Patient.objects.all():
        for p in Page.objects.filter(patient=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, note, views=0):
    p = Page.objects.get_or_create(patient=cat, title=title)[0]
    p.note=note
    p.views=views
    p.save()
    return p

def add_cat(name,views,likes):
    c = Patient.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

#Start Execution here!
if __name__ == '__main__':
    print("Starting Rango Population script...")
    populate()