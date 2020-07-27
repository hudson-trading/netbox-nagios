try:
    from extras.plugins import PluginConfig
except ImportError:
    # Dummy so install of wheel works without Netbox.
    class PluginConfig(object):
        pass


from .version import VERSION


class NetboxNagiosConfig(PluginConfig):
    """
    This class defines attributes for the NetBox Nagios plugin.
    """

    # Plugin package name
    name = "netbox_nagios"

    # Human-friendly name and description
    verbose_name = "Nagios"
    description = "Plugin to show Nagios status in Netbox"

    # Plugin version
    version = VERSION

    # Plugin author
    author = "Hudson River Trading LLC"
    author_email = "opensource@hudson-trading.com"

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = ["livestatus_host", "nagios_base_url"]

    # Default configuration parameter values, if not set by the user
    default_settings = {
        "livestatus_host_overrides": [],
        "livestatus_port": 6557,
        "nagios_base_url_overrides": [],
    }

    # Base URL path. If not set, the plugin name will be used.
    base_url = "nagios"

    # Caching config
    caching_config = {}


config = NetboxNagiosConfig  # pylint: disable=invalid-name
