READ_PARAMETER_MAP = {
    "Battery SoC": {
        "device_class": "battery",
        "unit": "%",
        "topic":  "Dc/Battery/Soc",
        "module_type": "system"
    },
    "Active SOC Limit": {
        "device_class": "battery",
        "unit": "%",
        "topic":  "Settings/CGwacs/BatteryLife/SocLimit",
        "module_type": "settings"
    },
    "BMS Battery Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Dc/Battery/Voltage",
        "module_type": "system"
    },
    "BMS Battery Load": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Dc/Battery/Power",
        "module_type": "system"
    },
    "Total PV Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Dc/Pv/Power",
        "module_type": "system"
    },
    "Active Input Source": {
        "device_class": "none",
        "unit": None,
        "topic":  "Ac/ActiveIn/Source",
        "module_type": "system"
    },
    "Inverter State": {
        "device_class": "none",
        "unit": None,
        "topic":  "SystemState/State",
        "module_type": "system"
    },
    "Load L1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/Out/L1/P",
        "module_type": "vebus"
    },
    "Load L1 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Ac/Out/L1/V",
        "module_type": "vebus"
    },
    "Load L1 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Ac/Out/L1/I",
        "module_type": "vebus"
    },
    "Load L2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/Out/L2/P",
        "module_type": "vebus"
    },
    "Load L2 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Ac/Out/L2/V",
        "module_type": "vebus"
    },
    "Load L2 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Ac/Out/L2/I",
        "module_type": "vebus"
    },
    "Load L3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/Out/L3/P",
        "module_type": "vebus"
    },
    "Load L3 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Ac/Out/L3/V",
        "module_type": "vebus"
    },
    "Load L3 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Ac/Out/L3/I",
        "module_type": "vebus"
    },
    "Total Load Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/Out/P",
        "module_type": "vebus"
    },
    "Active Input L1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/ActiveIn/L1/P",
        "module_type": "vebus"
    },
    "Active Input L2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/ActiveIn/L2/P",
        "module_type": "vebus"
    },
    "Active Input L3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/ActiveIn/L3/P",
        "module_type": "vebus"
    },
    "Grid meter energy import": {
        "device_class": "energy",
        "unit": "kWh",
        "topic":  "Ac/Energy/Forward",
        "module_type": "grid"
    },
    "Grid meter energy export": {
        "device_class": "energy",
        "unit": "kWh",
        "topic":  "Ac/Energy/Reverse",
        "module_type": "grid"
    },
    "Grid L1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/L1/Power",
        "module_type": "grid"
    },
    "Grid L2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/L2/Power",
        "module_type": "grid"
    },
    "Grid L3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/L3/Power",
        "module_type": "grid"
    },
    "Total Grid Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Ac/Power",
        "module_type": "grid"
    },
    "Grid L1 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Ac/L1/Voltage",
        "module_type": "grid"
    },
    "Grid L2 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Ac/L2/Voltage",
        "module_type": "grid"
    },
    "Grid L3 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Ac/L3/Voltage",
        "module_type": "grid"
    },
    "Grid L1 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Ac/L1/Current",
        "module_type": "grid"
    },
    "Grid L2 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Ac/L2/Current",
        "module_type": "grid"
    },
    "Grid L3 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Ac/L3/Current",
        "module_type": "grid"
    },
    "MPPT Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "Dc/0/Voltage",
        "module_type": "solarcharger"
    },
    "MPPT urrent": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Dc/0/Current",
        "module_type": "solarcharger"
    },
    "MPPT State": {
        "device_class": "none",
        "unit": None,
        "topic":  "State",
        "module_type": "solarcharger"
    },
}
