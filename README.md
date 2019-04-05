# CP320-Combined Integration Exploration Project (Winter 2019)
### By:
<p>Morgenne Besenschek</p>
<p>James Robertson</p>

### Overview

This circuit highlights the use of a joystick to control the connected devices. By moving the joystick left or right, the stepper motor will move clockwise or counterclockwise. Moving the motor changes the position of the time of flight sensor, which detects how close an object is. Users can move the sensor back and forth, and view how far away the sensor is from the other side of the device by reading the OLED screen.

Features we implemented:
- Converts joystick output values to a familiar scale, where neutral joystick position is at (0,0): [joystick.py](https://github.com/robejam/CP320--Combined-Integration-Exploration-Project/blob/master/Project%20Files/joystick.py)
- Controlling a stepper motor using a joystick: [joystickstepper.py](https://github.com/robejam/CP320--Combined-Integration-Exploration-Project/blob/master/Project%20Files/joystickstepper.py)

Moving the joystick left or right moves the stepper motor counterclockwise or clockwise. The stepper motor moves faster the further away from neutral the joystick is.

Full circuit integration can be viewed [here.](https://github.com/robejam/CP320--Combined-Integration-Exploration-Project/blob/master/Project%20Files/integrationcode.py)

### Block Diagram

![Block Diagram](https://raw.githubusercontent.com/robejam/CP320--Combined-Integration-Exploration-Project/master/Block%20Diagram.png)

### Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=XyRx3iDWlRw
" target="_blank"><img src="http://img.youtube.com/vi/XyRx3iDWlRw/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Biggest Challenges

We ran into a roadblock at the beginning of the project with the joystick refusing to function despite all efforts to debug potential software and hardware issues. After spending an entire class trying to figure out the issue, [this](https://www.raspberrypi.org/forums/viewtopic.php?t=213951#p1323337) forum post ended up highlighting the importance of the SPI max_speed_hz option.

### Components Used
- Stepper Motor: [Link](http://sayal.com/STORE/View_SPEC.asp?SKU=162138)
- L298N dual bridge DC stepper controller board: [Link](http://sayal.com/STORE/View_SPEC.asp?SKU=248133), [Datasheet](https://www.velleman.eu/downloads/29/vma409_a4v01.pdf) 
- Adafruit VL53L0X Time of Flight Distance Sensor: [Link](https://www.digikey.ca/product-detail/en/adafruit-industries-llc/3317/1528-1814-ND/6569762), [Datasheet](https://www.st.com/resource/en/datasheet/vl53l0x.pdf) 
- Parallax 2 Axis Joystick: [Link](https://www.robotshop.com/ca/en/parallax-2-axis-joystick.html), [Datasheet](https://www.parallax.com/sites/default/files/downloads/2-Axis-Joystick-Potentiometer-Datasheet.pdf)
- SSD1306 128x32 OLED: [Datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)
- Bearing: [Link](https://www.amazon.ca/gp/product/B00EPNN62M/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- Shaft Coupler: [Link](https://www.amazon.ca/gp/product/B07BF7NT6L/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
- Screw Rod with Brass Nut: [Link](https://www.amazon.ca/gp/product/B01HGIZY6I/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
- Acrylic parts were designed and laser cut at the Laurier Science Maker Lab: [Link](https://students.wlu.ca/work-leadership-and-volunteering/entrepreneurship/makerspaces/science-maker-lab/index.html)

### Libraries Used
- Luma.OLED: Display drivers for SSD1306: [Link](https://github.com/rm-hull/luma.oled)
- Python Imaging Library: [Link](https://github.com/python-pillow/Pillow)
- VL53L0X Api port for Raspberry Pi: [Link](https://github.com/cassou/VL53L0X_rasp)

### Useful Links
- Using A Joystick On The Raspberry Pi Using An MCP3008: [Link](https://www.raspberrypi-spy.co.uk/2014/04/using-a-joystick-on-the-raspberry-pi-using-an-mcp3008/)
