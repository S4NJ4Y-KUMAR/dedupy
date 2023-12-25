from setuptools import setup, find_packages

setup(
    name='dedupy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'argparse'
    ],
    entry_points={
        'console_scripts': [
            'dedupy = dedupy.tool:main',  # This points to your main function
        ],
    },
)   