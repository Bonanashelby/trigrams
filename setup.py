"""This is our setup for trigrams exercise."""

from setuptools import setup


dependencies = ['ipython']
extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov']
}


setup(
    name='trigrams',
    description='Implements trigrams on any text/texts',
    version='0.1.0',
    authors='Anna, Morgan',
    author_email='bonanashelby@gmail.com',
    license='MIT',
    py_modules=['trigrams', 'test_trigrams'],
    package_dir={' ': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
            'trigrams = trigrams:main'
        ]
    }
)
