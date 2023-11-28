//#define DHTPIN @@@  // 온습도 핀 번호
//#define DHTTYPE @@@    // 센서 (DHT11)
#define MQ5pin 3 // 가스센서 핀 번호
#define MQ7pin 5 // 가스센서 핀 번호


//DHT dht(DHTPIN, DHTTYPE)

int chk;
float mq5;    // 가스 센서
float mq7;    // 가스 센서
float hum;    // 습도
float temp;   // 온도


void setup() {
  Serial.begin(9600);
  // dht.begin();

}

void loop() {
  
  delay(3000);

/*hum = dht.readHumidity();
  temp = dht.readTemperature();       //온습도 인식값
 
  Serial.print("습도 인식값 : ");  //라즈베리파이에서 온도,습도,가스 센서 종류 구분
  Serial.println("hum");

  Serial.print("온도 인식값 : ");  
  Serial.println("temp");  */

  mq5 = analogRead(MQ5pin);       // 가스센서 인식값
  mq7 = analogRead(MQ7pin); 

  Serial.print("mq5:");   
  Serial.println(mq5);
  Serial.print("mq7:");   
  Serial.println(mq7);

  // 시리얼모니터의 값을 라즈베리파이에서 줄별로 읽고 센서 종류를 구분하여 인식값을 받아 웹소켓으로 전달 -

}
