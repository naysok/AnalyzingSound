#!/usr/bin/env bash
# ffmpeg -ss [開始地点(秒)] -i [入力する動画パス] -t [切り出す秒数] [出力する動画パス]
ffmpeg -ss 0 -i output.mp4 -t 55 output_divide.mp4