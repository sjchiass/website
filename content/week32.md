Title: Week 32 of 2020 update
Date: 2020-08-04 13:15
Category: Updates
Tags: pitemp, plants, writing
Slug: week-32-2020
Author: Sebastien Chiasson
Summary: I continue work on modelling pi temperatures, and have considered starting growing plants.

## Modelling pi temperatures

### Past work

I've been logging CPU temperatures of my Raspberry Pi 3B+ for past several weeks. I add and remove parts of its case and run tests for hours. I've put the data in OLS models to see how different components affect temperatures. I've come to realize that this kind of modelling is "descriptive" but not too explanatory. This is because the data is generated from randomly stressing the CPU with 0/25/50/75/100% load. This data can answer the question "what gets hot" but now "how much heat is evacuated by an open top"?

My problem has been that different case configurations have wildly different temperature ranges. A narrow range of temperature means less variety, and less variety means less for a model to work with. Left alone, a fully closed case will slowly work its way to 80C and stay there. This kind of data isn't great because it only shows a cluster of temperatures: the CPU throttles itself and cannot go higher, and the closed case keeps the heat inside. The added problem is that the series is not stationary either. The temperature will fluctuate at first, but when it reaches its plateau it ceases to fluctuate: the range of temperature depends on how long the test has been running.

![Cases' time series]({static}images/updates/32/timeseries.png)

My solution to this has been to add cooldown periods. Above a certain temperature, the script will make the CPU sleep until it lowers beneath a lower temperature bound. This should add some variety to closed cases since they'll now have more than one opportunity to build up heat. Note that this changes the nature of data: closed up cases will now stress the CPU less since they'll spend more of their time in cooldown. This may not not be realistic in terms of daily RaspBerry Pi use.

### This week

I'm going to keep playing with the modified script. I am only running it for open top, holed top, closed top, intake fan, and exhaust fan. Both side covers are on.

![A test underway]({static}images/updates/32/20200804_141854.jpg)

The question is: how do I best adjust the script to capture good quality time series data? It's important that the CPU is allowed to build up heat, so cooldown cycles should not be started too soon (but too high and there is never cooldown). Latent case heat should be eliminated if possible, so the CPU should cool down to a fairly low temperature (50-55C) before working again.

A bit of an annoying problem is that cases with fans neither reach high temperatures nor cool down very fast. How do I add more variety to their temperatures? I could enforce cooldowns at regular intervals, regardless of temperature. However, I should have a look at the data before going this route.

## Plants

### Past work

I've had a 5V USB water pump and a soild humidity sensor for years, but I have never used them. I had thought of buying an aquarium to make a large safe test area.

![The pump and sensors]({static}images/updates/32/20200804_141653.jpg)

### This week

I bought a small bag of potting soil and a small bag of catgrass seeds for $4 each. I'm going to start the seeds in the soil and see what happens. I'll use my daylight LED bulb as a light source. No need for special grow lights just yet!

![Cat grass seeds]({static}images/updates/32/20200804_141743.jpg)

After I've had a bit of practice, I want to try my soil humidity sensor. If that works, I can place the plants' tupperware in a bigger plastic container and start testing the USB pump.

I only want to start automating things once I'm sure the sensor and the pump work well.

Thankfully I still have a timed outlet that I can use to control the light bulb. It should work fine.

## Writing

### Past work

I've written a few things for this website but have stopped.

### This week

It's unlikely I'll stick to it, but I've started writing about logical fallacies. I think the work of writing it is good, even if it's not something I finish.

I'd also enjoy writing about Epictetus and Zen, but I'm not sure anyone would find that interesting. At least logical fallacies excite the mind.

Of course, I've also started writing these updates. (EDIT: this one has taken almost exactly one hour to write. Not bad.)

## Other things

I've modified the lighting for my electronics bench. I've moved one of the spotlights up to the top of the structure. I found that light was in the way. Light now comes from all directions.

![Well-lit lab]({static}images/updates/32/20200804_141716.jpg)

How do I find the desk lab? The easy access to the power supply and soldering station is great. The parts drawers are also convenient.

The bad part? The multimeter and its probes take up space and are always a mess.
