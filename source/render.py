import StringIO
import csv

from tornado import template
loader = template.Loader(".")

scsv= open("speakers.csv", "r").read()
speakers=[]
speakerprefix="./assets/images/headshots/"
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    row = list(row)
    if row == []:
        break
    row[0]=speakerprefix+row[0]
    speakers.append(row)

scsv= open("day1.csv", "r").read()
day1= []
# for row in csv.reader(scsv.split('\n'), delimiter='|'):
#     time = row[0]+" - "+row[1]
#     day1.append([time]+row[2:])
#
# scsv= open("day2.csv", "r").read()
day2= []
# for row in csv.reader(scsv.split('\n'), delimiter='|'):
#     time = row[0]+" - "+row[1]
#     day2.append([time]+row[2:])

sponsorprefix = "./assets/images/sponsors/"
bitcoinsponsors = [["bitmain.png","bitmain"]]
bitcoinsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],bitcoinsponsors)
litecoinsponsors = []
litecoinsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],litecoinsponsors)
mediasponsors = []
mediasponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],mediasponsors)
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(speakers=speakers,day1=day1,day2=day2,bitcoinsponsors=bitcoinsponsors,litecoinsponsors=litecoinsponsors,mediasponsors=mediasponsors))
