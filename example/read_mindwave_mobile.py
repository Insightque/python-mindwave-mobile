import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
import csv
import sys
import time
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='+' ,help='[DataLabel] ex) 5min_r30_g100_b50 ', dest='dataLabel')
    parser.add_argument('--addr', '-a', help='[Device Address] ex) B9:00:04:0B:4C:C4', default='B9:00:04:0B:4C:C4', dest='deviceAddr')

    dataLabel = parser.parse_args().dataLabel
    deviceAddr = parser.parse_args().deviceAddr

    return dataLabel, deviceAddr


if __name__ == '__main__':
    dataLabel, blueAddr = get_arguments()
    fileName = time.strftime("%Y%m%d%H%M%S_")+dataLabel[0]

    print('File Label:{}'.format(dataLabel))
    print('Device Address:{}'.format(blueAddr))

    with open(fileName+'.csv', mode='w') as logFileName:
        log_writer = csv.writer(logFileName, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        mindwaveDataPointReader = MindwaveDataPointReader(blueAddr)
        mindwaveDataPointReader.start()
        if (mindwaveDataPointReader.isConnected()):    
            while(True):
                dataPoint = mindwaveDataPointReader.readNextDataPoint()
                if (not dataPoint.__class__ is RawDataPoint):
                    data = str(dataPoint).split(':')
                    if( data[0] == 'delta'):
                        log_writer.writerow([time.strftime("%Y%m%d%H%M%S_")]+data)
                    else:
                        print(dataPoint)
        else:
            print((textwrap.dedent("""\
                    Exiting because the program could not connect
                    to the Mindwave Mobile device.""").replace("\n", " ")))
        
