import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    # 首先创建一些字典， 列出想添加到各分类的网页
    # 然后创建一个嵌套字典, 设置各分类
    # 这么做看起来不易理解, 但是便于迭代, 方便为模型添加数据
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
         "url": "http://www.greeteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
    ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # 打印添加的分类
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_view_likes(views_num, likes_nums):
    for name in ("Python", "Django", "Other Frameworks"):
        c = Category.objects.get(name=name)
        c.view = views_num
        c.likes = likes_nums
        c.save()


def add_pages_views():
    pages = Page.objects.all()
    for page in pages:
        views_num = random.randint(5, 100)
        page.views = views_num
        page.save()


if __name__ == '__main__':
    # print("Starting Rango population script...")
    # populate()
    # a = [(128, 64), (64, 32), (32, 16)]
    # for m, n in a:
    #     add_view_likes(m, n)
    #     user_id = id

    add_pages_views()
