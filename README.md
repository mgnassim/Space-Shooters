# Space Shooters

## What is Space Shooters?
**Space Shooters** is based on the old and well known space invaders.
With our version it is in real life instead of on such an old arcade cabinet.
At the start of the game you get a gun that shoots laser.
With that rifle you have to shoot the ten targets in front of you as quickly as possible.
The faster you do it, the higher your score is.


## How does the game work
### How to start the game
You start the game by first scanning with QR code this will lead you
to the website here you will be asked to scan the pass (in which
the RFID sensor is located) this pass gives access to the game. after this
you will be asked for a nickname in advance once this is done
press start, and all targets go up and the game begins.

### High scores
To get competition into the game, link your nickname with a
score. This score is determined by the speed at which you play the game
ends. This is then uploaded to the website. That will be
tracked and here are the top people who have scored the highest.

### How does the game end
The game can end by hitting all targets or by
a forced exit by a stop button on the website that lets
know from the raspberry pis that they have to go up all the targets
that have been shot and the game must reset.

## Components
### parts list
#### Sensors
* [Laser Receiver Module](https://www.banggood.com/Laser-Receiver-Module-Non-modulator-Tube-Laser-Sensor-Module-p-915633.html?rmmds=detail-top-buytogether-auto&cur_warehouse =CN)
* [HC-SR04](https://www.kiwi-electronics.nl/ultrasonic-sensor-hc-sr04)
* [RFID sensor](https://www.amazon.nl/BUYGOO-Reader-RFID-chip-Arduino-Raspberry/dp/B07D9C82W8/ref=asc_df_B07D9C82W8/?tag=nlshogostdde-21&linkCode=df0&hvadid&454717163742& =1142888669055717597&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1010543&hvtargid=pla-464388957750&psc=1)

#### Other components
* [Servo Motor](https://www.amazon.nl/AZDelivery-Micro-Servo-Helicopter-Aircraft/dp/B07CZ42862/ref=asc_df_B07CZ42862/?tag=nlshogostdde-21&linkCode=df0&hvadid=430533579786&hv74thpont &hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9064189&hvtargid=pla-828702003009&psc=1)
* [PWM](https://www.grandado.com/products/dc-6-v-12-v-24-v-28vdc-3a-80-w-pwm-motor-speed-controller-regulator-adjustable -variable-speed control-with-potentiometer-switch?utm_campaign=&utm_content=&utm_source=Channable.beslist&utm_medium=8719896452153&utm_term=&variant=6367870779424&currency=EUR&bl3nlclid=1c1a3faf002d-483450-)
* [Laser pen] (https://www.bol.com/nl/p/rode-laserpen-laserpointer-presenter/9200000096827660/?Referrer=ADVNLGOO002013-G-49170245275-S-382273935838-9200000096827660&gclid=Cj0KCQjw8fr7BRDSARIsAK0Qqr4wtriGnA7w05cbYwetCRWlzGTZG8IwYBKZRWvI1EnVb_BiWOHe3F8aAvjPEALw_wcB)

### L.O.M = Laser Receiving Module
This sensor measures whether it is hit by a **laser beam**.
when the sensor is hit it transmits a high signal
to the raspberry pi. That signal is processed to the movement
of the servo motor at the target.

### Ultrasonic Sensor
We use the Ultrasonic sensor (HC-SR04) to measure how far the
player is out of the game. If the player is within 3 meters of the game, the game will be stopped until you are 3 meters from the game again.

### RFID sensor
We use the RFID sensor(MFRC-522 RC522) for scanning
the play pass. which must be scanned to activate the
game.

### Servo
The servo motors are used to turn the targets
fall when they are hit and turn them back up at the end of the game.
