from setuptools import find_packages, setup

setup(
    name="dummy",
    version="0.0.01",
    description="Just a dummy package",
    author="zishan",
    install_requires=["numpy", "pandas", "pytest"],
    packages=find_packages(),
)
