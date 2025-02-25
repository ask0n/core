"""Nexia constants."""
from homeassistant.const import Platform

PLATFORMS = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.CLIMATE,
    Platform.SCENE,
    Platform.SWITCH,
]

ATTRIBUTION = "Data provided by mynexia.com"

NOTIFICATION_ID = "nexia_notification"
NOTIFICATION_TITLE = "Nexia Setup"

CONF_BRAND = "brand"

NEXIA_SCAN_INTERVAL = "scan_interval"

DOMAIN = "nexia"
DEFAULT_ENTITY_NAMESPACE = "nexia"

ATTR_DESCRIPTION = "description"

ATTR_AIRCLEANER_MODE = "aircleaner_mode"

ATTR_RUN_MODE = "run_mode"

ATTR_ZONE_STATUS = "zone_status"
ATTR_HUMIDIFY_SETPOINT = "humidify_setpoint"
ATTR_DEHUMIDIFY_SETPOINT = "dehumidify_setpoint"


MANUFACTURER = "Trane"

SIGNAL_ZONE_UPDATE = "NEXIA_CLIMATE_ZONE_UPDATE"
SIGNAL_THERMOSTAT_UPDATE = "NEXIA_CLIMATE_THERMOSTAT_UPDATE"

BRAND_NEXIA_NAME = "Nexia"
BRAND_ASAIR_NAME = "American Standard Home"
BRAND_TRANE_NAME = "Trane Home"
