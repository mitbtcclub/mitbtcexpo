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
    platinumsponsors = []
    platinumsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],platinumsponsors)
    goldsponsors = [["nash.png","Nash","http://nash.agency/"]]
    goldsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],goldsponsors)
    silversponsors = [["chaincode.png","Chaincode", "http://www.chaincode.com"], ["zcoin.png","ZCoin","https://zcoin.io/"],["FCAT.png","Fidelity Center for Applied Technology","https://www.fidelitylabs.com/"]]
    silversponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],silversponsors)
    academicpartners = [["dci.png","Digital Currency Initiative", "http://dci.mit.edu"], ["ben.jpg", "Blockchain Education Network", "https://www.blockchainedu.org"], ["SloanBlockchain.png","http://blockchain.mit.edu/","Sloan Blockchain"],["casa.png","Casa", "https://keys.casa/"]]
    academicpartners = map(lambda x: [sponsorprefix+x[0]]+x[1:],academicpartners)
    with open(prefix + "index.html", "wb") as f:
        f.write(loader.load(prefix + "index.tmpl").generate(speakers=speakers,day1_26=day1_26,day1_32=day1_32,day2_26=day2_26,day2_32=day2_32,platinumsponsors=platinumsponsors,goldsponsors=goldsponsors,silversponsors=silversponsors,academicpartners=academicpartners))

generateHTML("flashback/")
generateHTML("")
