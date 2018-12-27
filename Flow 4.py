[
    {
        "id": "6f51670e.f072d8",
        "type": "tab",
        "label": "¬yµ{5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "37d908ce.40a8a8",
        "type": "http in",
        "z": "6f51670e.f072d8",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 90,
        "y": 200,
        "wires": [
            [
                "23c0bc47.cd9614"
            ]
        ]
    },
    {
        "id": "1e6d914a.a6a85f",
        "type": "rpi-gpio in",
        "z": "6f51670e.f072d8",
        "name": "GPIO4",
        "pin": "7",
        "intype": "tri",
        "debounce": "25",
        "read": false,
        "x": 120,
        "y": 320,
        "wires": [
            [
                "ee49be44.361cf"
            ]
        ]
    },
    {
        "id": "ee49be44.361cf",
        "type": "function",
        "z": "6f51670e.f072d8",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 320,
        "wires": [
            [
                "9b92a7bd.d49f48"
            ]
        ]
    },
    {
        "id": "23c0bc47.cd9614",
        "type": "function",
        "z": "6f51670e.f072d8",
        "name": "Get GPIO",
        "func": "msg.payload=global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 200,
        "wires": [
            [
                "5dcf4c8.0944cb4",
                "9b92a7bd.d49f48"
            ]
        ]
    },
    {
        "id": "5dcf4c8.0944cb4",
        "type": "http response",
        "z": "6f51670e.f072d8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 630,
        "y": 200,
        "wires": []
    },
    {
        "id": "9b92a7bd.d49f48",
        "type": "debug",
        "z": "6f51670e.f072d8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 670,
        "y": 320,
        "wires": []
    }
]