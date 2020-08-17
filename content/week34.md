Title: Week 34 of 2020 update
Date: 2020-08-16 20:34
Category: Updates
Tags: plants, electronics
Slug: week-34-2020
Author: Sebastien Chiasson
Summary: Plants attacked by cats; miscellaneous electronics

## Plants

### Past work

My first adventures in cat grass growing came to its natural end.

My cats ate it.

I had moved the grass to the window since the plants had gotten too tall for the small lamp. I had also added a small fan to make them sway in the breeze, which is supposed to exercise them and make them tougher.

I was able to keep the container there for most of the week, but the cats eventually discovered it! They were obsessed with gobbling it all up. (Probably because they were afraid the other would eat it first.)

![Cat attack!]({static}images/updates/34/20200815_084221.jpg)

They only seem to enjoy the blades and not the stems. This leaves a few centimeters of the plants above the ground. I'll see if any are able to recover.

Here is a close-up of a cut grass blade. It looks to me like crushed areas are a darker green, while the clean cuts become dry and yellowed.

![Grass damage]({static}images/updates/34/vlcsnap-2020-08-16-18h58m20s641.png)

Sometimes the cats will get most of it in their mouths and will start chewing. If they don't manage to break it off, it'll just stay slimy like the photo below. There will also be some leftover trace evidence. (I think I got sick after some of that stuff fell into my tea.)

![A clue!]({static}images/updates/34/vlcsnap-2020-08-16-19h02m47s371.png)

I had wanted to take a close-up of the roots last time. This time they were a little beat-up and one had a small bug. The bug must have come from the potting soil. (I might have dropped some of that dirt into my tea... I was sick last week.)

![A small white bug crawls on a root]({static}images/updates/34/vlcsnap-2020-08-16-19h04m21s631.png)

### This week

I need to fix my plant growing setup. With some wood I'll build a structure for the light to come from higher above. I'll raise the plants or the structure with books, as needed. The important thing if for the light to come down directly.

At the store I was able to get a lightbulb receptacle that can plug into a wall outlet. As long as I'm able to secure it (duct tape?), I can position my light source it more freely.

![A new stronger bulb with a receptacle]({static}images/updates/34/20200816_193145.jpg)

## Other things

### OBS and streaming

I've been able to set up OBS Studio to output its video to a webcam. This should let me share desktops during video calls and even switch between multiple webcams. OBS Studio is used for streaming.

Getting OBS to output to a webcam requires [v4l2loopback](https://github.com/umlaeute/v4l2loopback). It's a Linux kernel module that will create a virtual `/dev/video` device that can receive video data and make it available as a webcam feed. As far as Discord/Skype/etc knows, your stream will just be another webcam.

I was able to get `v4l2loopback` to work on Ubuntu 18.04 and Fedora 32. In both cases it turned out easier that expected: just `git clone`, `make`, and `sudo make install`. The documentation warns you about mixing kernel and kernel header versions (or Linux will "spit in your eye"), but I haven't had problems yet.

In order to use the loopback in OBS, you also need the [obs-v4l2sink](https://github.com/CatxFish/obs-v4l2sink) OBS plugin. This was easy in Ubuntu 18.04, but Fedora 32 was troublesome. On Fedora you can build it easily enough, but it won't be recognized by OBS unless its install path is adjusted. See the discussion here: <https://github.com/CatxFish/obs-v4l2sink/issues/42> (I think the `sed` command fixed it for me.)

### Voltmeter and ammeter

Last week I was looking at a DROK brand voltage and current meter, but I afterwards discovered it had a minimum measurement threshold of 6.5V. This is too high for most of my electronics. Instead I went with a cheaper little unit.

![The meter connected to my power supply]({static}images/updates/34/20200816_192308.jpg)

The ammeter must be connected after the load; otherwise it doesn't measure current properly. Rather than integrate it into the power supply, I think I'm going to put the meter in a box and use it in-between the supply and the device/circuit. I can then just move it around as I want, like a multimeter.

I should also buy some of those USB multimeters. With some bodging they could work to measure the current draws of Arduinos.

### Banana plugs and alligator clips

These are surprisingly hard to find (cheap) online. They'd be nice to have for binding posts.

Small alligator clips are also handy. They're small enough to clip either around the back of the post, or through the hole in the front.

### Powering your old cellphone directly

My old phone's battery was dead, so I powered the phone directly and succeeded. This was a bit interesting. It's something that would be hard to do without a variable power supply, a multimeter, and some fine clip-on test leads.

![Clip-on test leads on the battery pins]({static}images/updates/34/20200811_194900.jpg)

The neat thing about this is that the phone battery isn't meant to operate at 3.8V as I first thought. With a 3.8V supply the phone will power up but immediately power off: it thinks the battery is critically low. The phone will only be happy at 4.0V to 4.3V, with the higher voltage registering as a "full" battery.

![Powered phone at 4.2V]({static}images/updates/34/20200811_201008.jpg)

The phone was easy to handle thanks to the good clip-on leads. Sadly, there was nothing important on the phone itself.
