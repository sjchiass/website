---
title: Automated plant growing
date: 2022-09-03T15:00:00-04:00
tags: plants, electronics
author: Sebastien Chiasson
summary: Growing plants in soil but with some automatic pumps
---

## Overview

:leaves: :herb: :strawberry:

This is some arugula, cat grass, and jalapeno plants in three plastic containers on top of a bookcase. They have some lights above and some nearby water pumps.

There's a Raspberry Pi Zero taking photos, reading sensors and posting everything here: https://plants.sjchiass.com

## Videos

### Timelapse

This gives a good idea of the results

<iframe width="560" height="315" src="https://www.youtube.com/embed/RcQ8kqm4ix0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Pumps pumping water

This shows how I run the pumps for at least 5 seconds to get enough water into the pots

<iframe width="560" height="315" src="https://www.youtube.com/embed/LzDN57yIcsg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Setup

![How the electronics are mounted next to the plants]({attach}20220823_210632.jpg)

It's a pretty DIY setup tied to a bunch of wooden sticks.

From left to right

  * If you're curious, the sticks are tied together with a **lashing knot** https://www.animatedknots.com/tripod-lashing-knot
    * Pretty sturdy and useful when you're short of construction materials
  * **A DHT-22** sensor for measuring temperature and humidity https://www.pishop.ca/product/dht22-am2302-digital-temperature-humidity-sensor-for-arduino/
  * Part of a soil moisture sensor attached to a **photo-resistor**
    * Soil sensors that measure soil moisture by resistance corrode quickly.
    * It does come with a useful board, so I use it to measure light intensity instead.
  * A Raspberry Pi **NoIR camera** to see in the dark, sort of https://www.pishop.ca/product/raspberry-pi-noir-camera-module-v2-8mp/
  * Attached to the camera, a **Bright Pi** board https://www.pishop.ca/product/bright-pi-bright-white-and-ir-camera-light-for-raspberry-pi/
  * A **Grow hat**, to measure soil moisture by capacitance and to run the pumps https://www.pishop.ca/product/grow/
  * A **Raspberry Pi Zero** (hiding)
  * An **Arduino Uno**
  * Three somewhat **cheap pumps** from Amazon
    * I had to find these "picoblade" molex-like connectors before I could connect to the Grow
    * Annoyingly, they don't seem super common, and I got them from Amazon

## Some thoughts

### Calibrating moisture sensors

Over time the sensors have gotten less sensitive to water. In the configuration you can set them in a range from 30-1. I now have them set at 3-1, after having decreased the value lower and lower. So I am pretty much at the limit.

#### Possibilities

  * The sensors are wearing down (moist soil is a hostile environment for sensors)
  * The soil is getting so dense with roots that it makes the soil seem more moist
  * The pumps cause some erosion of the soil, meaning that the water goes straight down rather than propagate to the side of the pot where the sensors are
  * Peat moss is not what these sensors are expecting

### Choice of soil

My soil is mostly peat moss, which seems to really hate water. You can add water to a pot of peat moss and the two will just stay completely apart. When the peat moss and the water do mix though, they make a really dense sludge. A soil that goes from these two extremes is tougher to manage I think.

Next time I will use normal potting soil.

### How long to run pumps?

The basic settings have the pumps running every 1 minute but only for 0.5s. My pumps seems weaker so that's not enough time for water to get into the pots. Instead I run for at least 5 seconds (you can see this well in the second video above).

Here is my configuration

```
channel1: {auto_water: true, dry_point: 3, enabled: true, pump_speed: 0.5, pump_time: 5.0,
  warn_level: 0.5, water_level: 0.5, watering_delay: 600, wet_point: 0}
channel2: {auto_water: true, dry_point: 10, enabled: true, pump_speed: 1.0, pump_time: 5.0,
  warn_level: 0.5, water_level: 0.5, watering_delay: 600, wet_point: 0}
channel3: {auto_water: true, dry_point: 3, enabled: true, pump_speed: 0.5, pump_time: 5.0,
  warn_level: 0.5, water_level: 0.5, watering_delay: 600, wet_point: 0}
general: {alarm_enable: true, alarm_interval: 600, black_screen_when_light_low: true,
  light_level_low: 4.0}
```

I have a very high watering delay of `600` (default is `60`). Why? If something goes wrong, the pumps will keep pumping until the reservoir is empty! **It's really important to have a way of dealing with overflow!** By setting a high delay, I reduce the potential damage.

If you're away for a while, all bets are off.

### Bottoms up

My plants now have enough roots that they can be watered from the overflow container. You can put 500ml of water there, and the plants will suck it all up in a few minutes. This can be a convenient alternative to letting the pumps do the work.

I found this out when one of the pumps emptied the reservoir. The plants cleaned up the mess on their own. Good plants. :heart:

### Algae

`nutrients + water + light = algae`

I have some growing in my water reservoir now. Ideally my reservoir should block out light, or I only feed nutrients by the bottoms up method.

![Small patches of green algae in the water reservoir]({attach}20220823_210700.jpg)

## Conclusion: baby peppers?

I'll keep running the setup until the pepers are done maturing. While the setup is automatic, it is still a bit annoying having to keep an eye on it.

Plus I want the Raspberry Pi Zero back for a cat camera. :cat: :camera:

![A very small pea-sized jalapeno pepper]({attach}20220830_190048.jpg)

