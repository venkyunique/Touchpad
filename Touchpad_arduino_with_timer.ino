#include "OneButton.h"

#define bt_start  10
#define bt_stop1   9
#define bt_stop2   8
#define bt_reset   7


OneButton button1(bt_stop1, true); // lane1
OneButton button2(bt_stop2, true); // lane2
OneButton button3(bt_reset, true); // lane2
OneButton button4(bt_start, true); // lane2


int hh = 0, mm = 0, ss = 0, ms = 0;
bool timerStart = false;

int FINISH = 1;

int finish_swim = 0;

int pos = 1;

int arr[8];
int swimmers = 2;
int ptr = 0;

struct lane1{
  String name1;
  int hh1;
  int mm1;
  int ss1;
  int ms1;
  int lap1;
};

struct lane2{
  String name2;
  int hh2;
  int mm2;
  int ss2;
  int ms2; 
  int lap2;
};

lane1 a = {"Anshu",0,0,0,0,0};
lane2 b = {"Sonu",0,0,0,0,0};

void setup() { // put your setup code here, to run once
  Serial.begin(19200);
  
  button1.attachClick(singleclick1);
  button2.attachClick(singleclick2);
  button3.attachClick(stopnreset);
  button4.attachClick(start);

  
  pinMode(bt_start, INPUT_PULLUP);
  pinMode(bt_stop1,  INPUT_PULLUP);
  pinMode(bt_stop2,  INPUT_PULLUP);
  pinMode(bt_reset, INPUT_PULLUP);
//  pinMode(led_g , OUTPUT);
//  pinMode(led_r , OUTPUT);

  

  noInterrupts();         // disable all interrupts
  TCCR1A = 0;             // set entire TCCR1A register to 0  //set timer1 interrupt at 1kHz  // 1 ms
  TCCR1B = 0;             // same for TCCR1B
  TCNT1  = 0;             // set timer count for 1khz increments
  OCR1A = 1999;           // = (16*10^6) / (1000*8) - 1
  //had to use 16 bit timer1 for this bc 1999>255, but could switch to timers 0 or 2 with larger prescaler
  TCCR1B |= (1 << WGM12); // turn on CTC mode
  TCCR1B |= (1 << CS11);  // Set CS11 bit for 8 prescaler
  TIMSK1 |= (1 << OCIE1A);// enable timer compare interrupt
  interrupts();           // enable

}

void loop() {
  button1.tick();
  button2.tick();
  button3.tick();
  button4.tick();
  
  if(finish_swim == 2)
  {
    timerStart = false;
    Serial.print("$ DONE");
    delay(10000000);
  }

  Serial.print("# ");
//  Serial.print((hh / 10) % 10);
//  Serial.print(hh % 10);
//  Serial.print(":");
  Serial.print((mm / 10) % 10);
  Serial.print(mm % 10);
  Serial.print(":");
  Serial.print((ss / 10) % 10);
  Serial.print(ss % 10);
  Serial.print(":");
  Serial.print((ms / 100) % 10);
  Serial.print((ms / 10) % 10);
  Serial.println(ms % 10); 
  

}

void singleclick1()
{
//  if (a.lap1 == (FINISH-1)) {
      a.hh1 = hh;
      a.mm1 = mm;
      a.ss1 = ss;
      a.ms1 = ms;

//      Serial.println("@ 1 "+((a.mm1 / 10) % 10)+(a.mm1 % 10) + ":" +(a.ss1 / 10) % 10+a.ss1 % 10+":"+(a.ms1 / 100) % 10+(a.ms1 / 10) % 10+a.ms1 % 10+" "+pos);
      char buff[20];
        sprintf(buff,"@ 1 %d%d:%d%d:%d%d%d %d\n",(a.mm1 / 10) % 10,a.mm1 % 10,(a.ss1 / 10) % 10,a.ss1 % 10,(a.ms1 / 100) % 10,(a.ms1 / 10) % 10,a.ms1 % 10,pos);
        Serial.print(buff);
      finish_swim = finish_swim + 1;
      pos= pos + 1;
//    }
//    a.lap1 = a.lap1 + 1;
  
}

void singleclick2()
{
//  if (b.lap2  == (FINISH-1)) {
      b.hh2 = hh;
      b.mm2 = mm;
      b.ss2 = ss;
      b.ms2 = ms;
      char buff1[20];
      sprintf(buff1,"@ 2 %d%d:%d%d:%d%d%d %d\n",(b.mm2 / 10) % 10,b.mm2 % 10,(b.ss2 / 10) % 10,b.ss2 % 10,(b.ms2 / 100) % 10,(b.ms2 / 10) % 10,b.ms2 % 10,pos);
      Serial.print(buff1);
      pos= pos + 1;
      finish_swim = finish_swim + 1;
     
//    }
//     b.lap2 = b.lap2 + 1;
}

void stopnreset()
{
  timerStart = false;
  ms = 0, ss = 0, mm = 0, hh = 0; // Reset stopwatch
} 

void start(){
  timerStart = true;
}

ISR(TIMER1_COMPA_vect) {
  if (timerStart == true) {
    ms = ms + 1;
    if (ms > 999) {
      ms = 0;
      ss = ss + 1;
      if (ss > 59) {
        ss = 0;
        mm = mm + 1;
      }
      if (mm > 59) {
        mm = 0;
        hh = hh + 1;
      }
    }
  }
}
