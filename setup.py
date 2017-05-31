from setuptools import setup

setup(
    name='fidelity',
    version='0.1',
    description='Library for transcribing Tigrinya in ASCII',
    url='http://github.com/morrisalp/fidelity',
    author='Morris Alper',
    author_email='morrisalp@gmail.com',
    license='GPL-3.0',
    packages=['fidelity'],
    test_suite='nose.collector',
    tests_require=['nose']
)