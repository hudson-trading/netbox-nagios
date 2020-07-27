from django import template  # pylint: disable=import-error

register = template.Library()  # pylint: disable=invalid-name


@register.filter(is_safe=True)
def nagios_status_color(value: int):
    local_colors = {0: "success", 1: "warning", 2: "danger", 3: "info"}
    return local_colors.get(value, "default")


@register.filter(is_safe=True)
def nagios_status_string(value: int):
    strings = {0: "OK", 1: "WARN", 2: "CRIT", 3: "UNKN"}
    return strings.get(value, "NO DATA")
