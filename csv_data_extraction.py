
import csv
import requests
file = open("faceexp-comparison-data-train-public.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
images = []
for row in csvreader:
    rows.append(row)
for x in rows:
    images.append(x[0])
    images.append(x[5])
    images.append(x[10])

file.close()
#
images = images[3092:]
#
with open('not_downloaded.txt', 'a') as f:
    for url in images:
        print("here")
        filename = url.split('/')[-1]
        try:
            r = requests.get(url, allow_redirects=True)
        except:
            f.write(url)
            f.write(", ")
        open(filename, 'wb').write(r.content)