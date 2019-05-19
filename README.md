# UBC Kultura Downloader
**UBC Kultura Downloader** is a script that, given the URL video stream segment served by Kultura hosted on UBC, can get all the pieces to the video, download them, and stitch them together to a full-length video.

This is a very rudimentary script for a specific use case. I anticipate it may work with other Kultura-based streams if the video is served publicly.

## Requirements

- Python 3
- `requests` package
    - Do `pip install -r requirements.txt` or `pip install requests`

## Usage

The script requires a video stream segment. For example, a URL of the form `https://streaming.video.ubc.ca/ ........  a6rb/name/a.mp4/seg-x-v1-a1.ts` where`x` is any valid segment number. You may obtain such URL by playing the video in a browser, opening up the inpect element tool, and finding the requests made by the browser. In Chrome this is under the Network tab.

Then simply execute `python3 kaltura_dl.py -url <your-url> -output <filename>`

It may be wise to place the URL and filename in quotations if you get any errors.

## Other

You may replace the base segment file name to obtain other outputs:

- `seg-x-v2-a1.ts` - Audio only
- `seg-x-v1-a2.ts` - Video only

Outputs will still be containered.