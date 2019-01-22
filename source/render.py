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

def generateHTML(prefix):
    day1_26= []
    scsv= open(prefix + "day1_26.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        day1_26.append([time]+row[2:])
    day1_32= []
    scsv= open(prefix + "day1_32.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        panelists = "".join([x if i == 0 else ", "+x for i,x in enumerate(row[5:9]) if x != ""])
        day1_32.append([time]+row[2:5]+[panelists])

    day2_26= []
    scsv= open(prefix + "day2_26.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        day2_26.append([time]+row[2:])
    day2_32= []
    scsv= open(prefix + "day2_32.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        panelists = "".join([x if i == 0 else ", "+x for i,x in enumerate(row[5:9]) if x != ""])
        day2_32.append([time]+row[2:5]+[panelists])

    sponsorprefix = "./assets/images/sponsors/"
    platinumsponsors = [["circle.png","Circle Wallet", "https://www.circle.com/en/"]]
    platinumsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],platinumsponsors)
    goldsponsors = [["arcc.jpg","ARCC", "http://ibmr.io"], ["zkcapital.png","zkCapital", "https://zk.capital"], ["nucypher.svg","NuCypher", "https://www.nucypher.com"], ["zion.png","City of Zion", "https://cityofzion.io"], ["pillar.png", "Pillar VC", "https://pillar.vc"], ["protocol.png","Protocol Labs", "https://protocol.ai"], ["inblockchain.png", "InBlockchain", "http://www.inblockchain.com"], ["fusion.svg", "Fusion", "https://fusion.org"]]
    goldsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],goldsponsors)
    silversponsors = [["jarvis.png","Jarvis", "https://jarvis.ai"], ["shapeshift.png","Shapeshift", "https://www.shapeshift.io"], ["raptor.png","Raptor","http://www.raptorgroup.com"], ["chaincode.png","Chaincode", "http://www.chaincode.com"], ["ledger.png","Ledger Wallet", "https://www.ledgerwallet.com"], ["sia.png", "Sia", "https://siafunds.tech"], ["decred.png", "Decred", "https://decred.org"]]
    silversponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],silversponsors)
    academicsponsors = [["dci.png","Digital Currency Initiative", "http://dci.mit.edu"], ["ben.jpg", "Blockchain Education Network", "https://www.blockchainedu.org"]]
    academicsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],academicsponsors)
    with open(prefix + "index.html", "wb") as f:
        f.write(loader.load(prefix + "index.tmpl").generate(speakers=speakers,day1_26=day1_26,day1_32=day1_32,day2_26=day2_26,day2_32=day2_32,platinumsponsors=platinumsponsors,goldsponsors=goldsponsors,silversponsors=silversponsors,academicsponsors=academicsponsors))


generateHTML("flashback/")
generateHTML("")
