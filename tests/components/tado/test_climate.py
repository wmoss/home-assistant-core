"""The sensor tests for the tado platform."""

from .util import async_init_integration


async def test_air_con(hass):
    """Test creation of aircon climate."""

    await async_init_integration(hass)

    state = hass.states.get("climate.air_conditioning")
    assert state.state == "cool"

    expected_attributes = {
        "current_humidity": 60.9,
        "current_temperature": 24.8,
        "fan_mode": "auto",
        "fan_modes": ["auto", "high", "medium", "low"],
        "friendly_name": "Air Conditioning",
        "hvac_action": "cooling",
        "hvac_modes": ["off", "auto", "heat", "cool", "heat_cool", "dry", "fan_only"],
        "max_temp": 31.0,
        "min_temp": 16.0,
        "preset_mode": "home",
        "preset_modes": ["away", "home"],
        "supported_features": 25,
        "target_temp_step": 1,
        "temperature": 17.8,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(item in state.attributes.items() for item in expected_attributes.items())


async def test_heater(hass):
    """Test creation of heater climate."""

    await async_init_integration(hass)

    state = hass.states.get("climate.baseboard_heater")
    assert state.state == "heat"

    expected_attributes = {
        "current_humidity": 45.2,
        "current_temperature": 20.6,
        "friendly_name": "Baseboard Heater",
        "hvac_action": "idle",
        "hvac_modes": ["off", "auto", "heat"],
        "max_temp": 31.0,
        "min_temp": 16.0,
        "preset_mode": "home",
        "preset_modes": ["away", "home"],
        "supported_features": 17,
        "target_temp_step": 1,
        "temperature": 20.5,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(item in state.attributes.items() for item in expected_attributes.items())


async def test_smartac_with_swing(hass):
    """Test creation of smart ac with swing climate."""

    await async_init_integration(hass)

    state = hass.states.get("climate.air_conditioning_with_swing")
    assert state.state == "auto"

    expected_attributes = {
        "current_humidity": 42.3,
        "current_temperature": 20.9,
        "fan_mode": "auto",
        "fan_modes": ["auto", "high", "medium", "low"],
        "friendly_name": "Air Conditioning with swing",
        "hvac_action": "heating",
        "hvac_modes": ["off", "auto", "heat", "cool", "heat_cool", "dry", "fan_only"],
        "max_temp": 30.0,
        "min_temp": 16.0,
        "preset_mode": "home",
        "preset_modes": ["away", "home"],
        "swing_modes": ["on", "off"],
        "supported_features": 57,
        "target_temp_step": 1.0,
        "temperature": 20.0,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(item in state.attributes.items() for item in expected_attributes.items())
