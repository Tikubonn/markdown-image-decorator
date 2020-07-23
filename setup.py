
from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as stream:
  long_description = stream.read()

setup(
  name="markdown_image_decorator",
  description="this is a extension package for markdown. decorate <img> tag with <a> and <figure> tag if necessary.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  version="1.0.0",
  license="MIT",
  author="tikubonn",
  author_email="https://twitter.com/tikubonn",
  url="https://github.com/tikubonn/markdown-image-decorator",
  py_modules=(
    "markdown_image_decorator",
  ),
  install_requires=(
    "markdown>=3.0",
  ),
  tests_require=(
    "bs4==0.0.1"
  ),
  classifiers=(
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT License",
  ),
)
