---
title: Getting ffmpeg to generate timelapse
date: 2021-04-15T07:24:51
tags:
- linux
- timelapse
author: Sebastien Chiasson
summary: A more reliable way to get ffmpeg to work
draft: true
---

<https://stackoverflow.com/questions/3211595/renaming-files-in-a-folder-to-sequential-numbers>

```console
ls -v | cat -n | while read n f; do mv -n "$f" $(printf "%03d.jpg" "$n"); done
```

Then <https://superuser.com/a/1500049>

```console
ffmpeg -framerate 30 -i %03d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p beans.mp4
```
