import setuptools

with open("README.md ", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samaker",
    version="1.0.0",
    author="wenbin Shi",
    author_email="shiwenbin1617@gmail.com",
    description="A TestCase maker package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
