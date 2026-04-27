#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

unsigned long last_time = 0;
const unsigned long interval = 10000; // 10000微秒 = 10毫秒 (100Hz)

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10); 

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) { delay(10); }
  }

  
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ); 
}

void loop() {
  unsigned long current_time = micros();
  //阻塞出发
  if (current_time - last_time >= interval) {
    last_time = current_time; // 重置计时器

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    // 计算简易 pitch 角 
    float pitch = atan2(a.acceleration.x, sqrt(a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z)) * 180.0 / PI;

    // 输出格式：时间戳(微秒),pitch角
    Serial.printf("%lu,%.2f\n", current_time, pitch);
  }
}