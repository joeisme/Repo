[
    {
        "id": "835a7c5f.8ab8c",
        "type": "tab",
        "label": "¬yµ{1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "795fc2a0.349bdc",
        "type": "rpi-gpio out",
        "z": "835a7c5f.8ab8c",
        "name": "Green LED",
        "pin": "7",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 360,
        "y": 220,
        "wires": []
    },
    {
        "id": "692e079f.929168",
        "type": "inject",
        "z": "835a7c5f.8ab8c",
        "name": "on",
        "topic": "",
        "payload": "1",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 170,
        "y": 120,
        "wires": [
            [
                "795fc2a0.349bdc",
                "36019ac7.a8ccf6"
            ]
        ]
    },
    {
        "id": "ce63429f.4110b",
        "type": "inject",
        "z": "835a7c5f.8ab8c",
        "name": "off",
        "topic": "",
        "payload": "0",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 160,
        "y": 240,
        "wires": [
            [
                "795fc2a0.349bdc",
                "36019ac7.a8ccf6"
            ]
        ]
    },
    {
        "id": "36019ac7.a8ccf6",
        "type": "debug",
        "z": "835a7c5f.8ab8c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 360,
        "y": 80,
        "wires": []
    }
]