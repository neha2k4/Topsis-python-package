from setuptools import setup, find_packages

setup(
    name="topsis-neha-102203358",  # Unique name for your package
    version="1.0.2",        # Initial version
    author="Neha",
    author_email="nehagarg2k4@gmail.com",
    description="A Python package to calculate TOPSIS rankings",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis-package",  # Update with your repository URL
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",
        ],
    },
)
