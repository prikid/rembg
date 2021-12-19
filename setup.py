import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

with open("requirements.txt") as f:
    requireds = f.read().splitlines()

setup(
    name="kyrptl_api_rembg",
    version="1.0.28",
    description="Remove image background",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielgatis/rembg",
    author="Daniel Gatis",
    author_email="danielgatis@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="remove, background, u2net",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=requireds,
    entry_points={
        "console_scripts": [
            "kyrptl_api_rembg=kyrptl_api_rembg.cmd.cli:main",
            "kyrptl_api_rembg-server=kyrptl_api_rembg.cmd.server:main",
        ],
    },
)
