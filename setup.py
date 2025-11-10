from setuptools import setup, find_packages

setup(
    name="bitloom",
    version="0.0.1",
    author="Mohamed Ali",
    author_email="mmdali008@gmail.com",
    description="Weaving code insights into exportable reports.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mhmd4li/bitloom",
    packages=find_packages(),
    python_requires=">=3.8",
)
