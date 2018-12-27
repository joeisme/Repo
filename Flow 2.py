[
    {
        "id": "c96f220f.93da8",
        "type": "tab",
        "label": "¬yµ{2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "85119f0d.45d62",
        "type": "inject",
        "z": "c96f220f.93da8",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 200,
        "y": 220,
        "wires": [
            [
                "9f486e7f.267b2"
            ]
        ]
    },
    {
        "id": "9f486e7f.267b2",
        "type": "function",
        "z": "c96f220f.93da8",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey:\"FtZyZYF7b0Ho8drT\"\n};\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 281,
        "wires": [
            [
                "8d0e2259.e3cf5",
                "f17fc00c.2a762"
            ]
        ]
    },
    {
        "id": "8d0e2259.e3cf5",
        "type": "http request",
        "z": "c96f220f.93da8",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DaqpJ9pk/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 640,
        "y": 200,
        "wires": [
            [
                "18bd9b09.0e42b5"
            ]
        ]
    },
    {
        "id": "f17fc00c.2a762",
        "type": "http request",
        "z": "c96f220f.93da8",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DaqpJ9pk/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 660,
        "y": 360,
        "wires": [
            [
                "3949ad93.b06a32"
            ]
        ]
    },
    {
        "id": "18bd9b09.0e42b5",
        "type": "debug",
        "z": "c96f220f.93da8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 850,
        "y": 220,
        "wires": []
    },
    {
        "id": "3949ad93.b06a32",
        "type": "debug",
        "z": "c96f220f.93da8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 870,
        "y": 500,
        "wires": []
    }
]