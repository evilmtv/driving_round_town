##############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from setuptools import setup
# from pycreate2.version import __version__ as VERSION
from build_utils import get_pkg_version
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution

VERSION = get_pkg_version('pycreate2/__init__.py')
PACKAGE_NAME = 'pycreate2'
BuildCommand.pkg = PACKAGE_NAME
BuildCommand.py2 = False
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION


setup(
    author='Kevin Walchko',
    author_email='walchko@users.noreply.github.com',
    name=PACKAGE_NAME,
    version=VERSION,
    description='A library to control iRobot Create 2 with python',
    long_description=open('README.rst').read(),
    url='http://github.com/walchko/{}'.format(PACKAGE_NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    license='MIT',
    keywords=['irobot', 'create 2', 'api', 'framework', 'library', 'robotics', 'robot', 'smart'],
    packages=[PACKAGE_NAME],
    # install_requires=open('requirements.txt').readlines(),
    install_requirements=[
        'pyserial',
        'simplejson',
        'build_utils'
    ]
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand
    },
    scripts=[
        'bin/create_reset.py',
        'bin/create_shutdown.py',
        'bin/create_monitor.py'
    ]
)
