# icinga Status in NetBox

Plugin to show icinga host and service status in NetBox on the device and VM page.

![Preview](docs/images/preview.png)

## Installation

Add the plugin to your `PLUGINS` list in `configuration.py` and configure at
least the `livestatus_host` and `icinga_base_url` options in `PLUGINS_CONFIG`:

```python
PLUGINS = [
    "netbox_icinga",
]

PLUGINS_CONFIG = {
    "netbox_icinga": {
        "livestatus_host": "icinga.example.com",
        "icinga_base_url": "https://icinga.example.com/icinga/cgi-bin/",
    },
}
```

Optional options are `livestatus_port` (defaults to 6557)
`livestatus_host_overrides` and `icinga_base_url_overrides` (both default to an
empty list) that take tuples of `(regex, override)` to use a different
livestatus host or icinga URL for a subset of hosts. The regexes are applied in
order, with the first match being used.

Example:

```python
PLUGINS_CONFIG = {
    "netbox_icinga": {
        ...
        "livestatus_host_overrides": [
            (r"^(some|other)host$", "icinga-special.example.com"),
        ],
        "icinga_base_url_overrides": [
            (r"^(some|other)host$", "https://icinga-special.example.com/icinga/cgi-bin/"),
        ],
    },
}
```
