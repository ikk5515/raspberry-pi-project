#include <MQUnifiedsensor.h>    //라이브러리 추가해야 함


#define placa "Arduino UNO"
#define Voltage_Resolution 5
#define pin 3   // 3
#define pin2 5   // 5 

#define type "MQ-5" 
#define type2 "MQ-7"

#define ADC_Bit_Resolution 10 
#define RatioMQ5CleanAir 6.5  
#define RatioMQ7CleanAir 27.5    // 깨끗한 공기의 기준 

float mq5_LPG;    
float mq7_CO;

MQUnifiedsensor MQ5(placa, Voltage_Resolution, ADC_Bit_Resolution, pin, type);
MQUnifiedsensor MQ7(placa, Voltage_Resolution, ADC_Bit_Resolution, pin2, type2);

void setup() {

  Serial.begin(9600); 



  MQ5.setRegressionMethod(1); 
  MQ5.setA(80.897); MQ5.setB(-2.431); //   LPG | 80.897 | -2.431

  MQ7.setRegressionMethod(1); 
  MQ7.setA(99.042); MQ7.setB(-1.518); //   CO | 99.042 | -1.518


  MQ5.init();   
  MQ7.init(); 


  float calcR0 = 0;
  float calcR1 = 0;
  for(int i = 1; i<=10; i ++)
  {
    MQ5.update(); 
    calcR0 += MQ5.calibrate(RatioMQ5CleanAir);

    MQ7.update(); 
    calcR1 += MQ7.calibrate(RatioMQ7CleanAir);


  }      
  MQ5.setR0(calcR0/10);
  MQ7.setR0(calcR1/10);      //calibrate가 10번씩 불필요하면 한 번만 


 // MQ5.serialDebug();
 // MQ7.serialDebug();
    //  Serial.print("calibrate 완료");
}

void loop() {

  MQ5.update(); 
  mq5_LPG = MQ5.readSensor(); 

  Serial.print("mq5:");   
  Serial.println(mq5_LPG);
 // Serial.println("ppm");

 // MQ5.serialDebug();    // 표시 안되면 

  MQ7.update(); 
  mq7_CO = MQ7.readSensor(); 

  //MQ7.serialDebug();    // 표시 안되면 

  Serial.print("mq7:");   
  Serial.println(mq7_CO);      
  //Serial.println("ppm");
  

  delay(3000); 

}
