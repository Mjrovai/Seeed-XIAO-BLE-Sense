/*
  Data Forwarder - Built-in IMU (Accelerometer) on the XIAO BLE Sense
  Based on Edge Impulse Example
  https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-data-forwarder

  Requires the Seeed Arduino LSM9DS1 library 
  https://github.com/Seeed-Studio/Seeed_Arduino_LSM6DS3/

  Marcelo Rovai @July2022
*/

#include "LSM6DS3.h"
#include "Wire.h"

//Create an instance of class LSM6DS3
LSM6DS3 xIMU(I2C_MODE, 0x6A);    //I2C device address 0x6A

#define CONVERT_G_TO_MS2    9.80665f
#define FREQUENCY_HZ        50
#define INTERVAL_MS         (1000 / (FREQUENCY_HZ + 1))

static unsigned long last_interval_ms = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // configure the IMU
  if (xIMU.begin() != 0) {
      Serial.println("Device error");
  } else {
      Serial.println("Device OK!");
  }

  Serial.println("Data Forwarder - Built-in IMU (Accelerometer) on the XIAO BLE Sense\n");
}

void loop() {
    float x, y, z;

    if (millis() > last_interval_ms + INTERVAL_MS) {
        last_interval_ms = millis();

        x = xIMU.readFloatAccelX();
        y = xIMU.readFloatAccelY();
        z = xIMU.readFloatAccelZ();

        Serial.print(x * CONVERT_G_TO_MS2);
        Serial.print('\t');
        Serial.print(y * CONVERT_G_TO_MS2);
        Serial.print('\t');
        Serial.println(z * CONVERT_G_TO_MS2);
    }
}
