# -*- coding: utf-8 -*-
"""Installer for the uwosh.oie.studyabroadtheme package."""

from setuptools import find_packages, setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='uwosh.oie.studyabroadtheme',
    version='1.1.10.dev0',
    description="Plone theme for UW Oshkosh Office of International Education",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Wildcard Corp.',
    author_email='corporate@wildcardcorp.com',
    url='https://pypi.python.org/pypi/uwosh.oie.studyabroadtheme',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['uwosh', 'uwosh.oie'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'Products.GenericSetup',
        'setuptools',
        'z3c.jbot',
        'plone.app.theming',
        'plone.app.themingplugins',
    ],
    extras_require={
        'test': [
            'collective.xmltestreport',
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    setup_requires=[
        'flake8',
        'isort',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
