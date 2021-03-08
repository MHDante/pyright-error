from distutils.core import setup

setup(
    name="shared-lib",
    version="0.0.1",
    package_dir={"": "src"},
    packages=["shared_code", "stubbed_code"],
    install_requires=[
        "grpcio==1.35.0",
        "grpc-stubs==1.24.5",
        "protobuf==3.14.0",
        "torch==1.7.1"
    ],
)