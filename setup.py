from setuptools import setup, find_packages
setup(
    name = "Labrador",
    version = "0.5.0",
    packages = find_packages(),
    install_requires = [
        'pyyaml',
        'jprops',
        'requests'],
    author = "Elliot Block",
    author_email = "elliot@framed.io",
    description = "Configuration retrieval",
    url = "https://github.com/framed-data/labrador",
    scripts = ['bin/lab']
)
