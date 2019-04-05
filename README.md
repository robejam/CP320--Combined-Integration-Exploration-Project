# CP320-Combined Integration Exploration Project (Winter 2019)
### By:
<p>Morgenne Besenschek</p>
<p>James Robertson</p>

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
