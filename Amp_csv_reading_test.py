import csv

# filePath = '/Users/yoshionao_mbp/Documents/AnalyzingSound/data/Cluster_A_30.csv'
filePath = '/Users/yoshionao_mbp/Documents/AnalyzingSound/ex/Cluster_A_30.csv'


f = open(filePath, "r")
reader = csv.reader(f)
# header = next(reader)

for i, row in enumerate(reader):
    # print(row)
    if (i > 0):
        print(i, row[0], row[1], row[2])

f.close()