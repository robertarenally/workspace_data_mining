import os
import csv

dirpath = 'datasets\classic3\med'
output = 'Classic3_med.csv'

with open(output, 'w') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(['data', 'target_names'])

    files = os.listdir(dirpath)

    for filename in files:
        lines = []
        with open(dirpath + '/' + filename) as afile:
            for line in afile.readlines():
                lines.append(line.strip())

            csvout.writerow([' '.join(lines), 'med'])
            afile.close()
    outfile.close()