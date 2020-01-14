"""
Flask-Bundler
-------------

Flask-Bundler allows you to serve your project assets from Webpack directly,
allowing cache busting and easy deployment.

It uses Webpack's BundleTracker plugin to get information about the bundles
in your configuration and to serve them.
"""
from setuptools import setup


setup(
    name='Flask-Bundler',
    version='1.0',
    url='http://github.com/emdemir/flask-sqlite3/',
    license='BSD',
    author='Efe Mert Demir',
    author_email='efemertdemir@hotmail.com',
    description='Flask extension to serve Webpack bundles',
    long_description=__doc__,
    packages=['flask_bundler'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
