# mitm_save_me

This is a quick and dirty `mitmproxy` script I wrote that saves literally
every file your browser comes across via HTTP request. This works well for
stuff like video streams where you get a new .ts file every five seconds.

# Why

To my surprise, there wasn't already an easy way to do this. If it was a
singular .ts file, it's trivial to just pass that to ffmpeg, but with them
being separated into individual files like some streams are, it becomes an
issue.

The usual tools like ffmpeg or youtube-dl didn't work very well for the
particular stream I was trying to capture. I also tried using the "Save as 
HAR" feature in Developer Tools on both Chromium and Firefox; this would work
well only sometimes, often leading to freezes or blank files.

# How

You'll need mitmproxy and the save_me.py script; then you can run it like so:
```
mitmproxy -s ./save_me.py
```
mitmproxy will save everything to your *current working directory*, stopping
when you kill it. The filenames are just timestamps; I wanted to avoid
detecting filetypes during HTTP data being sent so mitmproxy could "keep up"
(for lack of a better term).

# Extra

After you're done recording, you can write a script to filter through the
files. An example of this is provided in filter.sh, in which I simply check
the filetype, and if it matches .ts, it appends this result to a file.

I can then pass this file to ffmpeg like so:
```
ffmpeg -safe 0 -f concat -i list.txt -c copy out.ts
```

So far, this has worked pretty well. Just be mindful of your disk space.

# TODO:

- Configurable output directory. Could've done this from the start, not sure
  why I didn't.
- Quality of life features, such as reporting how much data has been saved
  every X seconds, etc.