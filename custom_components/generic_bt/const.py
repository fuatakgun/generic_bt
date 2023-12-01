"""Constants"""
import voluptuous as vol
from enum import Enum, auto

from homeassistant.helpers.config_validation import make_entity_service_schema
import homeassistant.helpers.config_validation as cv

DOMAIN = "generic_bt"
DEVICE_STARTUP_TIMEOUT_SECONDS = 30

class Schema(Enum):
    """General used service schema definition"""

    WRITE_GATT = make_entity_service_schema(
        {
            vol.Required("target_uuid"): cv.string,
            vol.Required("data"): cv.string
        }
    )
    READ_GATT = make_entity_service_schema(
        {
            vol.Required("target_uuid"): cv.string
        }
    )