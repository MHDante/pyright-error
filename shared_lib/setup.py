from distutils.core import setup

setup(
    name="shared-lib",
    version="0.0.1",
    package_dir={"": "src"},
    packages=["shared_code"],
    install_requires=[
        "grpcio==1.35.0",
        "grpc-stubs==1.24.5",
    ],
)