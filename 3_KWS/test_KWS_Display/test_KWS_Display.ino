
/* Includes ---------------------------------------------------------------- */
#include <Arduino.h>
#include <U8x8lib.h>
#include <Wire.h>

#define NUMBER_CLASSES 3

/** OLED */
U8X8_SSD1306_128X64_NONAME_HW_I2C oled(PIN_WIRE_SCL, PIN_WIRE_SDA, U8X8_PIN_NONE);  

int pred_index = 0;     
float pred_value = 0; 
String lbl = " ";


void setup() {
    pinMode(LEDR, OUTPUT);
    pinMode(LEDG, OUTPUT);
    pinMode(LEDB, OUTPUT);
    
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
    
    oled.begin();
    oled.setFlipMode(2);
    oled.setFont(u8x8_font_chroma48medium8_r);
    oled.setCursor(0, 0);
    oled.print(" XIAO Sense KWS");
}

/**
 * @brief      turn_off_leds function - turn-off all RGB LEDs
 */
void turn_off_leds(){
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
}

/**
 * @brief      Show Inference Results on OLED Display
 */
void display_oled(int pred_index, float pred_value){
  switch (pred_index){
    case 0:
      turn_off_leds();
      digitalWrite(LEDG, LOW);
      lbl = "IESTI  " ;
      break;

    case 1:
      turn_off_leds();
      lbl = "SILENCE";
      break;
    
    case 2:
      turn_off_leds();
      digitalWrite(LEDR, LOW);
      lbl = "UNIFEI ";
      break;
  }
    oled.setCursor(0, 2);
    oled.print("      ");
    oled.setCursor(2, 4);
    oled.print("Label:");
    oled.print(lbl);
    oled.setCursor(2, 6);
    oled.print("Prob.:");
    oled.print(pred_value);
}

void loop() {
    for (int i = 0; i < NUMBER_CLASSES; i++) { 
      pred_index = i;     
      pred_value = 0.8;   
      display_oled(pred_index, pred_value);
      delay(2000);
    }

}
