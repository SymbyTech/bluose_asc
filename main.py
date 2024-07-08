from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading
import json
import time
from pydantic import BaseModel
from Stack import Stack

app = FastAPI()
stack = Stack()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define data model
class LEDToggle(BaseModel):
    led_num: int
    state: int

def sensor_data():   
    global stack
    while True:
        # stack.get_current_sensor_data() returns all the current sensor values
        # stack.get_bme_data() returns all the BME280 data
        retv = json.dumps({'current':stack.get_current_sensor_data()})
        time.sleep(1)
        print({"success": True,'sensordata': retv})

sensor_thread = threading.Thread(target=sensor_data)
sensor_thread.daemon = True
sensor_thread.start()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.post("/led_toggle")
def handle_led_toggle(data: LEDToggle):
    led_num = data.led_num
    state = data.state
    # led_num points to each individual LED
    # LED state 1 or 0 (for on or off)
    # LED_BOARD points to the board where the LEDs are connected to
    LED_BOARD = 1
    stack.switch(LED_BOARD, led_num+1, state)
    return {"success": True, "message": f"LED Channel {led_num} toggled to {state}"}

@app.get("/sensor_data")
def get_sensor_data():
    global stack
    # stack.get_current_sensor_data() returns all the current sensor values
    # stack.get_bme_data() returns all the BME280 data
    retv = json.dumps({'current':stack.get_current_sensor_data()})
    return {"success": True,'sensordata': retv}
