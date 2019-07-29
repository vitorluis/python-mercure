# -*- coding: utf-8 -*-
"""
pymercure is a library to interact with Mercure pub/sub service
Usage
-----
Usage is simple::
    import grequests
    urls = [
        'http://www.heroku.com',
        'http://tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com'
    ]
Create a set of unsent Requests::
    >>> rs = (grequests.get(u) for u in urls)
Send them all at the same time::
    >>> grequests.map(rs)
    [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]
"""

from setuptools import setup

setup(
    name='pymercure',
    version='0.0.1',
    url='https://github.com/vitorluis/python-mercure',
    license='BSD',
    author='Vitor Villar',
    author_email='vitor.luis98@gmail.com',
    description='Mercure Python library',
    long_description=__doc__,
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
