import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SchemaToTypedDict",
    version="0.0.1",
    author="Riley Flynn",
    author_email="riley@rileyflynn.me",
    description="JSON Schema to TypedDict converter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nint8835/SchemaToTypedDict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "schematotypeddict=SchemaToTypedDict.__main__:convert"
        ]
    }
)
