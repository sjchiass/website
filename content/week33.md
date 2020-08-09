Title: Week 33 of 2020 update
Date: 2020-08-09 19:44
Category: Updates
Tags: pitemp, plants
Slug: week-33-2020
Author: Sebastien Chiasson
Summary: Progress on both rpi temperatures and cat grass manufacturing.

## Plants

### Past work

I germinated the seeds and planted them. They were slow to get going but now they're growing like, well, weeds.

Yesterday they were tiny.

![Small grass]({static}images/updates/33/20200808_080757.jpg)

Today they've grown an inch or two.

![Big grass]({static}images/updates/33/20200809_175639.jpg)

For fun I plugged in my cheap USB microscope and had a look.

Here is a closeup of the grass blade.

![Grass blade close-up]({static}images/updates/33/vlcsnap-2020-08-09-17h43m40s438.png)

The grass grows sheathed. It starts out as a white rounded stalk but opens to extend a wide green blade of grass.

![Sheath]({static}images/updates/33/vlcsnap-2020-08-09-17h48m31s086.png)

My potting soil has what I think is perlite to help aerate it. Perlite is glass turned to a light foam-like state by heat. I think it may be a bit like popcorn? I used to use a lot of it when I was playing with hydroponics.

![Perlite?]({static}images/updates/33/vlcsnap-2020-08-09-17h50m21s554.png)

### This week

I'm going to let it grow. I've wondered a little whether I should get cheap grow lights from Amazon and see if they beat my current bulb or natural sunlight. Could be interesting.

## Modelling pi temperatures

### Past work

GitHub: <https://github.com/sjchiass/pitemp>

I had been thinking a lot about the best way to get good temperature data for my raspberry pi temperature project, and it all worked out alright.

My old way of collecting data had an issue with heat building up in the case and having biased datasets for closed cases. The data was good for simulating day-to-day use, but in day-to-day use of a raspberry pi, those little plastic cases are little ovens. Here is the problematic data.

(Useful: `plt.tight_layout()` got the titles to stop writing over the other plots' axes.)

![Cases' time series]({static}images/updates/33/timeseries.png)

As you can see above, the case heats and stay hot for the duration of the test. The data isn't that great to figuring out how much heat the case dissipates. (I should come up with a measure of this bias, actually.)

The new script lets the case heat up to maximum then lets it cool down to a minimum. It waits 30 seconds before "declaring" the minimums and maximums. It does this for two hours. Here is the data. As you can see, much fairer to the closed cases.

![Cases' time series improved]({static}images/updates/33/time_series_better.png)

I was also proud of this little graph showing the minimums and maximums. Nice colors and some reference lines.

![A nice bar chart of different case temperatures]({static}images/updates/33/minmax_temps.png)

### This week

I'm going to keep cleaning up the analysis I've bundled with the code and data.

I may try the new data collection method with more case configurations, like removing the side panels. I'm also able to collect data on the heatsinks, but I haven't done that yet. Should be interesting: heatsinks probably benefit the most from fans and it'd be interesting to measure the interaction there.

## Other things

I found this interesting cheese at the store. I think it may be like the strange bottled cheese I found in Quebec truck stops. If my guess is correct, this will be very tough and salty cheese. It's not that pleasant to eat, but its saltiness satisfies junk food cravings.

Interestingly, the brand is Phoenicia, which implies this may be a kind of cheese popular in the Middle East. I found it next to the halloumi cheese.

![Cheese]({static}images/updates/33/20200809_131912.jpg)

I think I'm going to buy this $20 "DROK" volt, amp, watt and watt-hour display from Amazon and connect it to my Elenco bench power supply. It'll help me see the current draw of what I'm powering from there. I'll have to test and see if it measures properly.

![LCD meter]({static}images/updates/33/voltmeter.jpg)

Now I'll be able to measure voltage and current when playing with case fans! With only one multimeter, I can only measure or voltage at once. (And I have to move things around a bit.)

![Old setup]({static}images/updates/33/20200704_192253.jpg)
