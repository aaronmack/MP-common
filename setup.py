import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mp-common-pkg", # Replace with your own username
    version="0.0.1",
    author="Aaron Li",
    author_email="lilong999000@gmail.com",
    description="A common repository, for MP System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aaronmack/MP-common",
    packages=["common_pkg"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)