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
        "topic": "SystemState/State",
        "module_type": "system",
        "map": {
            0: "Off",
            1: "Low power",
            2: "VE.Bus Fault condition",
            3: "Bulk charging",
            4: "Absorption charging",
            5: "Float charging",
            6: "Storage mode",
            7: "Equalisation charging",
            8: "Passthru",
            9: "Inverting",
            10: "Assisting",
            244: "Battery Sustain",
            252: "External control",
            256: "Discharging",
            257: "Sustain",
            258: "Recharge",
            259: "Scheduled recharge"
        }
     },
    "High DC Current Alarm": {
        "topic": "Alarms/HighDcCurrent",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "High DC current condition"
        }
     },
    "State": {
        "topic": "State",
        "module_type": "vebus",
        "map": {
            0: "Off",
            1: "Low power",
            2: "Fault condition",
            3: "Bulk charging",
            4: "Absorption charging",
            5: "Float charging",
            6: "Storage mode",
            7: "Equalisation charging",
            8: "Passthru",
            9: "Inverting",
            10: "Power assist",
            11: "Power supply mode",
            244: "Sustain (Prefer Renewable Energy)",
            252: "External control",
        }
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
    "Grid Energy Import": {
        "device_class": "energy",
        "unit": "kWh",
        "topic":  "Ac/Energy/Forward",
        "module_type": "grid"
    },
    "Grid Energy Export": {
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
    "MPPT Current": {
        "device_class": "current",
        "unit": "A",
        "topic":  "Dc/0/Current",
        "module_type": "solarcharger"
    },
    "MPPT Power": {
        "device_class": "power",
        "unit": "W",
        "topic":  "Yield/Power",
        "module_type": "solarcharger"
    },
    "Total kWh produced": {
        "device_class": "energy",
        "unit": "kWh",
        "topic":  "Yield/System",
        "module_type": "solarcharger"
    },
    "MPPT State": {
        "topic": "State",
        "module_type": "solarcharger",
        "map": {
            0: "Off",
            2: "Fault",
            3: "Bulk",
            4: "Absorption",
            5: "Float",
            6: "Storage",
            7: "Equalize",
            252: "External control",
        }
    },
    "MPPT Error": {
        "topic": "ErrorCode",
        "module_type": "solarcharger",
        "map": {
            0: "No error",
            1: "Battery temperature too high",
            2: "Battery voltage too high",
            3: "Battery temperature sensor miswired (+)",
            4: "Battery temperature sensor miswired (-)",
            5: "Battery temperature sensor disconnected",
            6: "Battery voltage sense miswired (+)",
            7: "Battery voltage sense miswired (-)",
            8: "Battery voltage sense disconnected",
            9: "Battery voltage wire losses too high",
            17: "Charger temperature too high",
            18: "Charger over-current",
            19: "Charger current polarity reversed",
            20: "Bulk time limit reached",
            22: "Charger temperature sensor miswired",
            23: "Charger temperature sensor disconnected",
            34: "Input current too high"
        }
    },
    "MPPT Operation Mode": {
        "topic": "MppOperationMode",
        "module_type": "solarcharger",
        "map": {
            0: "Off",
            1: "Voltage or Current limited",
            2: "Active",
        }
     },    
}
