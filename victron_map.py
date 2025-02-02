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
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Dc/Battery/Voltage",
        "module_type": "system"
    },
    "BMS Battery Load": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Dc/Battery/Power",
        "module_type": "system"
    },
    "Total PV Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Dc/Pv/Power",
        "module_type": "system"
    },
    "Active Input Source": {
        "topic":  "Ac/ActiveIn/Source",
        "module_type": "system",
        "map": {
            0: "Not available",
            1: "Grid",
            2: "Genset",
            3: "Shore",
            240: "Inverting or Island mode"            
        }
     },
    "FeedbackEnabled": {
        "topic":  "Ac/ActiveIn/FeedbackEnabled",
        "module_type": "system",
        "map": {
            0: "No",
            1: "Yes"          
        }
     },
    "NumberOfPhases": {
        "topic":  "Ac/Consumption/NumberOfPhases",
        "module_type": "system",
        "map": {
            1: "Single",
            2: "Split",
            3: "Three"          
        }
     },
    "AC Input 1 Source": {
        "topic":  "Ac/In/0/Source",
        "module_type": "system",
        "map": {
            0: "Not used",
            1: "Grid",  
            2: "Generator",
            3: "Shore"  
        }
     },
    "AC Input 1": {
        "topic":  "Ac/In/0/Connected",
        "module_type": "system",
        "map": {
            0: "Disconected",
            1: "Connected"  
        }
     },
    "AC Input 2 Source": {
        "topic":  "Ac/In/1/Source",
        "module_type": "system",
        "map": {
            0: "Not used",
            1: "Grid",  
            2: "Generator",
            3: "Shore"  
        }
     },
    "AC Input 2": {
        "topic":  "Ac/In/1/Connected",
        "module_type": "system",
        "map": {
            0: "Disconected",
            1: "Connected"  
        }
     },
    "System State": {
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
            2: "HighDCcurrent"
        }
     },
    "High DC Voltage Alarm": {
        "topic": "Alarms/HighDcVoltage",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "HighDCvoltage"
        }
     },
    "PhaseRotation Alarm": {
        "topic": "Alarms/PhaseRotation",
        "module_type": "vebus",
        "map": {
            0: "OK",
            1: "PhaseRotation warning"
        }
     },
    "Low Battery Alarm": {
        "topic": "Alarms/LowBattery",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "LowBattery"
        }
     },
    "L1 HighTemperature Alarm": {
        "topic": "Alarms/L1/HighTemperature",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "HighTemperature"
        }
     },
    "L2 HighTemperature Alarm": {
        "topic": "Alarms/L2/HighTemperature",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "HighTemperaturee"
        }
     },
    "L3 HighTemperature Alarm": {
        "topic": "Alarms/L3/HighTemperature",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "HighTemperature"
        }
     },     
    "L1 Overload Alarm": {
        "topic": "Alarms/L1/Overload",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "Overload"
        }
     },
    "L2 Overload Alarm": {
        "topic": "Alarms/L2/Overload",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "Overload"
        }
     },
    "L3 Overload Alarm": {
        "topic": "Alarms/L3/Overload",
        "module_type": "vebus",
        "map": {
            0: "OK",
            2: "Overload"
        }
     },  
    "Inverter State": {
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
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/Out/L1/P",
        "module_type": "vebus"
    },
    "Load L1 Apparent Power": {
        "device_class": "apparent_power",
        "state_class": "measurement",
        "unit": "VA",
        "topic":  "Ac/Out/L1/S",
        "module_type": "vebus"
    },
    "Load L1 Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Ac/Out/L1/V",
        "module_type": "vebus"
    },
    "Load L1 Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Ac/Out/L1/I",
        "module_type": "vebus"
    },
    "Load L2 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/Out/L2/P",
        "module_type": "vebus"
    },
    "Load L2 Apparent Power": {
        "device_class": "apparent_power",
        "state_class": "measurement",
        "unit": "VA",
        "topic":  "Ac/Out/L2/S",
        "module_type": "vebus"
    },
    "Load L2 Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Ac/Out/L2/V",
        "module_type": "vebus"
    },
    "Load L2 Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Ac/Out/L2/I",
        "module_type": "vebus"
    },
    "Load L3 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/Out/L3/P",
        "module_type": "vebus"
    },
    "Load L3 Apparent Power": {
        "device_class": "apparent_power",
        "state_class": "measurement",
        "unit": "VA",
        "topic":  "Ac/Out/L3/S",
        "module_type": "vebus"
    },
    "Load L3 Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Ac/Out/L3/V",
        "module_type": "vebus"
    },
    "Load L3 Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Ac/Out/L3/I",
        "module_type": "vebus"
    },
    "Total Load Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/Out/P",
        "module_type": "vebus"
    },
    "Total Apparant Load Power": {
        "device_class": "apparent_power",
        "state_class": "measurement",
        "unit": "VA",
        "topic":  "Ac/Out/S",
        "module_type": "vebus"
    },
    "Active Input L1 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/ActiveIn/L1/P",
        "module_type": "vebus"
    },
    "Active Input L2 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/ActiveIn/L2/P",
        "module_type": "vebus"
    },
    "Active Input L3 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/ActiveIn/L3/P",
        "module_type": "vebus"
    },
    "Grid Energy Import": {
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
        "topic":  "Ac/Energy/Forward",
        "module_type": "grid"
    },
    "Grid Energy Export": {
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
        "topic":  "Ac/Energy/Reverse",
        "module_type": "grid"
    },
    "Grid L1 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/L1/Power",
        "module_type": "grid"
    },
    "Grid L2 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/L2/Power",
        "module_type": "grid"
    },
    "Grid L3 Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/L3/Power",
        "module_type": "grid"
    },
    "Total Grid Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Ac/Power",
        "module_type": "grid"
    },
    "Grid L1 Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Ac/L1/Voltage",
        "module_type": "grid"
    },
    "Grid L2 Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Ac/L2/Voltage",
        "module_type": "grid"
    },
    "Grid L3 Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Ac/L3/Voltage",
        "module_type": "grid"
    },
    "Grid L1 Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Ac/L1/Current",
        "module_type": "grid"
    },
    "Grid L2 Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Ac/L2/Current",
        "module_type": "grid"
    },
    "Grid L3 Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Ac/L3/Current",
        "module_type": "grid"
    },
    "MPPT Voltage": {
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
        "topic":  "Dc/0/Voltage",
        "module_type": "solarcharger"
    },
    "MPPT Current": {
        "device_class": "current",
        "state_class": "measurement",
        "unit": "A",
        "topic":  "Dc/0/Current",
        "module_type": "solarcharger"
    },
    "MPPT Power": {
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
        "topic":  "Yield/Power",
        "module_type": "solarcharger"
    },
    "Energy produced": {
        "device_class": "energy",
        "state_class": "total_increasing",
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
