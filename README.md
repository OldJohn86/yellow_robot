# yellow_robot
------------------

	A quadruped robot, inspired from OpenQuadrupeder/microspotAi robot
	https://gitlab.com/custom_robots/spotmicroai/website

	forum : https://app.slack.com/client/TLWGGB71C/CMN94UF0F

------------------

# PAY ATTENTION !! THE ROBOT HAS NOT BEEN TESTED FOR NOW, WITH WALK CYCLE

------------------

### To-Do List

- [x] *Hardware* // Teensy firmware, from Maurice Rahme, https://github.com/moribots/spot_mini_mini/tree/spot/spot_real/Control/Teensy,

- [x] *Builds*   // modify legs : add a belt tensionner,
- [x] *Builds*   // modify upper legs : simulate a DLDC motors,
- [x] *Builds*   // modify legs : add a belt tensionner,
- [x] *Builds*   // add a handle,
- [ ] *Builds*   // add bottom cover metal patchs, for dock station charge,

- [ ] *Software* // Myahrs+ usb IMU. Create/add the ROS Melodic package,
- [ ] *Software* // Ultrasonic sensors (FL, FR, Back). Create the ROS Melodic package who publishs the 3 topics,
- [ ] *Software* // D435 intel camera. Create/add the ROS Melodic package,
- [ ] *Software* // HP Speaker. Create the ROS Melodic package, with a service,
- [ ] *Software* // RGB leds ramps (FL and FR). Create the ROS Melodic package, with a service,
- [ ] *Software* // back lcd screen I2C. Create the ROS Melodic package, with a service,
- [ ] *Software* // back RPI Cam. Create the ROS Melodic package,
- [ ] *Software* // back joystick (ADC ADS1115 I2C). Create the ROS Melodic package,
- [x] *Software* // top cover RGB led. Create the ROS Melodic package,
- [ ] *Software* // battery status (ADC ADS1115 I2C). Create the ROS Melodic package,

------------------

SYSTEM VERSION : Ubuntu 18.04 64bits

ROS VERSION    : Ros version 1 : MELODIC

------------------

MASTER BOARD   : RPI4B or Jetson Nano

2ND BOARD      : Mano Biletsky home-made board
                 https://github.com/mano1979

3RD BOARD      : Teensy 4.1 or 4.0

------------------

SERVOS         : 12 x DS3218MG 180°, or better...35Kgs

------------------

OTHERS         : 

                 1 D435 intel depth camera

                 3 HC04P iltrasonic sensors
                 
                 1 raspberrypi picam
                 
                 1 imu (mine : Myahrs+)
                 
                 1 analogic joystick
                 
                 1 20x40mm speaker
                 
                 2 Neopixels 8x
                 
                 1 RGB led
                 
                 2 x ADC ADS 1115
                 
                 1 tiny led screen
                 
                 1 5v ubec
                 
                 1  power switch

------------------

BEARINGS           :  (refs/link  may change !!)

                      20 x 625.zz 5*16*5
https://www.ebay.fr/itm/10-x-Kugellager-625-ZZ-5-16-5-mm-3D-Drucker-CNC-Modellbau/181937342662?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649

                       4 x 6810 2RS / 61810 2RS 50x65x7 mm
https://www.kugellager-express.de/navi.php?kf=&ed=1&qs=6810+2RS+%2F+%26%238234%3B61810+2%26%238236%3BRS+50x65x7+mm&search=

METAL SERVOS ARMS  :  (refs/link  may change !!) 

                    12 x Metal Round Servo Arm 25T Disc Horns
https://www.ebay.fr/itm/x5-Metal-Round-Servo-Arm-25T-Disc-Horns-for-MG995-MG996R-Futaba-Savox-RC-Robot/263283372008?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649

BELTS              :  (refs/link  may change !!)

                     4 x GT2 2 m 2 mm pitch 6 mm
https://www.ebay.fr/itm/GT2-2M-2mm-Pitch-6mm-Width-Closed-Loop-Synchronous-Timing-Belt-for-Pulley-CNC-3D/283194907394?ssPageName=STRK%3AMEBIDX%3AIT&var=585191909441&_trksid=p2057872.m2749.l2649

------------------

TOTAL WEIGHT :

                    ~3080 Grs
                   
------------------

SERVOS MOUNT :

			 See calibration page !

------------------


![Alt text](/OpenQuad_V2/images/boxed.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/handle.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/looking.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/paused.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/stand.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/head.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/top_cover.jpg?raw=true "Openquad_v2")

![Alt text](/OpenQuad_V2/images/bottom_cover.jpg?raw=true "Openquad_v2")

Printer : Zortrax M200+ 3D printer.

Filaments : Z-ABS+, Z-ULTRA, ABS+ Black CARBON.

infill : 20%

![Alt text](/OpenQuad_V2/images/zortrax_m200_plus.jpg?raw=true "Openquad_v2")

------------------

	Vincent FOUCAULT
	vincentfoucault12@gmail.com
	FRANCE
