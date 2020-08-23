Title: Week 32 of 2020 electronics update
Date: 2020-08-04 13:15
Category: Electronics
Tags: updates, pitemp
Slug: week-32-2020-electronics
Author: Sebastien Chiasson
Summary: I continue work on modelling pi temperatures

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

