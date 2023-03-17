# Build Instructions and Notes

### Operating Principles

The core components in the build are the relay and microcontroller. The relay on the control board is an electromagnetic switch. Sending 5VDC to the relay energises the internal coil, mechanically switching its state from Normally-Open (NO) to a closed circuit $^*$. This process is automated using a programmable microcontroller which sends a 5VDC signal to the relay at specific times. All the circuitry has been placed within an enclosure to prevent access to the high AC voltages involved.

$^*$ _Note that the relay used in this build can also be wired for a Normally-Closed state if required (with lower current limits of 10A)._ 


## Bill of Materials

|Name               |QTY|Description                           |
|:------------------|:-:|:-------------------------------------|
|[Raspberry Pi](https://uk.farnell.com/raspberry-pi/rpi3-modbp/sbc-board-raspberry-pi-3-model/dp/2842228?src=raspberrypi)|1  |Raspberry Pi 3B+ single board computer. |
|[PCB HAT](https://www.adafruit.com/product/2310)|1  |Adafruit Perma-Proto HAT without EEPROM.|
|[Thermocouple Amplifier](https://www.adafruit.com/product/269)|3  |MAX31855 thermocouple amplifier board for Type-K thermocouples.|
|[Thermocouple connectors](https://uk.rs-online.com/web/p/sensor-accessories/8919031)|3  |For quick connection of thermocouples to datalogger.|
|[Thermocouple cable](https://uk.rs-online.com/web/p/thermocouple-extension-wire/2363959)|1  |Length depending on requirements.|
|Thermocouples|3  |Type-K thermocouples to suit the application.|
|Misc.|   | <ul><li>Wiring</li><li>Soldering Iron and solder</li><li>Small screwdriver</li></ul>|


## Wiring

### Thermocouple Amplifier to PCB HAT

To be added.

![Circuit schematic](./Images/TC-HAT-Schematic.png)

### Thermocouple connectors

To be added




## Python Codes

In progress. To be added.

The arduino code for uploading to the Arduino UNO microcontroller is located in `/Code/relay-switch.ino`. This contains a routine which turns the relay from the default open circuit (Normally-Open) to closed circuit where the outlet plug will be energised with AC from the source (in our case, single-phase 240VAC).

First, the signal pin is set as an output. Here, we use `LED_BUILTIN` as the signal pin which is pin 13 on the Arduino UNO.

```
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}
```

The remainder of the code involves setting up the time intervals and switching duration. These define how long the relay will switch `on` and `off` for (in milliseconds). And the switching duration is expressed by a total ON time `t` which is limited in the for loop to be less than a user-defined value (e.g., `t<1800000`). The relay is actuated by sending pin 13 `HIGH` (5VDC) and returned to NO by sending pin 13 `LOW`. In this example, the AC circuit is energised for 1 minute, turns off for 2 minutes, and will operate for a total ON time of 30 minutes. Once this target duration of 30 mins is reached, the loop exits and the relay returns to the default NO state permanently.   

```
void loop() {
  long on=60000;      
  long off=120000;    

  for (long t=0; t<1800000; t=t+on) {    
    digitalWrite(LED_BUILTIN, HIGH);    
    delay(on);                          
    digitalWrite(LED_BUILTIN, LOW);     
    delay(off);                         
    Serial.println(""); 
   }
  
  exit(0); 
```


