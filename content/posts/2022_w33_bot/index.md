---
title: Adventures of FartBot
date: 2022-08-14T09:00:00
tags:
- cats
- electronics
author: Sebastien Chiasson
summary: A robot approaches cats while meowing and farting
---

## Overview

This is Trilobot kit powered by a Raspberry Pi 4 and USB battery pack. There's a cheap speaker on the back to play the sounds. The controls are through Python.

## Video

:pouting_cat: :poop: :pouting_cat:

{{< youtube siE60RSGWLs >}}

## Parts list

Here's what I needed to make this, with some comments. :white_check_mark:

  * [Raspberry Pi 4 8GB](https://www.pishop.ca/product/raspberry-pi-4-model-b-8gb/)
    * The CPU and memory usage is very low, so a less powerful Raspberry Pi is better.
  * [Trilobot](https://www.pishop.ca/product/trilobot/)
    * Official [setup guide](https://learn.pimoroni.com/article/assembling-trilobot)
    * The kit provides the chassis, wheels, and distance sensors (which I don't use for now)
    * The Raspberry Pi is sandwiched inside the chassis
    * The camera is sandwiched in plates at the front of the body
  * [A cheap non-official Raspberry Pi camera](https://www.pishop.ca/product/raspberry-pi-compatible-5mp-camera/)
    * I got mine cheap on Amazon. If it's non-standard, the camera might have components that make it hard to mount properly.
  * [A 3A 5V battery pack](https://www.pishop.ca/product/power-bank-10000-mah-usb-c-fast-charge/)
    * In my opinion, the 3A is necessary. The Pi would sometimes reboot with less powerful batteries.
    * The [official Trilobot battery](https://shop.pimoroni.com/products/nanowave-3-5000mah-usb-c-a-power-bank) is 3A.
  * [A speaker with its own battery](https://www.amazon.ca/Rokono-Speaker-iPhone-Player-Laptop/dp/B007NJ3SIM)
    * Mine is older and was probably cheaper than this. Not sure where we got it, but it was probably from a discount store.
    * This kind of speaker is charged by USB and connects by a standard audio jack, which the Raspberry Pi has.
    * They are pretty loud!

Optional stuff :question:

  * [Argon Fan HAT](https://www.pishop.ca/product/argon-fan-hat-for-raspberry-pi-3b-3b-4b/)
    * The Raspberry Pi 4 gets hot, so having a fan might help.
  * [Headers](https://www.pishop.ca/raspberry-pi-header-dimensions/)
    * If you're going to add HATs to the Pi, you'll need to play with different header sizes to make things connect properly.
  * [Spacers](https://www.pishop.ca/product/brass-screw-and-stand-off-set-m2-5-180-pieces/)
    * Again, if you're adding stuff, you need a variety of sizes to make fit properly. A bit of trial and error.

## Software

### Streaming

Controlling a robot like this is difficult with lag. It was a challenge to find a streaming method that worked best.

Luckily the `libcamera` documentation has [a lot of examples](https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-vid) on how to do low-latency streaming. For the least latency use the `ffplay` commands, not the `cvlc` commands.

In my case, I set the camera framerate to 12. I find that this seems to reduce lag further. I'm guessing this is because the client "falls behind" at higher framerates.

My command for the server/robot:

```console
libcamera-vid -t 0 -n --width 800 --height 600 --codec h264 --profile baseline --framerate 12 --inline --listen -o tcp://0.0.0.0:8888
```

My command for the client/controller:

```console
ffplay tcp://192.168.0.123:8888 -fflags nobuffer -flags low_delay -framedrop
```

### Playing sound

I got free sound files from [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Flatulence). On Linux you can play `.wav` with `aplay`. For `.ogg` files you need to install `vorbis-tools` and then play them with the `ogg123` command. Both of these commands can be used non-blocking in Python with `subprocess.Popen()`.

### Remote control

I'm still working on this code. I feel like there must be a better way.

When you connect to the Pi through SSH, you only have a terminal to send commands over. What this code does is listen for key presses and run code conditionally. If a key is held down, it stays in its current state. If a key stops being pressed, the code returns to rest after a delay.

So if you hold down `w` the robot will keep moving forward. Since you're holding down `w`, you're actually sending repetitive `wwwwwwwwwwww` every 100ms or so through the console. When you stop pressing `w`, the robot will keep moving forward for 500ms and then stop.

If you tap `a` the robot will rotate to the left for 500ms, then stop.

This makes it like playing a video game on your keyboard. However, it's a lot less responsive and you can't press key combinations.

```python
import sys
import select
import tty
import termios
from random import sample
from subprocess import Popen
from time import sleep
from trilobot import Trilobot

tbot = Trilobot()

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)

def tbot_dispatch(i, speed):
    if i in ["w", "a", "s", "d", "q", "e"]:
        if i == "w":
            tbot.forward(speed)
        elif i == "a":
            tbot.turn_left(0.8*speed)
        elif i == "s":
            tbot.backward(speed)
        elif i == "d":
            tbot.turn_right(0.8*speed)
        elif i == "q":
            tbot.set_motor_speeds(0.8*speed, speed)
        elif i == "e":
            tbot.set_motor_speeds(speed, 0.8*speed)
    elif i == "m":
        to_play = sample([
        ["ogg123", "meow1.ogg"],
        ["ogg123", "meow2.ogg"],
        ["aplay", "meow3.wav"],
        ["ogg123", "meow4.ogg"]
        ], 1)
        Popen(to_play[0])
    elif i == "f":
        to_play = sample([
        ["ogg123", "fart1.ogg"],
        ["aplay", "fart2.wav"],
        ["ogg123", "fart3.ogg"]
        ], 1)
        Popen(to_play[0])
    elif i == "l":
        tbot.fill_underlighting(255, 255, 255)
    elif i == "k":
        tbot.fill_underlighting(0, 0, 0)
    elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        i = float(i)
        if i == 0.0:
            speed = 1.0
        else:
            speed = i/10.0
    else:
        tbot.coast()
    # Return the speed value
    return speed

speed = 0.5
downtime = 0
increment = 0.05
threshold = 10 * 0.05
at_rest = False
new, old = "", ""
try:
    tty.setcbreak(sys.stdin.fileno())

    while True:
        if isData():
            new = sys.stdin.read(1)
            at_rest = False
            downtime = 0
            if new == '\x1b':         # x1b is ESC
                break
            elif new != old:
                speed = tbot_dispatch(new, speed)
            old = new
        else:
            if at_rest:
                pass
            else:
                if downtime > threshold:
                    at_rest = True
                    new, old = "", ""
                    tbot.coast()
                    print("AT REST")
                else:
                    downtime += increment
                    sleep(increment)

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
```

## Next steps

  * Better lights to see in the dark :flashlight:
  * A microphone to stream audio :microphone:
  * Some kind of treat dispenser to make my cats a new friend :smiley_cat:
