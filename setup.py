#!/usr/bin/env python
from setuptools import setup, find_packages

version = __import__('mailchimp').__version__

setup(
    name = 'django-mailchimp',
    version = version,
    description = 'Mailchimp wrapper for Django, using Mailchimp API 1.3',
    author = 'Jonas Obrist et al.',
    url = 'http://github.com/divio/django-mailchimp',
    packages = find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>=2.2,<4.0',
        'requests~=2.0',
    ],
    package_data={
        'mailchimp': [
            'templates/mailchimp/*.html',
            'locale/*/LC_MESSAGES/*',
        ],
    },
)
