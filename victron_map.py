READ_PARAMETER_MAP = {
    "Battery SoC": {
        "device_class": "battery",
        "unit": "%",
        "topic":  "system/0/Dc/Battery/Soc",
    },
    "Active SOC Limit": {
        "device_class": "battery",
        "unit": "%",
        "topic":  "settings/0/Settings/CGwacs/BatteryLife/SocLimit",
    },
    "BMS Battery Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "system/0/Dc/Battery/Voltage",
    },
    "BMS Battery Load": {
        "device_class": "power",
        "unit": "W",
        "topic":  "system/0/Dc/Battery/Power",
    },
    "Total PV Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "system/0/Dc/Pv/Power",
    },
    "Active Input Source": {
        "device_class": "none",
        "unit": None,
        "topic":  "system/0/Ac/ActiveIn/Source",
    },
    "Inverter State": {
        "device_class": "none",
        "unit": None,
        "topic":  "system/0/SystemState/State",
    },
    "Load L1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "vebus/276/Ac/Out/L1/P",
    },
    "Load L1 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "vebus/276/Ac/Out/L1/V",
    },
    "Load L1 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "vebus/276/Ac/Out/L1/I",
    },
    "Load L2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "vebus/276/Ac/Out/L2/P",
    },
    "Load L2 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "vebus/276/Ac/Out/L2/V",
    },
    "Load L2 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "vebus/276/Ac/Out/L2/I",
    },
    "Load L3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "vebus/276/Ac/Out/L3/P",
    },
    "Load L3 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "vebus/276/Ac/Out/L3/V",
    },
    "Load L3 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "vebus/276/Ac/Out/L3/I",
    },
    "Active Input L1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "vebus/276/Ac/ActiveIn/L1/P",
    },
    "Active Input L2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "vebus/276/Ac/ActiveIn/L2/P",
    },
    "Active Input L3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "vebus/276/Ac/ActiveIn/L3/P",
    },
    "Grid meter energy import": {
        "device_class": "energy",
        "unit": "kWh",
        "topic":  "grid/30/Ac/Energy/Forward",
    },
    "Grid meter energy export": {
        "device_class": "energy",
        "unit": "kWh",
        "topic":  "grid/30/Ac/Energy/Reverse",
    },
    "Grid L1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "grid/30/Ac/L1/Power",
    },
    "Grid L2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "grid/30/Ac/L2/Power",
    },
    "Grid L3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "grid/30/Ac/L3/Power",
    },
    "Total Grid Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "grid/30/Ac/Power",
    },
    "Grid L1 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "grid/30/Ac/L1/Voltage",
    },
    "Grid L2 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "grid/30/Ac/L2/Voltage",
    },
    "Grid L3 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "grid/30/Ac/L3/Voltage",
    },
    "Grid L1 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "grid/30/Ac/L1/Current",
    },
    "Grid L2 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "grid/30/Ac/L2/Current",
    },
    "Grid L3 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "grid/30/Ac/L3/Current",
    },
    "MPPT 1 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "solarcharger/0/Yield/Power",
    },
    "MPPT 1 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "solarcharger/0/Dc/0/Voltage",
    },
    "MPPT 1 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "solarcharger/0/Dc/0/Current",
    },
    "MPPT 1 State": {
        "device_class": "none",
        "unit": None,
        "topic":  "solarcharger/0/State",
    },
    "MPPT 2 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "solarcharger/277/Yield/Power",
    },
    "MPPT 2 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "solarcharger/277/Dc/0/Voltage",
    },
    "MPPT 2 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "solarcharger/277/Dc/0/Current",
    },
    "MPPT 2 State": {
        "device_class": "none",
        "unit": None,
        "topic":  "solarcharger/277/State",
    },
    "MPPT 3 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "solarcharger/280/Yield/Power",
    },
    "MPPT 3 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "solarcharger/280/Dc/0/Voltage",
    },
    "MPPT 3 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "solarcharger/280/Dc/0/Current",
    },
    "MPPT 3 State": {
        "device_class": "none",
        "unit": None,
        "topic":  "solarcharger/280/State",
    },
    "MPPT 4 Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "solarcharger/281/Yield/Power",
    },
    "MPPT 4 Voltage": {
        "device_class": "voltage",
        "unit": "V",
        "topic":  "solarcharger/281/Dc/0/Voltage",
    },
    "MPPT 4 Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "solarcharger/281/Dc/0/Current",
    },
    "MPPT 4 State": {
        "device_class": "none",
        "unit": None,
        "topic":  "solarcharger/281/State",
    },
}
