from __future__ import absolute_import
from distutils.core import setup

setup(
    name='Bayesian',
    version='2018-02-28.2',
    author='Neville Newey',
    author_email='nn@theneweys.org',
    packages=['bayesian', 'bayesian.test', 'bayesian.examples',
              'bayesian.examples.bbns',
              'bayesian.examples.factor_graphs'],
    license='LICENSE.txt',
    description='Bayesian Inference Engine using Factor Graphs.',
    long_description=open('README.txt').read(),
    install_requires=[],
)
