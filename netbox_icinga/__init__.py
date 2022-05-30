try:
    from extras.plugins import PluginConfig
except ImportError:
    # Dummy so install of wheel works without Netbox.
    class PluginConfig:
        pass


from .version import VERSION


class NetboxIcingaConfig(PluginConfig):
    """
    This class defines attributes for the NetBox icinga plugin.
    """

    # Plugin package name
    name = "netbox_icinga"

    # Human-friendly name and description
    verbose_name = "icinga"
    description = "Plugin to show Icinga status in Netbox"

    # Plugin version
    version = VERSION

    # Plugin author
    author = "Izabela1337 forked from hudson-trading/netbox-icinga"
    author_email = "totallynotspykle@gmail.com"

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = ["icinga_base_url", "icinga_username", "icinga_password"]

    # Default configuration parameter values, if not set by the user
    default_settings = {
        "livestatus_port": 5665,
        "icinga_base_url_overrides": [],
    }

    # Base URL path. If not set, the plugin name will be used.
    base_url = "icinga"

    # Caching config
    caching_config = {}


config = NetboxIcingaConfig  # pylint: disable=invalid-name
