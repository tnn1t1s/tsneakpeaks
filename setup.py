# setup.py
from setuptools import setup, find_packages

setup(
    name="tsneakpeaks",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "scikit-learn>=1.0.0",
        "plotly>=5.0.0",
        "pillow>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "tsneakpeaks=tsneakpeaks.cli.cooper:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Lynchian journey through high-dimensional image spaces",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tsneakpeaks",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
