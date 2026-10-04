from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Device(BaseModel):
    name: str
    room: str
    temp: float
    online: bool


readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


@app.get("/devices")
def get_devices():
    return readings


@app.get("/devices/{name}")
def get_device(name: str):
    for device in readings:
        if device["name"] == name:
            return device
    raise HTTPException(status_code=404, detail="No device called " + name)


@app.post("/devices", status_code=201)
def create_device(device: Device):
    new_device = device.model_dump()
    readings.append(new_device)
    return new_device


@app.put("/devices/{name}")                 #task 1: update device
def update_device(name: str, device: Device):
    for i, existing in enumerate(readings):
        if existing["name"] == name:
            readings[i] = device.model_dump()
            return readings[i]
    raise HTTPException(status_code=404, detail="No device called " + name)
