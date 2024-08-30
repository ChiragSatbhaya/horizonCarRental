from setuptools import setup, find_packages

# Read the contents of your README file
with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="horizon_car_rental",
    version="1.0.0",
    author="Chirag Satbhaya",
    author_email="shahchi89@gmail.com",
    description="A car rental system for Horizon Car Rental.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/horizon_car_rental",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'horizon_car_rental=main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "mysql-connector-python",  # MySQL connector package
    ],
    include_package_data=True,
)
