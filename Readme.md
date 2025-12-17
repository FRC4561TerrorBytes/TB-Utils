# TB-Utils

Basic scripts and evergreen utilities that are interesting and potentially useful. RIO log downloader and countdown scripts copied from Spectrum 3847

## CopyRIOLogs
To run this script, do the following steps

1. Clone the repo
2. run `pip install -r requirements.txt`
3. Type `Python scripts/CopyRIOLogs.py` into a terminal window and press enter
4. Access your data logs in folder you cloned TB-Utils into

## MatchVideoTool
To run this script, do the following steps

1. Clone the repo
2. run `pip install -r requirements.txt`
3. Type `Python scripts/matchVideoTool.py $eventKey` into a terminal window, with an event key formatted like `2025nccmp_qm75` where the event and match number and type are specified. This data is available on [TheBlueAlliance](thebluealliance.com) in the URL for the page for any match. 
4. Access your videos in folder you cloned TB-Utils into

## NTCountdown

1. Clone the repo
2. run `pip install -r requirements.txt`
3. Connect to a robot running on a real FMS or in practice mode
4. Run `Python scripts/NTCountdown.py`
5. Turn on the speakers for your laptop
6. Run through a match, you should hear a warning for 60 and 30 seconds remaining, as well as a countdown for the last 15 seconds of a match