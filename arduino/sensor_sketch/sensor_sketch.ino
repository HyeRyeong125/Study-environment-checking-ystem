#define ULTRASONIC_TRIG 7
#define ULTRASONIC_ECHO 8
#define LIGHT_SENSOR A0
#define VIBRATION_SENSOR A1
#define MICROPHONE_SENSOR A2

long duration;
int distance;
unsigned long lastReadTime = 0;
const unsigned long READ_INTERVAL = 1000;

void setup() {
  Serial.begin(9600);
  pinMode(ULTRASONIC_TRIG, OUTPUT);
  pinMode(ULTRASONIC_ECHO, INPUT);
  pinMode(LIGHT_SENSOR, INPUT);
  pinMode(VIBRATION_SENSOR, INPUT);
  pinMode(MICROPHONE_SENSOR, INPUT);
  delay(1000);
  Serial.println("{\"status\": \"initialized\"}");
}

void loop() {
  if (millis() - lastReadTime >= READ_INTERVAL) {
    lastReadTime = millis();
    int light = analogRead(LIGHT_SENSOR);
    int vibration = analogRead(VIBRATION_SENSOR);
    int microphone = analogRead(MICROPHONE_SENSOR);
    int dist = getUltrasonic();
    sendJSON(light, vibration, microphone, dist);
  }
}

int getUltrasonic() {
  digitalWrite(ULTRASONIC_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(ULTRASONIC_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(ULTRASONIC_TRIG, LOW);
  duration = pulseIn(ULTRASONIC_ECHO, HIGH, 30000);
  distance = (duration * 0.034) / 2;

  // 디버깅: duration이 0이면 센서 미연결
  if (duration == 0) {
    Serial.println("{\"debug\": \"초음파 센서 미응답 - 센서 연결 확인 필요\"}");
    return -1;
  }

  return (distance > 2 && distance < 400) ? distance : -1;
}

void sendJSON(int light, int vibration, int microphone, int dist) {
  Serial.print("{\"light\":");
  Serial.print(light);
  Serial.print(",\"vibration\":");
  Serial.print(vibration);
  Serial.print(",\"microphone\":");
  Serial.print(microphone);
  Serial.print(",\"distance\":");
  Serial.print(dist);
  Serial.println("}");
}
