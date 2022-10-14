from setuptools import find_packages, setup

_NAME = 'inheritance_trial'
setup(
    name=_NAME,
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            '{0} = {0}.main:main'.format(_NAME),
        ]
    }
)
