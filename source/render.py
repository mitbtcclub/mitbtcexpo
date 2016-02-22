import StringIO
import csv

from tornado import template
loader = template.Loader(".")

scsv= open("speakers.psv", "r").read()
speakers=[]
speakerprefix="./assets/images/headshots/"
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    row = list(row)
    row[0]=speakerprefix+row[0]
    speakers.append(row)

scsv= open("day1.csv", "r").read()
day1= []
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    talkers = ", ".join([x for x in row[2:] if x != ""])
    day1.append(row)

scsv= open("day2.csv", "r").read()
day2= []
for row in csv.reader(scsv.split('\n'), delimiter='|'):
	talkers = ", ".join([x for x in row[2:] if x != ""])
	day2.append(row)

sponsorprefix = "./assets/images/sponsors/"
bitcoinsponsors = [["fidelity.png", "fidelity",400]]
bitcoinsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],bitcoinsponsors)
litecoinsponsors = [["bitfury.png","bitfury",300]]
litecoinsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],litecoinsponsors)
mediasponsors = []
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(speakers=speakers,day1=day1,day2=day2,bitcoinsponsors=bitcoinsponsors,litecoinsponsors=litecoinsponsors,mediasponsors=mediasponsors))
