---
title: How cold can peltier coolers get?
date: 2023-07-15T15:10:00-05:00
tags: electronics
author: Sebastien Chiasson
summary: Simple tests to see how much peltier coolers can cool
---

## Overview

I want to make a portable cooling pack for hot days, so I wired up some prototypes to get an idea how they function. What I'm thinking: with a 5V battery pack and some old CPU coolers, I can make a kind of cooled vest.

My tests measure how cold I can get a small block of aluminium. If this were part of a best, it would have water circulating through the block to cool down your body during hot summer days.

The coldest I got is -2.5C after 5 minutes. At this point there was condensation but not frost. (This would be dangerous if a pump were to break and water were to stay still long enough to freeze!)

![A photo of the colder temperature reached: -2.5C]({attach}cooler_coldest.jpg)

## What is a peltier cooler?

I get my cooling from peltier coolers, also known as thermoelectric coolers.

They're devices that become hot on one side but cool on the other. You just need to supply some power, and it will create this temperature difference without any moving parts. However, it is not very efficient and creates more heat than cooling. Simple to operation, but wasteful in operate.

You can find peltier coolers in some camping coolers. They provide a little bit of extra coolness, but since peltiers aren't very efficient, they're not something you want to trust with your food for a long time. Refrigerators with compressors are much more efficient.

You can read about the peltier effect in more detail on Wikipedia: <https://en.wikipedia.org/wiki/Thermoelectric_cooling>

### Setup

When I put everything together, I can just drop the thermometer into the water block. I let it run for 5 minutes and see how the temperature changes over time.

![A photo of the meat thermometer probe in the water block and the multimeter measuring current to peltier]({attach}test_setup.jpg)

## Hardware

All of this equipment is improvised. If you want to try this out, use whatever you can find.

The test setup revolves around squishing a cooler block, peltier coolers and heatsinks together. The peltiers cool down the water block (with thermometer inside) and dump heat through the heatsink. In practice, the water block would have water passing through it to cool other parts of your body.

  * Two generic 12V/50W thermoelectric peltier cooler, such as [these](https://www.amazon.ca/Aideepen-TEC1-12706-Heatsink-Thermoelectric-Cooling/dp/B078T7J3SF) (these get very hot, so be careful handling them!)
  * Two old-style stock AMD coolers (see image below)
  * A [Noctua NH-D9L](https://noctua.at/en/nh-d9l), a small CPU cooler with a 90mm fan
  * An aluminium CPU cooler block, 40mm x 40mm x 12mm, like [this](https://www.amazon.ca/dp/B07WRBDP8K)
  * Some thermal grease to transfer heat between components, a [20g tube from StarTech](https://www.startech.com/en-ca/computer-parts/heatgrease20)

The peltiers are power hungry! Make sure whatever power supply you use can handle a few amps.

  * A 5V 3A power supply, I use [a basic Elenco one](https://www.amazon.ca/Elenco-Triple-Output-Power-Supply/dp/B0002DT0GU)
  * A Nintendo Wii 12V 3.7A power supply, with some homemade wiring
  * A [Weber meat thermometer](https://www.weber.com/CA/en/accessories/grill-tools--et--cookware/instant-read-thermometer/6750.html) for measuring temperatures
  * A multimeter with ability to measure a few amps

### The AMD coolers setup

With the two AMD coolers, I use their braces to make a big cooler sandwich. The water block is sandwiched between peltiers, which are sandwiched between coolers. The secret sauce, of course, is silicone thermal grease--the mayonnaise of heat transfer.

The fans run at 5V, separate from the peltiers' 5V/12V power supply.

![A photo of two AMD coolers attached to two peltier coolers, surrounding an aluminium water block]({attach}amd_cooler.jpg)

### The Noctua cooler setup

The Noctua cooler is higher-end cooler, but I only have one. I keep everything together with some rubber bands.

The fan always runs at 5V.

![A photo of the water block, peltier and cooler held together by rubber bands]({attach}noctua_cooler.jpg)

## Results

Not surprisingly, more power and more peltiers give more cooling. There's a sweet spot of having two peltiers in parallel running off of 5V. This would run on a 5V portable battery pack and is my best bet for a cooler vest.

![A plot of the temperature over time]({attach}cooler_plot.png)

| Cooler       | Voltage | Amperage | Wattage | Lowest temperature |
|--------------|--------:|---------:|--------:|-------------------:|
| Noctua       | 5V      | 1.1A     |  5.5W   | 17.5C              |
| AMD series   | 12V     | 2.3A     | 27.6W   | 10.3C              |
| AMD parallel | 5V      | 1.7A     |  8.5W   |  5.5C              |
| Noctua       | 12V     | 2.3A     | 27.6W   | -2.4C              |
| AMD parallel | 12V     | 4.0A     | 48.0W   |    ?               |

## Hot!

I had to stop my test of two peltiers in parallel at 12V 4A because my homemade wiring started melting... This is just some improvised wiring I had made years ago to work with the Wii power supply.

![Smoke coming out of homemade power supply wiring]({attach}smoke_smaller.gif)

Also, the power supply is only rated for 3.7A. It was probably okay, but that smoke was a warning for me to steer clear of the amped-up lifestyle!

![Specs of the Nintendo Wii PSU]({attach}nintendo_wii_psu.jpg)

## Feline assistance

If you make eye contact with a cat, it takes that as an invitation.

![GIF of cat taking an opportunity to jump on my lap]({attach}surprise_cat.gif)

## Next steps

I'll take the 5V setup with the two AMD coolers, add in some tubing and a water pump, and see how cool the circulating water gets.

