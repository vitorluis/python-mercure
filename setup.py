# -*- coding: utf-8 -*-
"""
https://github.com/vitorluis/python-mercure
"""

from setuptools import setup, find_packages

setup(
    name='pymercure',
    version='0.0.1.0',
    url='https://github.com/vitorluis/python-mercure',
    license='BSD',
    author='Vitor Villar',
    author_email='vitor.luis98@gmail.com',
    description='Python Mercure library',
    long_description=__doc__,
    long_description_content_type='text/plain',
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
