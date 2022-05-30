import re

from extras.plugins import PluginTemplateExtension  # pylint: disable=import-error

from . import livestatus


class icingaStatus(PluginTemplateExtension):
    def __init__(self, context):
        super().__init__(context)
        self.settings = self.context["settings"].PLUGINS_CONFIG["netbox_icinga"]
        self.hostname = self.context["object"].name or ""  # name can be None.
        self.livestatus_port = self.settings["livestatus_port"]
        self.icinga_username = self.settings["icinga_username"]
        self.icinga_password = self.settings["icinga_password"]
        self.icinga_base_url = self.get_icinga_base_url()

    def get_icinga_base_url(self):
        """Uses settings and potential overrides to determine the icinga url."""
        for regex, icinga_base_url in self.settings["icinga_base_url_overrides"]:
            if re.search(regex, self.hostname):
                return icinga_base_url
        return self.settings["icinga_base_url"]

    def buttons(self):
        """Adds an extra button at the top of the bage."""
        return self.render(
            "device_icinga_buttons.html",
            extra_context={"icinga_base_url": self.icinga_base_url},
        )

    def right_page(self):
        """Adds a status table to the page."""
        extra_context = {
            "icinga_base_url": self.icinga_base_url
        }
        try:
            extra_context["icinga"] = livestatus.hoststatus(
                self.hostname,
                self.icinga_base_url,
                self.livestatus_port,
                self.icinga_username,
                self.icinga_password
            )
        except Exception:  # pylint: disable=broad-except
            # Be very defensive so that broken icinga doesn't break Netbox.
            pass
        return self.render("device_icinga_box.html", extra_context=extra_context)


class icingaStatusDevice(icingaStatus):
    model = "dcim.device"


class icingaStatusVM(icingaStatus):
    model = "virtualization.virtualmachine"


template_extensions = [  # pylint: disable=invalid-name
    icingaStatusDevice,
    icingaStatusVM,
]
