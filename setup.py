import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='Druglord',
    version='0.1.2',
    author='Bruno Vaula Werneck',
    author_email='brunovaulawerneck@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brunowerneck/druglord',
    packages=setuptools.find_packages(),
    license='LICENSE.txt',
    install_requires=[
        'beautifulsoup4',
        'requests',
        'selenium'
    ]
)
