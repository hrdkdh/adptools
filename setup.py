import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="adptools",
    version="0.0.1.7",
    author="duhwan kim",
    author_email="hrdkdh@naver.com",
    description="A package for ADP license. It contains PCA(Scree plot etc.) and Variable Selection tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrdkdh/adptools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)