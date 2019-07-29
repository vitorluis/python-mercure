# -*- coding: utf-8 -*-
"""
pymercure is a library to interact with Mercure pub/sub service
Usage
-----
import json

from publisher.sync import SyncPublisher

a = json.dumps({'status': 'Working from Python async'})
p = SyncPublisher(
    'http://localhost:3000/hub',
    'your.Token.Here'
)
print(p.publish(['mytopicname'], a))
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
