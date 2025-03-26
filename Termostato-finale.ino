

#include "DHT.h"

#define DHTPIN 3    // Digital pin connected to the DHT sensor

// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --

// Pin 15 can work but DHT must be disconnected during program upload.

// Uncomment whatever type you're using!

#define DHTTYPE DHT11   // DHT 11

//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V

// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1

// to 3.3V instead of 5V!

// Connect pin 2 of the sensor to whatever your DHTPIN is

// Connect pin 4 (on the right) of the sensor to GROUND

// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.

// Note that older versions of this library took an optional third parameter to

// tweak the timings for faster processors.  This parameter is no longer needed

// as the current DHT reading algorithm adjusts itself to work on faster procs.

DHT dht(DHTPIN, DHTTYPE);

int rele=10;

void setup() {

  Serial.begin(9600);

  Serial.println(F("DHT11!"));

  dht.begin();

  Serial.begin(9600);

  pinMode(rele, OUTPUT);

}

void loop() {

  // Wait a few seconds between measurements.


  delay(1000);

  // Reading temperature or humidity takes about 250 milliseconds!

  // Read temperature as Celsius (the default)

  float t = dht.readTemperature();
 


  // Check if any reads failed and exit early (to try again).

  if ( isnan(t)) {

    Serial.println(F("Failed to read from DHT sensor!"));

    return;

  }

 
  Serial.print(t);

  Serial.print(F("°C "));

  if(t>=25){

    digitalWrite(rele, HIGH) 

  }else{

    digitalWrite(rele, LOW)

  }


}
 