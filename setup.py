from setuptools import setup, find_packages
setup(
    name = "Labrador",
    version = "0.2.0",
    packages = find_packages(),
    install_requires = [
        'pyyaml',
        'jprops',
        'requests'],
    author = "Elliot Block",
    author_email = "elliot@deck36.net",
    description = "Configuration retrieval",
    url = "https://github.com/elliot42/labrador",
    scripts = ['bin/lab']
)
