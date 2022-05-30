# icinga Status in NetBox

Plugin to show icinga host and service status in NetBox on the device and device/VM page.

![Preview](docs/images/preview.png)

## Installation

Add the plugin to your `PLUGINS` list in `configuration.py` and configure at
least `icinga_base_url` option in `PLUGINS_CONFIG`:

```python
PLUGINS = [
    "netbox_icinga",
]

PLUGINS_CONFIG = {
    "netbox_icinga": {
        "icinga_base_url": "icinga.example.com"
    },
}
```

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
