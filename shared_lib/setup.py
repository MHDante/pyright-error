from distutils.core import setup

setup(
    name="shared-lib",
    version="0.0.1",
    package_dir={"": "src"},
    packages=["shared_code"],
    install_requires=[
        "torch==1.7.1"
    ],
)