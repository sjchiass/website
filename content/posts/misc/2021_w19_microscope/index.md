---
title: Rice bug identification
date: 2021-05-11T07:53:24-04:00
tags:
- microscope
- bugs
author: Sebastien Chiasson
summary: I found some bugs in my pouches of rice, and I think I've identified them. I threw the rice away afterwards.
---

## Backstory

I had bought large pouches of rice at the start of the pandemic, having read that rices keeps very well. Unfortunately I never really eat rice so the pouches languished in storage. Doubly unfortunate, they seem to have had bugs!

The bugs appear distinct from the other bugs I found in my beans. They're thinner.

## Video

{{< youtube sJ8H56PSEHc >}}

## Setup

I have OBS studio set up to capture from my webcam, my endoscope, and my web browser.

If you're on Fedora, just enable the RPM Fusion repositories, then

```console
sudo dnf install obs-studio
```

Let the wizard auto-configure things. He told me that I could only record at 720P 30FPS. When you record, things will be dumped into an `.mkv` file in real-time. I was able to use my usual techniques to separate the audio and clean it.

## Bug description

The main things I know about the bugs are

  * They like dry grains and seem to multiply in them (where to they get moisture?)
  * They're thin, 2-3mm long
  * They've got a peculiar spiky prothorax

{{< figure caption="Screenshot of a rice bug on its back" src="bug_a.png" >}}

{{< figure caption="Live bug crawling around in rice" src="bug_b.png" >}}

{{< figure caption="Screenshot of bug on its belly, eyes and carapace visible" src="bug_c.png" >}}

## Bug identification

### Rice bugs

First, a quick Wikipedia search for "rice bug" comes up with three possibilities

> The term rice bug may apply to a number of species in at least three bug genera that attack rice: especially at the later panicle stages.

  * Genus Leptocorisa <https://en.wikipedia.org/wiki/Leptocorisa>
  * Species Oebalus Pugnax, the rice stink bug <https://en.wikipedia.org/wiki/Oebalus_pugnax>
  * Genus Stenocoris <https://en.wikipedia.org/wiki/Stenocoris>

None of these look close to our specimen.

### Rice weevils

The next quick result for rice pests is the rice weevil. Look at any photo of these and you'll see a problem: it has a huge snout! No matter how I looked at my bugs, I could not find a snout!

> The adults are usually between 3 and 4.6 mm long, with a long snout.

<https://en.wikipedia.org/wiki/Rice_weevil>

The confusing thing is that some Google Image photos of rice weevils have it without a snout. I wonder if that's just from website with inaccurate photos.

### Rice beetles

With more accurate photos it's possible to come up with other possibilities, in particular beetles. The saw-toothed grain beetle looks quite similar, but

> O. surinamensis is a slender, dark brown beetle 2.4–3 mm in size, with characteristic "teeth" running down the side of the prothorax.

<https://en.wikipedia.org/wiki/Oryzaephilus_surinamensis>

Reading that article, another candidate exists: the merchant grain beetle.

> It can be differentiated from O. surinamensis by its larger eyes and by the shape of the head, the area just behind the eyes of O. mercator is narrower than that of O. surinamensis, which has a more triangular shaped head.

<https://en.wikipedia.org/wiki/Oryzaephilus_mercator>

### Conclusion

I had beetles in my rice. I threw it all away.