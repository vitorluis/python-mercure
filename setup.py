# -*- coding: utf-8 -*-
from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'pymercure/README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pymercure',
    version='0.0.1.0',
    url='https://github.com/vitorluis/python-mercure',
    license='BSD',
    author='Vitor Villar',
    author_email='vitor.luis98@gmail.com',
    description='Mercure Python library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'grequests',
        'requests',
        'sseclient-py'
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
    py_modules=['pymercure'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
