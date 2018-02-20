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

day1= []
scsv= open("day1.csv", "r").read()
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    time = row[0]+" - "+row[1]
    day1.append([time]+row[2:])

day2= []
scsv= open("day2.csv", "r").read()
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    time = row[0]+" - "+row[1]
    day2.append([time]+row[2:])

sponsorprefix = "./assets/images/sponsors/"
platinumsponsors = [["protocol.png","Protocol Labs"]]
platinumsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],platinumsponsors)
goldsponsors = [["ares.png","Ares"]]
goldsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],goldsponsors)
silversponsors = [["pillar.png","Pillar VC"], ["jarvis.png","Jarvis"], ["shapeshift.png","Shapeshift"]]
silversponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],silversponsors)
mediasponsors = [["protocol.png","Protocol Labs"]]
mediasponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],mediasponsors)
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(speakers=speakers,day1=day1,day2=day2,platinumsponsors=platinumsponsors,goldsponsors=goldsponsors,silversponsors=silversponsors,mediasponsors=mediasponsors))
