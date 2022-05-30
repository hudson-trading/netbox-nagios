# icinga Status in NetBox

Plugin to show icinga host and service status in NetBox on the device and device/VM page.

![Preview](docs/images/preview.png)

## Installation

Package this plugin to .whl by runnig `pip3 whel .`, then install package in
netbox's venv (located by default @`/opt/netbox/venv`)

Add the plugin to your `PLUGINS` list in `configuration.py` and configure at
least `icinga_base_url`, `icinga_username` and `icinga_password` option in `PLUGINS_CONFIG`:

```python
PLUGINS = [
    "netbox_icinga",
]

PLUGINS_CONFIG = {
    "netbox_icinga": {
        "icinga_base_url" : "icinga.example.com",
        "icinga_username" : "username",
        "icinga_password" : "password"
    },
}
```
*(authorization via X.509 client certificate is not yet supported)*

Finally, restart netbox service to apply changes; for distros with systemd run:
`systemctl restart netbox`

## Advanced config

Optional options are `livestatus_port` (defaults to 5665)
`icinga_base_url_overrides` (both default to an
empty list) that take tuples of `(regex, override)` to use a different
livestatus host or icinga URL for a subset of hosts. The regexes are applied in
order, with the first match being used.

Example:

```python
PLUGINS_CONFIG = {
    "netbox_icinga": {
        ...
        "icinga_base_url_overrides": [
            (r"^(some|other)host$", "https://icinga-special.example.com/icinga/cgi-bin/"),
        ],
    },
}
```
