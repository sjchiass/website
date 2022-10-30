---
title: A basic voltmeter with an LCD
date: 2020-08-30T16:46:00
tags: electronics, arduino
author: Sebastien Chiasson
summary: A basic voltmeter with an LCD. Simple but instructive.
---

### Past week

You can do fun things by reading the Arduino analog pins.

I used this sample LCD code as a base: <https://www.arduino.cc/en/Tutorial/HelloWorld>.

The Arduino (the Atmega 328P) measures 0V-5V on its analog pins. It can return 1024 values (10-bit). By default the reference is the voltage supply (5V) but can be switched to whatever you have connected to the `AREF` pin.

So out of the box you can make a 0V-5V voltmeter with the analog pins. Feed the analog pin a voltage and it'll return a number from 0 to 1023. Divide the number by 5 and you get a float from 0V to ~5V.

With voltage dividers you can expand that range. By dividing your input with 110k ohms (ground) and 460k ohms (voltage), you will divide your incoming voltage by 5.7. If you feed in 20V, it will become about 3.5V, which is within the 0V-5V range. Your range has now expanded to 0V-28V.

So with a voltage divider you can make a basic voltmeter that measure beyond the 0V to 5V range. Here's how I did it in the Arduino C code.

```
// print the calculated voltage
float vin = 5.05; // should this be 5V instead?
// divide resistances by 1000 for simplicity
float adj = (101.0 + 476.0) / 101.0;
lcd.print(vin * analogRead(A0) * adj / 1024.0);
```

The higher voltage is a bit too high.

![Measuring higher voltage]({attach}20200830_144555.jpg)

The lower voltage is better, I think?

![Measuring lower voltage]({attach}20200830_144601.jpg)

Just to show my setup, I had the variable voltage of my power supply going into the voltage divider and then into the analog pin. The rest of the circuit follows the LCD guide and is powered by the power supply's regulated 5V, which in turn is the `AREF`.

![Setup]({attach}20200830_144633.jpg)

### Next week

Here is a plot of the squishing that happens with my voltage divider above. The divider reduces the higher voltage into the 0V to 5V suitable for the Arduino analog pin.

![Simple divider]({attach}simple_divider.png)

When you divide with ground (0V), you're using it to reduce the voltage of the incoming positive voltage source (allowing you to measure higher voltages). The re-scaling of the voltage is centered on 0V.

If you were to divide with another voltage, it would be centered on that instead. Or rather, it would be centered more towards it.

![5V divider]({attach}5v_divider.png)

It took me a bit of time to realize that this is how voltage dividers behave with two positive voltage sources.

If I want to offset a voltage, I have to use the Arduino's `AREF`. I need to think more about how the reference value affects things. The range should always be 0V to `AREF`, right? How can it be made to be below 0V?
