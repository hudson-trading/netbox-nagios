from setuptools import find_packages, setup

from netbox_icinga.version import VERSION

setup(
    name="netbox-icinga",
    version=VERSION,
    author="Hudson River Trading LLC",
    author_email="opensource@hudson-trading.com",
    description="Netbox Plugin to show icinga device state in Netbox.",
    url="https://github.com/hudson-trading/netbox_icinga/",
    license="New BSD",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
