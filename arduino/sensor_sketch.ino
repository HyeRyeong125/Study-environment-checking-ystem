// EcoMind - Arduino Sensor Data Collection Sketch
// Arduino Uno with HC-SR04, Light Sensor, Vibration Sensor, Microphone
// Sends sensor data via USB Serial in JSON format

// Pin Definitions
#define ULTRASONIC_TRIG 7
#define ULTRASONIC_ECHO 8
#define LIGHT_SENSOR A0
#define VIBRATION_SENSOR A1
#define MICROPHONE_SENSOR A2

// Variables for ultrasonic sensor
long duration;
int distance;

// Timing for sensor readings
unsigned long lastReadTime = 0;
const unsigned long READ_INTERVAL = 1000; // Read sensors every 1 second

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud

  // Set pin modes
  pinMode(ULTRASONIC_TRIG, OUTPUT);
  pinMode(ULTRASONIC_ECHO, INPUT);
  pinMode(LIGHT_SENSOR, INPUT);
  pinMode(VIBRATION_SENSOR, INPUT);
  pinMode(MICROPHONE_SENSOR, INPUT);

  // Wait for serial to be ready
  delay(1000);
  Serial.println("{\"status\": \"Arduino Uno initialized\"}");
}

void loop() {
  // Read sensors at specified interval
  if (millis() - lastReadTime >= READ_INTERVAL) {
    lastReadTime = millis();

    // Collect sensor data
    int lightValue = readLightSensor();
    int vibrationValue = readVibrationSensor();
    int microphoneValue = readMicrophone();
    int distanceValue = readUltrasonic();

    // Send JSON formatted data via Serial
    sendSensorData(lightValue, vibrationValue, microphoneValue, distanceValue);
  }
}

// Read light sensor (Photoresistor / PWD-LED)
// Returns analog value (0-1023)
int readLightSensor() {
  return analogRead(LIGHT_SENSOR);
}

// Read vibration sensor (HW-072)
// Returns analog value (0-1023)
int readVibrationSensor() {
  return analogRead(VIBRATION_SENSOR);
}

// Read microphone sensor
// Returns analog value (0-1023)
int readMicrophone() {
  return analogRead(MICROPHONE_SENSOR);
}

// Read ultrasonic sensor (HC-SR04)
// Returns distance in centimeters
int readUltrasonic() {
  // Send pulse to trigger pin
  digitalWrite(ULTRASONIC_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(ULTRASONIC_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(ULTRASONIC_TRIG, LOW);

  // Measure echo pulse duration
  duration = pulseIn(ULTRASONIC_ECHO, HIGH, 30000);

  // Calculate distance (speed of sound = 340 m/s)
  // Distance = duration * 340 / 2 / 10000 (in cm)
  distance = (duration * 0.034) / 2;

  // Return distance or -1 if out of range
  return (distance > 2 && distance < 400) ? distance : -1;
}

// Send sensor data in JSON format via Serial
void sendSensorData(int light, int vibration, int microphone, int distance) {
  String jsonData = "{";
  jsonData += "\"timestamp\": " + String(millis()) + ", ";
  jsonData += "\"light_sensor\": {";
  jsonData += "\"illuminance\": " + String(light) + ", ";
  jsonData += "\"raw_value\": " + String(light);
  jsonData += "}, ";

  jsonData += "\"vibration_sensor\": {";
  jsonData += "\"detected\": " + String(vibration > 500 ? "true" : "false") + ", ";
  jsonData += "\"raw_value\": " + String(vibration);
  jsonData += "}, ";

  jsonData += "\"microphone_sensor\": {";
  // Simple noise level estimation (0-100 scale)
  int noiseLevel = map(microphone, 0, 1023, 0, 100);
  jsonData += "\"noise_level\": " + String(noiseLevel) + ", ";
  jsonData += "\"raw_value\": " + String(microphone);
  jsonData += "}, ";

  jsonData += "\"ultrasonic_sensor\": {";
  jsonData += "\"distance\": " + String(distance) + ", ";
  jsonData += "\"posture\": \"" + (distance > 0 && distance < 30 ? "warning" : "good") + "\"";
  jsonData += "}";
  jsonData += "}";

  Serial.println(jsonData);
}
