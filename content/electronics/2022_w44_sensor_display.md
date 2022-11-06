---
title: Environmental sensor display
date: 2022-11-05T21:00:00-04:00
tags: raspberry pi, sensors, python
author: Sebastien Chiasson
summary: My first version of a multi-sensor display
---

## Overview

This is a Raspberry Pi in a SmartiPi case with an official Raspberry Pi touchscreen. It makes a good simple display! People like looking at it change.

Inside the case there are temperature, humidity, CO2, voltatile organic compounds, and particulate sensors. They're fairly safe in there and have a fan to feed them fresh air. The more sensors you add, the more variety the dashboard has.

![A photo of the dashboard active, showing its temperature, humidty, etc gauges]({attach}dashboard.jpg)

## What it looks like

<iframe width="560" height="315" src="https://www.youtube.com/embed/v9opm4-TGmg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Measuring soldering fumes

<iframe width="560" height="315" src="https://www.youtube.com/embed/cnHTNX3bILg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Hardware

  * Sensors (the good stuff)
    * [DHT-22](https://www.adafruit.com/product/385) temperature and humidity sensor
    * [SGP30](https://shop.pimoroni.com/products/sgp30-air-quality-sensor-breakout) eCO2 and TVOC sensor
    * [PMS5003](https://shop.pimoroni.com/products/pms5003-particulate-matter-sensor-with-cable) particulate sensor, it shoots lasers at air to measure particles
  * Computer stuff
    * Raspberry Pi 4
    * [Official Raspberry Pi touchscreen](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)
    * [Smartipi Pro case](https://smarticase.com/products/smartipi-touch-pro), which fits the the screen, Pi and all the sensors

## Neat stuff

I have the code on [GitHub](https://github.com/sjchiass/sensor_display).

### Systemd user services

I followed [this guide](https://github.com/torfsen/python-systemd-tutorial). These services will run the code **when the user logs in**, so you can have your data logging scripts going right away.

(Services in Linux are like those hundreds on programs you see running in the background in the Windows Task Manager. They're background processes.)

I think that when I upgrade to actual system services (not user-dependant), I'll have a really powerful solution. Shutdown or reboot the computer and everyhting starts up again. It's also possible to have the services restart themselves automatically if they crash or need to restart for whatever reason.

### Efficiently reading files

Python reading a file in binary mode can skip to the end of it. So with a CSV you don't need to read the whole thing. [This Stack Overflow post](https://github.com/sjchiass/sensor_display/blob/main) shows how.

```python
with open(filename, "rb") as file:
    # Go to the end of the file before the last break-line
    file.seek(-2, os.SEEK_END) 
    # Keep reading backward until you find the next break-line
    while file.read(1) != b'\n':
        file.seek(-2, os.SEEK_CUR) 
    data = file.readline().decode()
data = data.replace("\n", "").split(",")
```

