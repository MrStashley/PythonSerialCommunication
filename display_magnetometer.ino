#include <Arduino_LSM9DS1.h>

const int X = 0, Y = 1, Z = 2;
float m[3] = {0,0,0};
float magBias[3] = {38.63278,-1.660625+25,-.2446365};

void setup() {
  Serial.begin(9600);
  IMU.begin();
  // put your setup code here, to run once:

}

void loop() {
  if(IMU.magneticFieldAvailable()){
    IMU.readMagneticField(m[X],m[Y],m[Z]);
      m[X] = (m[X] - magBias[X]); //* magScale[X];
      m[Y] = (m[Y] - magBias[Y]); //* magScale[Y];
      m[Z] = (m[Z] - magBias[Z]); // * magScale[Z];

      m[X] = -m[X];
      m[Y] = m[Y];
      m[Z] = m[Z];
      Serial.print(m[X]);
      Serial.print(" ");
      Serial.print(m[Y]);
      Serial.print(" ");
      Serial.print(m[Z]);
      Serial.println();
  }
}
