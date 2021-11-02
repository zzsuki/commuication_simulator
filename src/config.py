PROTOCOL_PORT_MAP = {
    "Modbus": {
        "TCP": 502,
        "UDP": None,
    },
    "S7COMM": {
        "TCP": 102,
    },
    "FINS": {
        "TCP": 9600,
    },
    "DNP3": {
        "TCP": 20000,
    },
    "OpcUA": {
        "TCP": 48400,
    },
    "IEC104": {
        "TCP": 2404,
    },
    "BACnet": {
        "UDP": 47808,
    }
}


# 规约告警
PROTOALERT_MAP = {
    "Modbus": [
    ],
    "S7COMM": [
        "0300002b02f0803201000010d0001a00000403120a10020002000083000058120a100200010000830003",
    ],
    "DNP3": [
        "056408c404000300b4b8",
    ],
    "FINS": [
        "800002000000000000",
    ],
    "OpcUA": [
    ],
    "OpcDA": [
    ],
    "OpcAE": [
    ]
}