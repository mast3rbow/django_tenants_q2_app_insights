import os
from setuptools import setup

try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except ImportError:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
        README = readme.read()


setup(
    name='django-tenants-q2-appinsights',
    version='0.1.5',
    author='Bryton Wishart',
    author_email='mast3rbow@gmail.com',
    keywords='django distributed task queue worker scheduler with application insights logging',
    packages=['django_tenants_q2_appinsights'],
    install_requires=['opencensus>=0.11.3, opencensus-context>=0.1.3, opencensus-ext-azure>=1.1.10'],
    url='https://django-q.readthedocs.org',
    license='MIT',
    description='A Application support plugin for Django Q2',
    long_description=README,
)