// variables
int GREEN = 2;
int RED = 3;
int DELAY_GREEN = 5000;
int DELAY_RED = 5000;
char serialData;

// basic functions
void setup()
{
  pinMode(GREEN, OUTPUT);
  pinMode(RED, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available() > 0)
  {
    serialData = Serial.read();
    Serial.print(serialData);
  }

  if(serialData == '1')
  {
    green_light();
    delay(DELAY_GREEN);
  }
  else if(serialData == '0')
  {
     red_light();
     delay(DELAY_RED);
  }
}

void green_light()
{
  digitalWrite(GREEN, HIGH);
  digitalWrite(RED, LOW);
}

void red_light()
{
  digitalWrite(GREEN, LOW);
  digitalWrite(RED, HIGH);
}
