from setuptools import setup


# Version of this package
MAJOR=0
MINOR=1
PATCH=0
devel=False

version = '{}.{}.{}'.format(MAJOR, MINOR, PATCH)
if devel:
    version += '.dev0'
with open('sphinx_docslab/_version.py', 'w') as fp:
    fp.write('''"""This file was automatically generated by setup.py. Do not edit.
"""
__version__ = '{}'
'''.format(version))


setup(version=version)
