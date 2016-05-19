import codecs
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "django-simple-serializer"

DESCRIPTION = "provide layered url router for tornado"

LONG_DESCRIPTION = read("README.rst")

KEYWORDS = "tornado layered router"

AUTHOR = "RaPoSpectre"

AUTHOR_EMAIL = "rapospectre@gmail.com"

URL = "https://github.com/bluedazzle/tornado-layered-router"

VERSION = "0.0.1"

LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=[
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    py_modules=['tornado_router'],
    include_package_data=True,
    zip_safe=True,
)
