import re

from extras.plugins import PluginTemplateExtension  # pylint: disable=import-error

from . import livestatus


class NagiosStatus(PluginTemplateExtension):

    def __init__(self, context):
        super().__init__(context)
        self.settings = self.context["settings"].PLUGINS_CONFIG["netbox_nagios"]
        self.hostname = self.context["object"].name
        self.livestatus_host = self.get_livestatus_host()
        self.livestatus_port = self.settings["livestatus_port"]
        self.nagios_base_url = self.get_nagios_base_url()

    def get_livestatus_host(self):
        """Uses settings and potential overrides to determine the Nagios host."""
        for regex, livestatus_host in self.settings["livestatus_host_overrides"]:
            if re.search(regex, self.hostname):
                return livestatus_host
        return self.settings["livestatus_host"]

    def get_nagios_base_url(self):
        """Uses settings and potential overrides to determine the Nagios url."""
        for regex, nagios_base_url in self.settings["nagios_base_url_overrides"]:
            if re.search(regex, self.hostname):
                return nagios_base_url
        return self.settings["nagios_base_url"]

    def buttons(self):
        """Adds an extra button at the top of the bage."""
        return self.render(
            "device_nagios_buttons.html",
            extra_context={"nagios_base_url": self.nagios_base_url},
        )

    def right_page(self):
        """Adds a status table to the page."""
        extra_context = {
            "nagios_base_url": self.nagios_base_url,
        }
        try:
            extra_context["nagios"] = livestatus.hoststatus(
                self.hostname, self.livestatus_host, self.livestatus_port,
            )
        except Exception:  # pylint: disable=broad-except
            # Be very defensive so that broken Nagios doesn't break Netbox.
            pass
        return self.render("device_nagios_box.html", extra_context=extra_context)

class DCIMNagiosStatus(NagiosStatus):
    model = 'dcim.device'
    def right_page(self):
        return self.x_page()

class VirtualMachinesNagiosStatus(NagiosStatus):
    model = 'virtualization.virtual-machines'
    def right_page(self):
        return self.x_page()

template_extensions = [DCIMNagiosStatus, VirtualMachinesNagiosStatus]  # pylint: disable=invalid-name
