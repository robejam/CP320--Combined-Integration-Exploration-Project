# CP320-Combined Integration Exploration Project  
# (Winter 2019)
### By:
<p>Morgenne Besenschek</p>
<p>James Robertson</p>

### Overview
This circuit highlights the use of a joystick to control the connected devices. By moving the joystick left or right, the stepper motor will move clockwise or counterclockwise. The stepper motor moves faster the further away from neutral the joystick is. Moving the motor changes the position of the time of flight sensor, which detects how close an object is. Users can move the sensor back and forth, and view how far away the sensor is from the other side of the device by reading the OLED screen. 

[Main Program](https://github.com/robejam/CP320--Combined-Integration-Exploration-Project/blob/master/Project%20Files/integrationcode.py)

### Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=XyRx3iDWlRw
" target="_blank"><img src="http://img.youtube.com/vi/XyRx3iDWlRw/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Features we implemented:
- The value of having the abs_x_pos and abs_y_pos functions are that they convert the raw joystick output values to a familiar scale, where neutral joystick position is at (0,0): [joystick.py](https://github.com/robejam/CP320--Combined-Integration-Exploration-Project/blob/master/Project%20Files/joystick.py)
  ```python3
  def abs_x_pos(lr_pos):
      if lr_pos > 516:
          abs_pos = lr_pos - 516
      elif lr_pos < 516:
          abs_pos = -1*(516-lr_pos)
      else:
          abs_pos = 0
      return abs_pos

  def abs_y_pos(ud_pos):
      if ud_pos > 506:
          abs_pos = ud_pos - 506
      elif ud_pos < 506:
          abs_pos = -1*(506-ud_pos)
      else:
          abs_pos = 0
      return abs_pos
  ```

- The `sleep(val)` function in [joystickstepper.py](https://github.com/robejam/CP320--Combined-Integration-Exploration-Project/blob/master/Project%20Files/joystickstepper.py) was another key thing for us to implement for stepper control as it allowed us to ramp the speed of the stepper motor shaft based on the position of the joystick. The function relies on the linear equation `slp(val) = -0.00018 * val + 0.1` where `val` is the absolute joystick value. The function computes a value between 0.1 and 0.01, the higher the number the more time there is between `stepper_sequence` rows causing the shaft to rotate slower and the inverse effect if the value is closer to 0.01.

### Block Diagram

![Block Diagram](https://raw.githubusercontent.com/robejam/CP320--Combined-Integration-Exploration-Project/master/Block%20Diagram.png)

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
  - One of the first sites we found that pointed us in the right direction but ultimately resulted in a headache as the site omits SPI speed for unknown reasons.  
- Sparkfun I2C Tutorial: [Link](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi)
  - Really helpful for us as the tutorial taught us about the `i2cdetect` program that lists the addresses of all connected I2C devices and two of our devices utilized I2C communication.
- Understanding Optical Time-of-Flight (ToF) Technology: [Link](https://www.youtube.com/watch?v=TpjnooXhOmY)
  - An informative mini tutorial on how TOF sensors like the ST VL53L0X work.
- Microstepping: [Link](https://hackaday.com/2016/08/29/how-accurate-is-microstepping-really/)
  - Not implemented in this project but used during research but an informative page on the topic, planning to attempt              implementing eventually. 
- CP320 Course website: [Link](http://denethor.wlu.ca/pc320/index.shtml)
- Google: [Link](www.google.ca)
  - Becuase it is our best friend
