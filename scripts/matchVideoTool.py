import requests
import argparse
from pytubefix import YouTube

HEADERS = {
    'X-TBA-Auth-Key': "xgGoJmaz1XxRLpMGBF7AU16RBi1Lk48UpkLE2jMbSE0pyyTzBwyQYt1qwhc7xSk5"
}

def getVideoURL(matchKey):
    url = "https://www.thebluealliance.com/api/v3/match/" + matchKey
    videos = requests.get(url, headers=HEADERS).json()['videos']

    if len(videos) == 0:
        print("No video available")
    
    #Just grab the first video for now, some places like PNW have multiple angles so that is a future concern
    ytKeys = filterYoutube(videos)[0]['key']
    return 'http://youtube.com/watch?v='+ytKeys

def downloadVideo(url):
    try: 
        # object creation using YouTube 
        yt = YouTube(url)
    except: 
        #to handle exception 
        print("Connection Error") 
    
    # Get all streams and filter for highest resolution file. Big files are not a concern because marie does not have 4K camera money
    mp4_streams = yt.streams.get_highest_resolution()

    try: 
        # downloading the video 
        mp4_streams.download()
        print('Video downloaded successfully!')
    except: 
        print("Some Error!")

#Filter non-youtube streams out from TBA data
def filterYoutube(videos):
    filtered = []

    for video in videos:
        if video['type'] == 'youtube':
            filtered.append(video)

    if len(filtered) == 0:
        print('No youtube videos available')
    
    return filtered

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a match key.")
    parser.add_argument('matchKey')
    
    args = parser.parse_args()

    downloadVideo(getVideoURL(args.matchKey.lower()))