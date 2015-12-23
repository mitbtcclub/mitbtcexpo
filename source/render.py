import StringIO
import csv

from tornado import template
loader = template.Loader(".")

scsv= open("speakers.csv", "r").read()
speakers=list(csv.reader(scsv.split('\n'), delimiter='|'))

scsv= open("day1.csv", "r").read()
day1= []
for row in csv.reader(scsv.split('\n'), delimiter=','):
	talkers = ", ".join([x for x in row[2:] if x != ""])
	day1.append([row[0],row[1],talkers])

scsv= open("day2.csv", "r").read()
day2= []
for row in csv.reader(scsv.split('\n'), delimiter=','):
	talkers = ", ".join([x for x in row[2:] if x != ""])
	day2.append([row[0],row[1],talkers])

goldsponsors = [("""./sponsors/chain.png""","Chain")]
silversponsors = [("""./sponsors/circle.png""","Circle")]
mediasponsors = [("""./sponsors/followthecoin.png""","Follow the Coin")]
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(speakers=speakers,day1=day1,day2=day2,goldsponsors=goldsponsors,silversponsors=silversponsors,mediasponsors=mediasponsors))
