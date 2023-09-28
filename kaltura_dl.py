import json
import os
import shutil
import argparse
import requests

temp_dir = "temp_dl"

def main(url, output_file):
    # Download all the available segments from the url.
    # Append /seg-x-v1-a1.ts, check for successful response, and save the file
    session = requests.Session()
    response = session.get(url + "/seg-1-v1-a1.ts")

    if response.status_code != 200:
        print("Invalid URL or video does not exist.")
        exit()

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    count = 1
    fileList = []
    print("Downloading pieces...")
    while response.status_code == 200:
        curr_seg = "/seg-{}-v1-a1.ts".format(count)
        response = session.get(url + curr_seg)
        with open(temp_dir + curr_seg, 'wb') as f:
            f.write(response.content)
        fileList.append(temp_dir + curr_seg)
        count += 1

    # Edge case: Last piece seems to not contain any video or audio stream
    # If the file less less than 1KB, ignore and delete it
    if os.path.getsize(fileList[-1]) < 1000:
        os.remove(fileList[-1])
        fileList = fileList[:-1]

    print("Stitching pieces...")
    with open(output_file, 'wb') as stitched:
        for filename in fileList:
            with open(os.path.join("", filename), 'rb') as part:
                shutil.copyfileobj(part, stitched)

    # Cleanup downloaded files
    for filename in fileList:
        os.remove(filename)
    if len(os.listdir(temp_dir)) == 0:
        os.removedirs(temp_dir)

    print("Done")

if __name__ == "__main__":
    # Expected input URL format:
    # https://streaming.video.ubc.ca/ ........  a6rb/name/a.mp4
    parser = argparse.ArgumentParser(description='Download and stitch UBC Kalutra videos')
    parser.add_argument('-url', action='store', dest='url', default=None, help='URL ending in .../a.mp4')
    parser.add_argument('-output', action='store', dest='output', default=None, help='Output file name')

    args = parser.parse_args()
    # Retain the url upto ".mp4"
    url = args.url[:args.url.index(".mp4") + 4]
    main(url, args.output)
