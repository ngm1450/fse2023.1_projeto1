from flask import Flask, request, jsonify
from threading import Thread
import RPi.GPIO as GPIO
import time
import random

app = Flask(__name__)

# Global variables
sensor_pins = [14, 15, 18, 23, 24, 25, 8, 7]
button_pins = [17, 27, 22, 10, 9, 11, 5, 6]
led_pin = 12
pass_sensor_1_pin = 16
pass_sensor_2_pin = 20
floor = None
vacancy = None
total_paid = 0

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pins, GPIO.IN)
GPIO.setup(button_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pass_sensor_1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pass_sensor_2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

# Helper functions
def get_vacancy():
    for i, pin in enumerate(sensor_pins):
        if GPIO.input(pin) == GPIO.LOW:
            return i
    return None

def update_led():
    GPIO.output(led_pin, GPIO.HIGH if get_vacancy() is None else GPIO.LOW)

def start_thread(func):
    thread = Thread(target=func)
    thread.daemon = True
    thread.start()

# Flask routes
@app.route('/')
def index():
    return 'Parking control system'

@app.route('/floor', methods=['GET'])
def get_floor():
    return jsonify({'floor': floor})

@app.route('/floor', methods=['POST'])
def set_floor():
    global floor
    floor = request.json['floor']
    return jsonify({'floor': floor})

@app.route('/vacancy', methods=['GET'])
def get_vacancy():
    return jsonify({'vacancy': vacancy})

@app.route('/vacancy', methods=['POST'])
def set_vacancy():
    global vacancy
    vacancy = request.json['vacancy']
    return jsonify({'vacancy': vacancy})

@app.route('/payment', methods=['POST'])
def make_payment():
    global total_paid
    duration = request.json['duration']
    rate_per_hour = 5  # Set the rate per hour here
    payment = duration * rate_per_hour  # Calculate payment
    total_paid += payment
    return jsonify({'payment': payment})

@app.route('/total_payment', methods=['GET'])
def get_total_payment():
    return jsonify({'total_payment': total_paid})

# Main control loop
def control_loop():
    global floor, vacancy
    
    while True:
        if floor is not None and vacancy is None:
            vacancy = get_vacancy()
            if vacancy is not None:
                print(f'Car parked on floor {floor}, vacancy {vacancy}')
                update_led()

        if floor is not None and vacancy is not None:
            if GPIO.input(button_pins[vacancy]) == GPIO.LOW:
                print(f'Car in vacancy {vacancy} on floor {floor} is leaving')
                # Generate a random duration for demonstration
                duration = random.randint(1, 10)
                response = requests.post('http://localhost:5000/payment', json={'duration': duration})
                payment = response.json()['payment']
                print(f'Payment: {payment}')
                vacancy = None
                update_led()
                time.sleep(1)

        if GPIO.input(pass_sensor_1_pin) == GPIO.HIGH:
            print
