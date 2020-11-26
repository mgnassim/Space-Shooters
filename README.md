# Space Shooters

### Ontwikkelaars
*Butros Groot, Riyad Ljeljak, Sirito Mathijssen, Giorgio, Bilal
Malik, Nassim Mengat*

## Wat is Space Shooters?
**Space Shooters** is gebaseerd op het oude en hele bekende space invaders.
Bij onze versie is het in real life in plaats van op zo’n oude arcadekast.
Bij het begin van het spel krijg je een geweer die laser schiet.
Met dat geweer moet je zo snel mogelijk de tien doelwitten voor je afschieten.
Hoe sneller je het doet hoe hoger je score is.


## Hoe werkt het spel
### Hoe start je het spel
Het spel start je door eerst met QR code te scannen deze leidt je
naar de website hier wordt gevraagd om het pasje te scannen (waarin
de RFID sensor zit) dit pasje geeft toegang tot het spel. hierna
wordt er gevraagd om een nickname in tevoren zodra dit is gebeurd
druk je op start, en gaan alle targets omhoog en begint het spel.

### High scores
Om competitie in het spel te krijgen link je je nickname met een
score. Deze score wordt bepaalt door de snelheid waarmee je het spel
eindigt. Dit wordt vervolgens geupload op de website. Dat wordt dan
bijgehouden en hier staan dan de top mensen die het hoogst hebben gescoord. 

### Hoe eindigt het spel
Het spel kan eindigen door alle targets geraakt te hebben of door
een geforceerde exit door een stop button op de website die laat
weten aan de raspberry pi's dat ze alle targets naar boven moeten
brengen die zijn neergeschoten en het spel moet resetten.

## Onderdelen
### onderdelen lijst
#### Sensoren
* [Laser Ontvanger Module](https://nl.banggood.com/Laser-Receiver-Module-Non-modulator-Tube-Laser-Sensor-Module-p-915633.html?rmmds=detail-top-buytogether-auto&cur_warehouse=CN)
* [HC-SR04](https://www.kiwi-electronics.nl/ultrasonic-sensor-hc-sr04)
* [RFID sensor](https://www.amazon.nl/BUYGOO-Reader-RFID-chip-Arduino-Raspberry/dp/B07D9C82W8/ref=asc_df_B07D9C82W8/?tag=nlshogostdde-21&linkCode=df0&hvadid=454717163742&hvpos=&hvnetw=g&hvrand=1142888669055717597&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1010543&hvtargid=pla-464388957750&psc=1)

#### Overige onderdelen
* [Servomotor](https://www.amazon.nl/AZDelivery-Micro-Servo-Helikopter-Vliegtuigen/dp/B07CZ42862/ref=asc_df_B07CZ42862/?tag=nlshogostdde-21&linkCode=df0&hvadid=430533579786&hvpos=&hvnetw=g&hvrand=7103477410555691880&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9064189&hvtargid=pla-828702003009&psc=1)
* [PWM](https://www.grandado.com/products/dc-6-v-12-v-24-v-28vdc-3a-80-w-pwm-motor-speed-controller-regulator-verstelbare-variabele-snelheidsregeling-met-potentiometer-switch?utm_campaign=&utm_content=&utm_source=Channable.beslist&utm_medium=8719896452153&utm_term=&variant=6367870779424&currency=EUR&bl3nlclid=1c1a3bf7-902d-4450-a0f6-3c3f88318398)
* [Laser pen](https://www.bol.com/nl/p/rode-laserpen-laserpointer-presenter/9200000096827660/?Referrer=ADVNLGOO002013-G-49170245275-S-382273935838-9200000096827660&gclid=Cj0KCQjw8fr7BRDSARIsAK0Qqr4wtriGnA7w05cbYwetCRWlzGTZG8IwYBKZRWvI1EnVb_BiWOHe3F8aAvjPEALw_wcB)

### L.O.M = Laser Ontvang Module
Deze sensor meet of dat het geraakt wordt door een **laserstraal**.
wanneer de sensor geraakt wordt geeft het een hoog signaal door
aan de raspberry pi. Dat signaal wordt verwerkt naar de beweging
van de servomotor bij de target.

### Ultrasoon sensor
De Ultrasoon sensor(HC-SR04) gebruiken we om te meten hoe ver de
speler van het spel af staat. Als de speler binnen 3 meter van het spel staat wordt het spel op stopgezet totdat je weer 3 meter van het spel af staat.

### RFID sensor
We gebruiken de RFID sensor(MFRC-522 RC522) voor het scannen van
de speel pas. die gescand moet worden voor het activeren van het
spel.

### Servo
De servomotoren worden gebruikt om de doelwitten om te laten
vallen wanneer ze zij geraakt en aan het einde van het spel weer rechtop te zetten.

