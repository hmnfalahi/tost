from setuptools import setup, find_packages


dependencies = [
    'gunicorn',
]


setup(
    name='tost',
    version=0,
    packages=find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tost = tost:tost.cli_main'
        ]
    }
)

