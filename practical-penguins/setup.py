import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trivia_tavern",
    version="0.0.1",
    author="Practical-penguins",
    author_email="kkawabat@asu.edu",
    description="django web application for trivia creation/organization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkawabat/summer-code-jam-2020/tree/master/practical-penguins",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)