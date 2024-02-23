import json
import pandas as pd
from loguru import logger

df = pd.read_csv("P610_Honeywell_DEMO.csv",sep=",",header=0)

def generate_devices() -> list[dict]:
    timeseries = []
    
    for idx, row in df.iterrows():
        point_name_parts = row["Object Name"].split('.')[-2:]
        point_name = ''.join(point_name_parts)
        object_id = row['Name'].replace('_', ':')
        
        match row["Object Type"]:
            case "Analog Value":
                value_type = "string"
            case "Binary Value":
                value_type = "bool"
                
        timeseries.append({
            "key": point_name,
            "type": value_type,
            "objectId": object_id,
            "propertyId": "presentValue"
        })
    
    return timeseries

generated_devices = generate_devices()

data = {
    "general": {
        "objectName": "TB_gateway",
        "address": "0.0.0.0:47808",
        "objectIdentifier": 599,
        "maxApduLengthAccepted": 1476,
        "segmentationSupported": "segmentedBoth",
        "vendorIdentifier": 15
    },
    "devices": [
        {
            "deviceName": "BACnet_Device_${objectName}",
            "deviceType": "default",
            "address": "192.168.51.1:47808",
            "pollPeriod": 5000,
            "timeseries": generated_devices,
            "serverSideRpc": [
                {
                    "method": "set_state",
                    "requestType": "writeProperty",
                    "requestTimeout": 10000,
                    "objectId": "binaryOutput:1",
                    "propertyId": "presentValue"
                },
                {
                    "method": "get_state",
                    "requestType": "readProperty",
                    "requestTimeout": 10000,
                    "objectId": "binaryOutput:1",
                    "propertyId": "presentValue"
                }
            ]
        }
    ]
}

with open("thingsboard_gateway/config/generated_bacnet.json", "w") as jf:
    json.dump(data, jf, indent=2)

logger.debug("OK")