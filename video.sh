ffmpeg -framerate 30 -start_number 0 -i Graph/drum_machine_30-%05d.png -r 30 -an -vcodec libx264 -pix_fmt yuv420p out1.mp4
