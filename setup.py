import setuptools
from druglord.__pkginfo__ import info

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name=info['name'],
    version=info['version'],
    author=info['author'],
    author_email=info['email'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=info['uri'],
    packages=['druglord'],
    include_package_data=True,
    license=info['license'],
    classifiers=info['classifiers'],
    install_requires=[
        'beautifulsoup4',
        'requests',
        'selenium'
    ]
)
