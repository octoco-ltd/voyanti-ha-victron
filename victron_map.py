READ_PARAMETER_MAP = {'Grid energy meter import': {'device_class': 'energy', 'unit': 'kWh', 'topic': ' grid/30/Ac/Energy/Forward'}, 'Grid energy meter export': {'device_class': 'energy', 'unit': 'kWh', 'topic': ' grid/30/Ac/Energy/Reverse'}, 'Battery Percent': {'device_class': 'battery', 'unit': '%', 'topic': ' system/0/Dc/Battery/Soc'}, 'Active SOC Limit': {'device_class': 'battery', 'unit': '%', 'topic': ' settings/0/Settings/CGwacs/BatteryLife/SocLimit'}, 'Battery Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': ' system/0/Dc/Battery/Voltage'}, 'Battery Load': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Dc/Battery/Power'}, 'AC Loads Phase 1': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Ac/Consumption/L1/Power'}, 'AC Output Voltage Phase 1': {'device_class': 'voltage', 'unit': 'V', 'topic': ' vebus/276/Ac/Out/L1/V'}, 'AC Output Current Phase 1': {'device_class': 'current', 'unit': 'A', 'topic': ' vebus/276/Ac/Out/L1/I'}, 'AC Loads Phase 2': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Ac/Consumption/L2/Power'}, 'AC Output Voltage Phase 2': {'device_class': 'voltage', 'unit': 'V', 'topic': ' vebus/276/Ac/Out/L2/V'}, 'AC Output Current Phase 2': {'device_class': 'current', 'unit': 'A', 'topic': ' vebus/276/Ac/Out/L2/I'}, 'AC Loads Phase 3': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Ac/Consumption/L3/Power'}, 'AC Output Voltage Phase 3': {'device_class': 'voltage', 'unit': 'V', 'topic': ' vebus/276/Ac/Out/L3/V'}, 'AC Output Current Phase 3': {'device_class': 'current', 'unit': 'A', 'topic': ' vebus/276/Ac/Out/L3/I'}, 'Grid Power Phase 1': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Ac/Grid/L1/Power'}, 'Grid Power Phase 2': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Ac/Grid/L2/Power'}, 'Grid Power Phase 3': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Ac/Grid/L3/Power'}, 'Grid Power Total': {'device_class': 'power', 'unit': 'W', 'topic': ' grid/30/Ac/Power'}, 'Grid Voltage Phase 1': {'device_class': 'voltage', 'unit': 'V', 'topic': ' grid/30/Ac/L1/Voltage'}, 'Grid Voltage Phase 2': {'device_class': 'voltage', 'unit': 'V', 'topic': ' grid/30/Ac/L2/Voltage'}, 'Grid Voltage Phase 3': {'device_class': 'voltage', 'unit': 'V', 'topic': ' grid/30/Ac/L3/Voltage'}, 'Grid Current Phase 1': {'device_class': 'current', 'unit': 'A', 'topic': ' grid/30/Ac/L1/Current'}, 'Grid Current Phase 2': {'device_class': 'current', 'unit': 'A', 'topic': ' grid/30/Ac/L2/Current'}, 'Grid Current Phase 3': {'device_class': 'current', 'unit': 'A', 'topic': ' grid/30/Ac/L3/Current'}, 'Current Solar Production': {'device_class': 'power', 'unit': 'W', 'topic': ' system/0/Dc/Pv/Power'}, 'MPPT 0 Production': {'device_class': 'power', 'unit': 'W', 'topic': ' solarcharger/0/Yield/Power'}, 'MPPT 0 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': ' solarcharger/0/Dc/0/Voltage'}, 'MPPT 0 Current': {'device_class': 'current', 'unit': 'A', 'topic': ' solarcharger/0/Dc/0/Current'}, 'MPPT 277 Production': {'device_class': 'power', 'unit': 'W', 'topic': ' solarcharger/277/Yield/Power'}, 'MPPT 277 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': ' solarcharger/277/Dc/0/Voltage'}, 'MPPT 277 Current': {'device_class': 'current', 'unit': 'A', 'topic': ' solarcharger/277/Dc/0/Current'}, 'MPPT 280 Production': {'device_class': 'power', 'unit': 'W', 'topic': ' solarcharger/280/Yield/Power'}, 'MPPT 280 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': ' solarcharger/280/Dc/0/Voltage'}, 'MPPT 280 Current': {'device_class': 'current', 'unit': 'A', 'topic': ' solarcharger/280/Dc/0/Current'}, 'MPPT 281 Production': {'device_class': 'power', 'unit': 'W', 'topic': ' solarcharger/281/Yield/Power'}, 'MPPT 281 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': ' solarcharger/281/Dc/0/Voltage'}, 'MPPT 281 Current': {'device_class': 'current', 'unit': 'A', 'topic': ' solarcharger/281/Dc/0/Current'}, 'Solar Charger State 277': {'device_class': 'none', 'unit': None, 'topic': ' solarcharger/277/State'}, 'Solar Charger State 280': {'device_class': 'none', 'unit': None, 'topic': ' solarcharger/280/State'}, 'Solar Charger State 281': {'device_class': 'none', 'unit': None, 'topic': ' solarcharger/281/State'}, 'Active input source': {'device_class': 'none', 'unit': None, 'topic': ' system/0/Ac/ActiveIn/Source'}, 'Inverter State': {'device_class': 'none', 'unit': None, 'topic': ' system/0/SystemState/State'}, 'SMD Total Battery Capacity': {'device_class': 'battery', 'unit': '%', 'topic': 'outputEnergy/bank1'}, 'SMD Battery Discharge Power': {'device_class': 'power', 'unit': 'W', 'topic': 'outputPower/bank1-dischargingPower'}, 'SMD Battery Power In': {'device_class': 'power', 'unit': 'W', 'topic': 'outputEnergy/bank1'}, 'Remaining Battery Capacity': {'device_class': 'energy_storage', 'unit': 'Wh', 'topic': 'outputEnergy/bank1'}, 'Battery1 SOC': {'device_class': 'battery', 'unit': '%', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'Battery2 SOC': {'device_class': 'battery', 'unit': '%', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'Battery3 SOC': {'device_class': 'battery', 'unit': '%', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'Battery4 SOC': {'device_class': 'battery', 'unit': '%', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'Battery5 SOC': {'device_class': 'battery', 'unit': '%', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'SMD Battery1 Capacity': {'device_class': 'none', 'unit': 'Ah', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'SMD Battery2 Capacity': {'device_class': 'none', 'unit': 'Ah', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'SMD Battery3 Capacity': {'device_class': 'none', 'unit': 'Ah', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'SMD Battery4 Capacity': {'device_class': 'none', 'unit': 'Ah', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'SMD Battery5 Capacity': {'device_class': 'none', 'unit': 'Ah', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'SMD Battery1 Power': {'device_class': 'power', 'unit': 'W', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'SMD Battery1 Current': {'device_class': 'current', 'unit': 'A', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'SMD Battery1 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'SMD Battery2 Power': {'device_class': 'power', 'unit': 'W', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'SMD Battery2 Current': {'device_class': 'current', 'unit': 'A', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'SMD Battery2 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'SMD Battery3 Power': {'device_class': 'power', 'unit': 'W', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'SMD Battery3 Current': {'device_class': 'current', 'unit': 'A', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'SMD Battery3 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'SMD Battery4 Power': {'device_class': 'power', 'unit': 'W', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'SMD Battery4 Current': {'device_class': 'current', 'unit': 'A', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'SMD Battery4 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'SMD Battery5 Power': {'device_class': 'power', 'unit': 'W', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'SMD Battery5 Current': {'device_class': 'current', 'unit': 'A', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'SMD Battery5 Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'Battery1 Max Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'Battery1 Min Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'Battery2 Max Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'Battery2 Min Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'Battery3 Max Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'Battery3 Min Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'Battery4 Max Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'Battery4 Min Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'Battery5 Max Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'Battery5 Min Cell Voltage': {'device_class': 'voltage', 'unit': 'V', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'Battery1 Temperature': {'device_class': 'temperature', 'unit': '°C', 'topic': 'inputEnergy/SMDBEM10303621 '}, 'Battery2 Temperature': {'device_class': 'temperature', 'unit': '°C', 'topic': 'inputEnergy/SMDBEM10303673 '}, 'Battery3 Temperature': {'device_class': 'temperature', 'unit': '°C', 'topic': 'inputEnergy/SMDBEM10303471 '}, 'Battery4 Temperature': {'device_class': 'temperature', 'unit': '°C', 'topic': 'inputEnergy/SMDBEM10303453 '}, 'Battery5 Temperature': {'device_class': 'temperature', 'unit': '°C', 'topic': 'inputEnergy/SMDBEX20226624 '}, 'SMD Battery1 Charge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303621 '}, 'SMD Battery1 Discharge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303621 '}, 'SMD Battery2 Charge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303673 '}, 'SMD Battery2 Discharge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303673 '}, 'SMD Battery3 Charge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303471 '}, 'SMD Battery3 Discharge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303471 '}, 'SMD Battery4 Charge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303453 '}, 'SMD Battery4 Discharge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303453 '}, 'SMD Battery5 Charge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEX20226624 '}, 'SMD Battery5 Discharge Counter': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEX20226624 '}, 'Battery2 Balancing Status': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303673'}, 'Battery3 Balancing Status': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303471'}, 'Battery4 Balancing Status': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEM10303453'}, 'Battery5 Balancing Status': {'device_class': 'none', 'unit': None, 'topic': 'inputEnergy/SMDBEX20226624'}, 'Battery1 SoH': {'device_class': 'none', 'unit': '%', 'topic': 'battery/soh1'}, 'Battery2 SoH': {'device_class': 'none', 'unit': '%', 'topic': 'battery/soh2'}, 'Battery3 SoH': {'device_class': 'none', 'unit': '%', 'topic': 'battery/soh3'}, 'Battery4 SoH': {'device_class': 'none', 'unit': '%', 'topic': 'battery/soh4'}, 'Battery5 SoH': {'device_class': 'none', 'unit': '%', 'topic': 'battery/soh5'}, 'SoC Profile': {'device_class': 'none', 'unit': None, 'topic': 'vems/soc_profile'}, 'Current SoC Target': {'device_class': 'none', 'unit': '%', 'topic': 'vems/current_soc_target'}, 'Current SoC Target Hour': {'device_class': 'none', 'unit': None, 'topic': 'vems/current_soc_target_hour'}, 'PV Forecast Today': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/pv_forecast_today'}, 'PV Forecast Tomorrow': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/pv_forecast_tomorrow'}, 'PV Remaining Today': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/pv_remaining_today'}, 'PV Forecast Morning': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/pv_forecast_morning'}, 'PV Forecast Afternoon': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/pv_forecast_afternoon'}, 'Solar Forecast Today': {'device_class': 'none', 'unit': None, 'topic': 'vems/solar_forecast_today/state'}, 'Power Forecast': {'device_class': 'none', 'unit': None, 'topic': 'vems/power_forecast/state'}, 'PV Power Forecast Now': {'device_class': 'none', 'unit': 'kW', 'topic': 'vems/pv_forecast_power_now'}, 'Excess Power': {'device_class': 'power', 'unit': 'W', 'topic': 'vems/excess_power'}, 'ToU Rate': {'device_class': 'none', 'unit': None, 'topic': 'vems/tou_rate'}, 'Peak Total Cost Import': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/import/peak_total_cost'}, 'Standard Total Cost Import': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/import/standard_total_cost'}, 'Off Peak Total Cost Import': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/import/off_peak_total_cost'}, 'Total Cost Import': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/import/total_cost'}, 'Peak Total Energy Import': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/import/peak_total_energy'}, 'Standard Total Energy Import': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/import/standard_total_energy'}, 'Off Peak Total Energy Import': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/import/off_peak_total_energy'}, 'Peak Total Cost Load': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/load/peak_total_cost'}, 'Standard Total Cost Load': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/load/standard_total_cost'}, 'Off Peak Total Cost Load': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/load/off_peak_total_cost'}, 'Total Cost Load': {'device_class': 'monetary', 'unit': 'ZAR', 'topic': 'vems/load/total_cost'}, 'Peak Total Energy Load': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/load/peak_total_energy'}, 'Standard Total Energy Load': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/load/standard_total_energy'}, 'Off Peak Total Energy Load': {'device_class': 'none', 'unit': 'kWh', 'topic': 'vems/load/off_peak_total_energy'}, 'SoC Profile Dynamic': {'device_class': 'none', 'unit': None, 'topic': 'vems/soc_profile_dyn'}, 'Dynamic SoC Target': {'device_class': 'battery', 'unit': '%', 'topic': 'vems/dynamic_soc_target'}}