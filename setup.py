"""Python setup script."""
from setuptools import setup

setup(
    name='tensor',
    version='0.0.1',
    description='Tensorflow Tests',
    packages=['tensor'],
    install_requires=[
        'argh',
        'setuptools',
        'requests',
        'toml',
        'crate',
        'tensorflow',
    ],
    entry_points={
        'console_scripts': [
            't = tensor.main:main',
        ]
    },
)
