#!/usr/bin/env bash
ffmpeg -i out1.mp4  -i data/Everything_affair.mp3 -c:v copy -c:a aac -strict experimental -map 0:v -map 1:a output.mp4
