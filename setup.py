import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oscli",
    version="0.0.1",
    author="Krzysztof Ś",
    author_email="papierukartka@gmail.com",
    description="OpenSubtitles CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/papierukartka/oscli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/oscli'],
    python_requires='>=3.6',
    # TODO: install_requires
)
