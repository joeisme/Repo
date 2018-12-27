[
    {
        "id": "b8404ff8.e9b95",
        "type": "tab",
        "label": "¬yµ{4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "1d999963.edbcf7",
        "type": "http in",
        "z": "b8404ff8.e9b95",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 80,
        "y": 120,
        "wires": [
            [
                "fe38978a.37bc78",
                "7a018ef4.e58ac"
            ]
        ]
    },
    {
        "id": "fe38978a.37bc78",
        "type": "function",
        "z": "b8404ff8.e9b95",
        "name": "Set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 230,
        "y": 120,
        "wires": [
            [
                "6c005286.f9f75c"
            ]
        ]
    },
    {
        "id": "6c005286.f9f75c",
        "type": "rpi-gpio out",
        "z": "b8404ff8.e9b95",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 470,
        "y": 140,
        "wires": []
    },
    {
        "id": "7a018ef4.e58ac",
        "type": "function",
        "z": "b8404ff8.e9b95",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 260,
        "y": 220,
        "wires": [
            [
                "825cabd1.878af8",
                "5e08b808.146678"
            ]
        ]
    },
    {
        "id": "825cabd1.878af8",
        "type": "http response",
        "z": "b8404ff8.e9b95",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 610,
        "y": 300,
        "wires": []
    },
    {
        "id": "5e08b808.146678",
        "type": "debug",
        "z": "b8404ff8.e9b95",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 480,
        "y": 440,
        "wires": []
    },
    {
        "id": "1424cf35.556d01",
        "type": "http in",
        "z": "b8404ff8.e9b95",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 70,
        "y": 340,
        "wires": [
            [
                "6d354601.7911d8",
                "76af3c52.e14e34"
            ]
        ]
    },
    {
        "id": "6d354601.7911d8",
        "type": "function",
        "z": "b8404ff8.e9b95",
        "name": "clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 220,
        "y": 340,
        "wires": [
            [
                "6c005286.f9f75c"
            ]
        ]
    },
    {
        "id": "76af3c52.e14e34",
        "type": "function",
        "z": "b8404ff8.e9b95",
        "name": "Return Status",
        "func": "msg.payload = \"GPIOS set to LOW\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 250,
        "y": 460,
        "wires": [
            [
                "825cabd1.878af8",
                "5e08b808.146678"
            ]
        ]
    }
]