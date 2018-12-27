[
    {
        "id": "a7e499b8.5a5148",
        "type": "tab",
        "label": "¬yµ{3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "c2c42f83.d9ad6",
        "type": "inject",
        "z": "a7e499b8.5a5148",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 110,
        "y": 160,
        "wires": [
            [
                "982411c0.0d25"
            ]
        ]
    },
    {
        "id": "982411c0.0d25",
        "type": "function",
        "z": "a7e499b8.5a5148",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey:\"FtZyZYF7b0Ho8drT\"\n};\nmsg.payload= \"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 280,
        "wires": [
            [
                "74bae97.ab6ef18"
            ]
        ]
    },
    {
        "id": "74bae97.ab6ef18",
        "type": "http request",
        "z": "a7e499b8.5a5148",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DaqpJ9pk/datapoints.csv",
        "tls": "",
        "x": 540,
        "y": 300,
        "wires": [
            [
                "929c04cf.3f9d98",
                "b1eb7a28.c64838"
            ]
        ]
    },
    {
        "id": "b1eb7a28.c64838",
        "type": "debug",
        "z": "a7e499b8.5a5148",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 830,
        "y": 460,
        "wires": []
    },
    {
        "id": "929c04cf.3f9d98",
        "type": "http response",
        "z": "a7e499b8.5a5148",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 860,
        "y": 300,
        "wires": []
    }
]