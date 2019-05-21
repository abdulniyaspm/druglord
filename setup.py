import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='Druglord',
    version='0.1.4',
    author='Bruno Vaula Werneck',
    author_email='brunovaulawerneck@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brunowerneck/druglord',
    packages=['druglord'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[
        'beautifulsoup4',
        'requests',
        'selenium'
    ]
)
