from glob import glob

with open('Classic3.csv', 'w') as singleFile:
    for csvFile in glob('*.csv'):
        for line in open(csvFile, 'r'):
            singleFile.write(line)
        singleFile.write('\n')

    singleFile.close()