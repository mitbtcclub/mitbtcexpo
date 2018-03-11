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

day1_26= []
scsv= open("day1_26.csv", "r").read()
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    if len(row) == 0:
        break
    time = row[0]+" - "+row[1]
    day1_26.append([time]+row[2:])
day1_32= []
scsv= open("day1_32.csv", "r").read()
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    if len(row) == 0:
        break
    time = row[0]+" - "+row[1]
    panelists = "".join([x if i == 0 else ", "+x for i,x in enumerate(row[5:9]) if x != ""])
    day1_32.append([time]+row[2:5]+[panelists])

day2_26= []
scsv= open("day2_26.csv", "r").read()
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    if len(row) == 0:
        break
    time = row[0]+" - "+row[1]
    day2_26.append([time]+row[2:])
day2_32= []
scsv= open("day2_32.csv", "r").read()
for row in csv.reader(scsv.split('\n'), delimiter='|'):
    if len(row) == 0:
        break
    time = row[0]+" - "+row[1]
    panelists = "".join([x if i == 0 else ", "+x for i,x in enumerate(row[5:9]) if x != ""])
    day2_32.append([time]+row[2:5]+[panelists])

sponsorprefix = "./assets/images/sponsors/"
platinumsponsors = [["protocol.png","Protocol Labs"]]
platinumsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],platinumsponsors)
goldsponsors = [["arcc.png","ARCC"], ["zkcapital.png","zkCapital"], ["nucypher.svg","NuCypher"], ["zion.png","City of Zion"], ["pillar.png", "Pillar VC"], ["inblockchain.png", "InBlockchain"]]
goldsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],goldsponsors)
silversponsors = [["jarvis.png","Jarvis"], ["shapeshift.png","Shapeshift"], ["raptor.png","Raptor"], ["chaincode.png","Chaincode"], ["ledger.png","Ledger Wallet"]
]
silversponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],silversponsors)
mediasponsors = [["protocol.png","Protocol Labs"]]
mediasponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],mediasponsors)
academicsponsors = [["dci.png","Digital Currency Initiative"], ["ben.jpg", "Blockchain Education Network"]]
academicsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],academicsponsors)
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(speakers=speakers,day1_26=day1_26,day1_32=day1_32,day2_26=day2_26,day2_32=day2_32,platinumsponsors=platinumsponsors,goldsponsors=goldsponsors,silversponsors=silversponsors,mediasponsors=mediasponsors,academicsponsors=academicsponsors))
