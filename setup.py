# Import required functions
from setuptools import setup, find_packages

# pip install -e .           ---->        to install the package

# Call setup function
setup(
    author="Allison Eduardo",
    description="Data Base",
    name="db",
    version="0.1.0",
    packages=find_packages(include=["db", "db.*"]),
    install_requires=["sqlite3"]
)
