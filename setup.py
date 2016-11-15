import sys
import os
from distutils.core import setup

setup(name = "createsend",
      version = '1.0.1',
      description = "A library which implements the complete functionality of the Campaign Monitor API.",
      author = "James Dennes",
      author_email = 'jdennes@gmail.com',
      url = "http://campaignmonitor.github.io/createsend-python/",
      license = "MIT",
      keywords = "createsend campaign monitor email",
      packages = ['createsend'],
      package_data = {'createsend': ['cacert.pem']})
