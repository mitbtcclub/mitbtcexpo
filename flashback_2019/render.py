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

teamcsv = open("team.csv", "r").read()
team=[]
teamprefix="./assets/images/headshots/"
for row in csv.reader(teamcsv.split('\n'), delimiter='|'):
    row = list(row)
    if row == []:
        break
    row[0]=teamprefix+row[0]
    team.append(row)

def generateHTML(prefix):
    day1_10= []
    scsv= open(prefix + "day1_10.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        day1_10.append([time]+row[2:])

    day1_34= []
    scsv= open(prefix + "day1_34.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        day1_34.append([time]+row[2:])

    day2_10= []
    scsv= open(prefix + "day2_10.csv", "r").read()
    for row in csv.reader(scsv.split('\n'), delimiter='|'):
        if len(row) == 0:
            break
        time = row[0]+" - "+row[1]
        day2_10.append([time]+row[2:])

    sponsorprefix = "./assets/images/sponsors/"
    platinumsponsors = []
    platinumsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],platinumsponsors)
    goldsponsors = [["nash.png","Nash","http://nash.io"],["nebulous.jpg","Nebulous","https://sia.tech/"]]
    goldsponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],goldsponsors)
    silversponsors = [["chaincode.png","Chaincode", "http://www.chaincode.com"], ["zcoin.png","ZCoin","https://zcoin.io/"],["FCAT.png","Fidelity Center for Applied Technology","https://www.fidelitylabs.com/"],["stellar.png","Stellar","https://www.stellar.org/"],["algorand.png","Algorand","https://www.algorand.com/"],["accomplice.png","Accomplice","https://accomplice.co/"], ["vechain.png", "VeChain", "https://www.vechain.org"]]
    silversponsors = map(lambda x: [sponsorprefix+x[0]]+x[1:],silversponsors)
    academicpartners = [["ben.jpg", "Blockchain Education Network", "https://www.blockchainedu.org"], ["SloanBlockchain.png","http://blockchain.mit.edu/","Sloan Blockchain"],["casa.png","Casa", "https://keys.casa/"], ["dci.png","Digital Currency Initiative", "http://dci.mit.edu"]]
    academicpartners = map(lambda x: [sponsorprefix+x[0]]+x[1:],academicpartners)
    mediapartners = [["cointelegraph.png", "Cointelegraph", "https://cointelegraph.com/"],["bitcoinmag.png", "Bitcoin Magazine", "https://bitcoinmagazine.com/"]]
    mediapartners = map(lambda x: [sponsorprefix+x[0]]+x[1:],mediapartners)
    with open(prefix + "index.html", "wb") as f:
        f.write(loader.load(prefix + "index.tmpl").generate(team=team,speakers=speakers,day1_10=day1_10,day1_34=day1_34,day2_10=day2_10,platinumsponsors=platinumsponsors,goldsponsors=goldsponsors,silversponsors=silversponsors,academicpartners=academicpartners,mediapartners=mediapartners))

#generateHTML("flashback/")
generateHTML("")
