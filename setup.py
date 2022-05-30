from setuptools import find_packages, setup

from netbox_icinga.version import VERSION

setup(
    name="netbox-icinga",
    version=VERSION,
    author="Izabela1337 forked from Hudson River Trading LLC",
    author_email="facjat8@gmail.com",
    description="Netbox Plugin to show icinga device state in Netbox.",
    url="https://github.com/izabela1337/netbox-icinga/",
    license="New BSD",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
