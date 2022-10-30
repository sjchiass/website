---
title: An attempt at making a cat collar camera
date: 2022-10-23T16:00:00-04:00
tags: cats, electronics
author: Sebastien Chiasson
summary: I can get the camera onto the cat, but the cat makes it fly all over the place
---

## Overview

This is a small Raspberry Pi with a battery pack that I've tied to a cat collar.

It's fairly light but much too bukly. It's impossible to see anything when the cats move.

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/fNkZwEKi6eQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Tech

The Pi saves video to its memory card, which I then transfer over to my desktop over wifi. The battery is strong enough to keep going for hours and hours.

  * A Raspberry Pi Zero 2 W
  * A Pi Camera
  * An official Pi Zero case with the camera cover
  * A 4,000 mAh battery pack
  * Velcro straps or zip-ties to bind the setup on a cat collar.

## Stabilizing video

I was curious to see whether stabilization could recover the overly shaky footage, but it turns out that it doesn't really. I think stabilization is better for removing slight shaking. This is too extreme.

This blog post explains how to use ffmpeg to stabilize a vide: <https://www.paulirish.com/2021/video-stabilization-with-ffmpeg-and-vidstab/>

<iframe width="560" height="315" src="https://www.youtube.com/embed/mbiutvnop3A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Desoldering a Pi

I had been using my Pi Zero for my plants. I had to get rid of the GPIO pins so that the board can fit in the case.

<iframe width="560" height="315" src="https://www.youtube.com/embed/soUsj2A0lLA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
