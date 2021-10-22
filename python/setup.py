import setuptools
import os

with open('README.rst', 'r') as readme:
    long_description = readme.read()

with open('README.md', 'r') as readme_markdown:
    conda_description = readme_markdown.read()

setuptools.setup(
    name='h2o_nitro',
    version=os.getenv('VERSION', '0.1.0'),
    author='Prithvi Prabhu',
    author_email='prithvi@h2o.ai',
    description='Make Flutter Apps using Python',
    long_description=long_description,
    # conda_description is a hack to read Anaconda description from a file. Not needed for PyPI.
    conda_description=conda_description,
    url='https://h2o.ai/products/h2o-wave',
    packages=['h2o_nitro'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Communications :: Chat',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: System :: Distributed Computing',
    ],
    python_requires='>=3.6.1',
    install_requires=[
    ],
)
