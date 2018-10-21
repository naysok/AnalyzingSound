#!/bin/sh
ffmpeg -i drum_machine_30.mp3 -vn -ac 2 -ar 44100 -acodec pcm_s16le -f wav drum_machine_30.wav