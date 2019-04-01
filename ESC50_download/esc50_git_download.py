import csv
import os
import shutil
from urllib import urlretrieve

DST_PATH = 'E:/ESC-50-masterTheOriginalRepoOGG/ESC-50-NewRepo'


IS_DATASET_LOCAL = False # False to download the files from the repo directly

if IS_DATASET_LOCAL == False:
    # to get the files directly from the repo uncomment the below line
    SRC_PATH = 'https://raw.githubusercontent.com/karoldvl/ESC-50/master/audio/'
else:
    # if the files are locally stored on your system
    SRC_PATH = 'E:/ESC-10-master/ESC-50/master/audio'

CSV_FILE_NAME  = "esc50.csv"

foldername_map = {'mouse_click': '402 - Mouse click', 'insects': '108 - Insects', 'crow': '110 - Crow',
                  'clapping': '303 - Clapping', 'rooster': '102 - Rooster', 'brushing_teeth': '308 - Brushing teeth',
                  'vacuum_cleaner': '407 - Vacuum cleaner', 'airplane': '508 - Airplane', 'snoring': '309 - Snoring',
                  'clock_tick': '409 - Clock tick', 'sheep': '109 - Sheep', 'siren': '503 - Siren',
                  'door_wood_creaks': '404 - Door - wood creaks', 'sneezing': '302 - Sneezing', 'frog': '105 - Frog',
                  'door_wood_knock': '401 - Door knock', 'keyboard_typing': '403 - Keyboard typing',
                  'church_bells': '507 - Church bells', 'helicopter': '501 - Helicopter', 'hen': '107 - Hen',
                  'crackling_fire': '203 - Crackling fire', 'engine': '505 - Engine', 'breathing': '304 - Breathing',
                  'can_opening': '405 - Can opening', 'drinking_sipping': '310 - Drinking - sipping',
                  'coughing': '305 - Coughing', 'fireworks': '509 - Fireworks', 'thunderstorm': '210 - Thunderstorm',
                  'rain': '201 - Rain', 'pouring_water': '208 - Pouring water', 'hand_saw': '510 - Hand saw',
                  'chainsaw': '502 - Chainsaw', 'train': '506 - Train', 'water_drops': '206 - Water drops',
                  'pig': '103 - Pig', 'glass_breaking': '410 - Glass breaking', 'crying_baby': '301 - Crying baby',
                  'clock_alarm': '408 - Clock alarm', 'cow': '104 - Cow', 'toilet_flush': '209 - Toilet flush',
                  'dog': '101 - Dog', 'car_horn': '504 - Car horn', 'cat': '106 - Cat', 'chirping_birds': '205 - Chirping birds',
                  'crickets': '204 - Crickets', 'laughing': '307 - Laughing', 'washing_machine': '406 - Washing machine',
                  'sea_waves': '202 - Sea waves', 'footsteps': '306 - Footsteps', 'wind': '207 - Wind'}


counter = 0
with open(CSV_FILE_NAME, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    headers = next(csv_reader)
    for row in csv_reader:
        store_path = os.path.join(DST_PATH, foldername_map[row[3]])
        if not os.path.exists(store_path):
            os.makedirs(store_path)

        dst = os.path.join(store_path, row[0])
        src = os.path.join(SRC_PATH, row[0])

        if IS_DATASET_LOCAL == False:
            urlretrieve(SRC_PATH + row[0], dst)
        else:
            shutil.copy2( os.path.join(SRC_PATH, row[0]), dst)

        counter += 1
        print ', '.join(row)

print counter
