"""An abstract class common to all Switchbot entities."""
from __future__ import annotations

from collections.abc import Mapping
import logging
from typing import Any

from switchbot import Switchbot, SwitchbotDevice

from homeassistant.components.bluetooth.passive_update_coordinator import PassiveBluetoothCoordinatorEntity
from homeassistant.const import ATTR_CONNECTIONS
from homeassistant.core import callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import ToggleEntity

from .coordinator import GenericBTCoordinator

_LOGGER = logging.getLogger(__name__)

class GenericBTEntity(PassiveBluetoothCoordinatorEntity[GenericBTCoordinator]):
    """Generic entity encapsulating common features of Generic BT device."""

    _device: GenericBTDevice
    _attr_has_entity_name = True

    def __init__(self, coordinator: GenericBTCoordinator) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._device = coordinator.device
        self._address = coordinator.ble_device.address
        self._attr_unique_id = coordinator.base_unique_id
        self._attr_device_info = {
            "connections":{(dr.CONNECTION_BLUETOOTH, self._address)},
            "name":coordinator.device_name
        }