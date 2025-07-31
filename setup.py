from setuptools import find_packages, setup
setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Vinay Ninave',
    author_email='vinayninave.cse23@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
)
