from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='fluiddb',
      version=version,
      description="Python FluidDB API",
      long_description="""\
== ABOUT ==""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='fluiddb database api',
      author='Igor Guerrero',
      author_email='igfgt1@gmail.com',
      url='http://www.igorgue.info/',
      license='Apache License Version 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
