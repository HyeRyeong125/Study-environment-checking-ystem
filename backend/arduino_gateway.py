#!/usr/bin/env python3
"""
Arduino Serial to MQTT Gateway
Reads sensor data from Arduino Uno via USB Serial and publishes to MQTT broker
"""

import serial
import json
import time
import sys
from datetime import datetime
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

# Configuration
SERIAL_PORT = os.getenv('ARDUINO_SERIAL_PORT', '/dev/cu.usbserial-140')
SERIAL_BAUD = int(os.getenv('ARDUINO_BAUD_RATE', 9600))
MQTT_BROKER = os.getenv('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
MQTT_USERNAME = os.getenv('MQTT_USERNAME', None)
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD', None)

# MQTT Topics
TOPICS = {
    'light': 'home/sensors/light',
    'vibration': 'home/sensors/motion',
    'microphone': 'home/sensors/motion',
    'ultrasonic': 'home/sensors/ultrasonic'
}


class ArduinoGateway:
    def __init__(self):
        self.ser = None
        self.mqtt_client = None
        self.connected = False

    def connect_serial(self):
        """Connect to Arduino via Serial"""
        try:
            print(f"⏳ Attempting to connect to Arduino on {SERIAL_PORT}...")
            self.ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
            print(f"✓ Serial port opened")
            time.sleep(2)  # Wait for Arduino to initialize
            print(f"✓ Connected to Arduino on {SERIAL_PORT}")
            return True
        except serial.SerialException as e:
            print(f"✗ Serial connection failed: {e}")
            print(f"✗ Port {SERIAL_PORT} might be in use or not available")
            return False
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            return False

    def connect_mqtt(self):
        """Connect to MQTT Broker"""
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_disconnect = self.on_mqtt_disconnect
        self.mqtt_client.on_publish = self.on_mqtt_publish

        try:
            if MQTT_USERNAME and MQTT_PASSWORD:
                self.mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

            self.mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
            self.mqtt_client.loop_start()
            return True
        except Exception as e:
            print(f"✗ MQTT connection failed: {e}")
            return False

    def on_mqtt_connect(self, client, userdata, flags, rc):
        """Callback for MQTT connection"""
        if rc == 0:
            print(f"✓ Connected to MQTT broker ({MQTT_BROKER}:{MQTT_PORT})")
            self.connected = True
        else:
            print(f"✗ MQTT connection failed with code {rc}")
            self.connected = False

    def on_mqtt_disconnect(self, client, userdata, rc):
        """Callback for MQTT disconnection"""
        print(f"✗ Disconnected from MQTT (code: {rc})")
        self.connected = False

    def on_mqtt_publish(self, client, userdata, mid):
        """Callback for MQTT publish"""
        pass

    def publish_sensor_data(self, data):
        """Parse Arduino JSON and publish to MQTT topics"""
        try:
            # Parse JSON from Arduino
            raw_data = json.loads(data)

            timestamp = datetime.now().isoformat()

            # Transform Arduino data to standard format
            # 초음파 센서 테스트 값 (임시)
            test_distance = 32 if raw_data.get('distance', -1) == -1 else raw_data.get('distance', -1)

            sensor_data = {
                'light_sensor': {
                    'illuminance': raw_data.get('light', 0),
                    'raw_value': raw_data.get('light', 0)
                },
                'motion_sensor': {
                    'noise_level': raw_data.get('vibration', 0),
                    'raw_value': raw_data.get('vibration', 0)
                },
                'microphone_sensor': {
                    'noise_level': raw_data.get('microphone', 0),
                    'raw_value': raw_data.get('microphone', 0)
                },
                'ultrasonic_sensor': {
                    'distance': test_distance,
                    'posture': 'warning' if test_distance < 25 else 'good' if test_distance > 0 else 'unknown'
                }
            }

            # Publish light sensor data
            light_payload = {
                'timestamp': timestamp,
                'illuminance': sensor_data['light_sensor']['illuminance'],
                'raw_value': sensor_data['light_sensor']['raw_value']
            }
            self.mqtt_client.publish(
                TOPICS['light'],
                json.dumps(light_payload),
                qos=1
            )
            print(f"📡 Light: {light_payload['illuminance']}")

            # Publish vibration/motion sensor data
            vibration_payload = {
                'timestamp': timestamp,
                'detected': sensor_data['motion_sensor']['noise_level'] > 100,
                'raw_value': sensor_data['motion_sensor']['raw_value']
            }
            self.mqtt_client.publish(
                TOPICS['vibration'],
                json.dumps(vibration_payload),
                qos=1
            )

            # Publish microphone/noise data
            microphone_payload = {
                'timestamp': timestamp,
                'noise_level': sensor_data['microphone_sensor']['noise_level'],
                'raw_value': sensor_data['microphone_sensor']['raw_value']
            }
            self.mqtt_client.publish(
                TOPICS['microphone'],
                json.dumps(microphone_payload),
                qos=1
            )
            print(f"🔊 Noise: {microphone_payload['noise_level']}")

            # Publish ultrasonic sensor data
            ultrasonic_payload = {
                'timestamp': timestamp,
                'distance': sensor_data['ultrasonic_sensor']['distance'],
                'posture': sensor_data['ultrasonic_sensor']['posture']
            }
            self.mqtt_client.publish(
                TOPICS['ultrasonic'],
                json.dumps(ultrasonic_payload),
                qos=1
            )
            distance = ultrasonic_payload['distance']
            if distance > 0:
                print(f"📏 Distance: {distance}cm - Posture: {ultrasonic_payload['posture']}")

        except json.JSONDecodeError as e:
            print(f"✗ JSON decode error: {e}")
        except Exception as e:
            print(f"✗ Error publishing sensor data: {e}")

    def run(self):
        """Main loop - read from Serial and publish to MQTT"""
        if not self.connect_serial():
            return False

        if not self.connect_mqtt():
            return False

        print("\n🚀 Arduino Gateway running... (Press Ctrl+C to exit)\n")
        print("⏳ Waiting for sensor data...\n")

        data_received = False
        try:
            while True:
                if self.ser and self.ser.in_waiting:
                    try:
                        line = self.ser.readline().decode('utf-8').strip()
                        if line:
                            if not data_received:
                                print(f"✓ First data received!\n")
                                data_received = True
                            print(f"📨 Raw data: {line}")
                            self.publish_sensor_data(line)
                    except UnicodeDecodeError as e:
                        print(f"✗ Decode error: {e}")
                    except Exception as e:
                        print(f"✗ Error: {e}")

                time.sleep(0.1)

        except KeyboardInterrupt:
            print("\n\n👋 Shutting down...")
        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up resources"""
        if self.ser:
            self.ser.close()
            print("Serial connection closed")

        if self.mqtt_client:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            print("MQTT disconnected")


def main():
    gateway = ArduinoGateway()
    gateway.run()


if __name__ == '__main__':
    main()
