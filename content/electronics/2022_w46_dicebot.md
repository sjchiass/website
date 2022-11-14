---
title: Dicelot the dicebot
date: 2022-11-13T20:30:00-05:00
tags: raspberry pi, sensors, python
author: Sebastien Chiasson
summary: A robot that rolls dice
---

# Dicelot the Dicebot

## Overview

It's a Raspberry PI 2b and Pico working together to roll a 6d6. I call it Dicelot because my poor penmanship transforms `dicebot` into `dicelot`.

I have all the code on GitHub: <https://github.com/sjchiass/dicebot>

## Neat stuff

  * It generates nearly 60,000 images from 27 originals. Despite the fake data the ML model still works!
  * The Pico is really cool: you can call it with the `adafruit-ampy` Python package and send it some Python code to run.
  * Tensorflow Lite is an inference-only version of Tensorflow for running smaller models.

## Example

![A GIF of the robot shaking dice]({attach}dice_shaking.gif)

![The robot's guess]({attach}inference_example.jpg)

## Hardware

Pretty standard stuff

  * A Raspberry Pi
  * A Raspberry Pi Pico with [Kitronik robotics board](https://kitronik.co.uk/products/5329-kitronik-compact-robotics-board-for-raspberry-pi-pico) (it has the capacity for 8 servos and 4 motors... I only use one servo)
  * A Raspberry Pi camera with a 12" long cable
  * An old plastic bottle of [nori and sesame furikake](https://www.takaokayausa.com/collections/furikake) to hold the dice
  * An old Amazon cardboard box, some wooden sticks and some hotglue
  * Bonus: a miniature 800x480 HDMI screen to make the project portable

## Next steps

Well, I might have gotten all the fun out of this that I can. Now that I know how to use the Pico, I'll use it for other projects.

I really want to use Lego Technic pieces for my next project. If I'm careful I probably won't ruin them!

## Cat tax

![My cat studying the dicebot]({attach}cat_dicebot.gif)

