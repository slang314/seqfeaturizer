
from setuptools import setup, find_packages

setup(
    name='seqfeaturizer',
    version='0.2.1',
    description='CLI tool to extract and filter interpretable features from biological sequences',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pandas', 'plotly'],
    entry_points={
        'console_scripts': ['seqfeat=seqfeaturizer.cli:main'],
    },
    python_requires='>=3.7',
)
