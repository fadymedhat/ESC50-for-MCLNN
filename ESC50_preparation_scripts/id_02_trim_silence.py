"""
This file is used to convert ogg format to wav for the ESC-50 dataset
make sure to configure the source and destination folders and have librosa installed before your execute this script
:: Fady Medhat
:: version 0.1
"""

import os
import librosa
from fnmatch import fnmatch


SRC_PATH = 'I:\\dataset-esc50\\ESC-50-oggtowav\\'
DST_PATH = 'I:\\dataset-esc50\\ESC-50-oggtowavtrimmed\\'


classfolder = os.listdir(SRC_PATH)
classfolder.sort()

# for each folder
# list the files in it
#   for each file
#   trim it
#   store it at the destination

for i in range(0,len(classfolder)):
    classId = i
    files = os.listdir(SRC_PATH + classfolder[i])
    files.sort()
    for name in sorted(files):

        if fnmatch(name, "*.wav"):
            y, sr = librosa.load(SRC_PATH + classfolder[i] + '\\' + name)

            # trim the zeros
            yt, index = librosa.effects.trim(y)

            # create a class folder if it does not exist
            if not os.path.exists(DST_PATH + classfolder[i]):
                os.makedirs(DST_PATH + classfolder[i])

            # save the trimmed file
            librosa.output.write_wav(DST_PATH + classfolder[i] + '\\' + name, yt, sr)

            # print the original duration and the new one
            print(librosa.get_duration(y), librosa.get_duration(yt) , max(y), max(yt))