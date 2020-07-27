from setuptools import find_packages, setup

from netbox_nagios.version import VERSION

setup(
    name="netbox-nagios",
    version=VERSION,
    author="Hudson River Trading LLC",
    author_email="opensource@hudson-trading.com",
    description="Netbox Plugin to show Nagios device state in Netbox.",
    url="https://github.com/hudson-trading/netbox_nagios/",
    license="New BSD",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
