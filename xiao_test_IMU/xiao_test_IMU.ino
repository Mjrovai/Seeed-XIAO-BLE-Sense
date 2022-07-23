/*
  IMU test for the built-in IMU on the XIAO BLE Sense
  Based on Harvard University tinyMLx - Sensor Test

  Requires the Seeed Arduino LSM9DS1 library 
  https://github.com/Seeed-Studio/Seeed_Arduino_LSM6DS3/

  Marcelo Rovai @July2022
*/

#include "LSM6DS3.h"
#include "Wire.h"

//Create an instance of class LSM6DS3
LSM6DS3 xIMU(I2C_MODE, 0x6A);    //I2C device address 0x6A

int imuIndex = 0; // 0 - accelerometer, 1 - gyroscope, 2 - thermometer
bool commandRecv = false; // flag used for indicating receipt of commands from serial port
bool startStream = false;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // configure the IMU
  if (xIMU.begin() != 0) {
      Serial.println("Device error");
  } else {
      Serial.println("Device OK!");
  }

  Serial.println("Welcome to the IMU test for the built-in IMU on the XIAO BLE Sense\n");
  Serial.println("Available commands:");
  Serial.println("a - display accelerometer readings in g's in x, y, and z directions");
  Serial.println("g - display gyroscope readings in deg/s in x, y, and z directions");
  Serial.println("t - display temperature readings in oC and oF");
}

void loop() {
  String command;

  // Read incoming commands from serial monitor
  while (Serial.available()) {
    char c = Serial.read();
    if ((c != '\n') && (c != '\r')) {
      command.concat(c);
    } 
    else if (c == '\r') {
      commandRecv = true;
      command.toLowerCase();
    }
  }

  // Command interpretation
  if (commandRecv) {
    commandRecv = false;
    if (command == "a") {
      imuIndex = 0;
      if (!startStream) {
        startStream = true;
      } 
      delay(3000);
    }
    else if (command == "g") {
      imuIndex = 1;
      if (!startStream) {
        startStream = true;
      }
      delay(3000);
    }
    else if (command == "t") {
      imuIndex = 2;
      if (!startStream) {
        startStream = true;
      }
      delay(3000);
    }
  }


  float x, y, z;
  if (startStream) {
    if (imuIndex == 0) { // testing accelerometer
      //Accelerometer
      x = xIMU.readFloatAccelX();
      y = xIMU.readFloatAccelY();
      z = xIMU.readFloatAccelZ();      
      Serial.print("\nAccelerometer:\n");
      Serial.print("Ax:");
      Serial.print(x);
      Serial.print(' ');
      Serial.print("Ay:");
      Serial.print(y);
      Serial.print(' ');
      Serial.print("Az:");
      Serial.println(z);
    }
    else if (imuIndex == 1) { // testing gyroscope
      //Gyroscope
      Serial.print("\nGyroscope:\n");
      x = xIMU.readFloatGyroX();
      y = xIMU.readFloatGyroY();
      z = xIMU.readFloatGyroZ();      
      Serial.print("wx:");
      Serial.print(x);
      Serial.print(' ');
      Serial.print("wy:");
      Serial.print(y);
      Serial.print(' ');
      Serial.print("wz:");
      Serial.println(z);
    }
    else if (imuIndex == 2) { // testing thermometer
       //Thermometer
      Serial.print("\nThermometer:\n");
      Serial.print(" Degrees oC = ");
      Serial.println(xIMU.readTempC(), 0);
      Serial.print(" Degrees oF = ");
      Serial.println(xIMU.readTempF(), 0);
      delay(1000);
    }
  }
}
