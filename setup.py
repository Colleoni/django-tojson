from setuptools import setup

setup(
    name = "django-tojson",
    version = "0.3.5",
    description = open("README.md", 'r').read(),
    url = "https://github.com/davidek/django-tojson",
    author="Davide Kirchner, Roberto Bampi",
    author_email="",
    packages = [
        "tojson"
    ],
    classifiers = [
        'Programming Language :: Python3',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Indipendent',
        'Framework :: Django 2',
    ]
)

