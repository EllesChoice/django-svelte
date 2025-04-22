import requests
import datetime

# Takes string IpAddress and returns json
def IPLookup(IpAddress):

    IPInfoURL = f"http://ip-api.com/json/{IpAddress}"

    return requests.get(IPInfoURL).json()

# Funktion som gör ett anrop mot en url
def GetRequestHittaPunktSE(fullName):
    
    # f"https://www.hitta.se/sök?vad={fullName}"
    baseURL = f"https://api.hitta.se/autocomplete/v3/{fullName}?app_new=5&within=55:10,69:25&where=Vallda&includeProduct=true&customers=2&geo.ip=true"

    print(f"Making request to: {baseURL}\n")

    source = requests.get(baseURL)

    if source.status_code == 200:

        print(source.json())
    else:
        print("Somehing went wrong")

# Funktion bygger träd struktur
def MaintainsTreeStructure(structurePart):

    NameAddress = structurePart[0]["name"].split(",", 1)
    Address = NameAddress[1].strip().split(" ", 1)[0]

    FullName = NameAddress[0]
    FirstName = FullName.split(" ", 1)[0]
    LastName = FullName.split(" ", 1)[1]

    structure = {
        "personal_identity_no": "19700101-7566",
        "status": "N",
        "protected_identity": False,
        "date_added": datetime.datetime.now(),
        "changed_date": datetime.datetime.now(),
        "first_name": FirstName,
        "middle_name": "middle name",
        "last_name": LastName,
        "full_name": FullName,
        "land_code": "+46",
        "co_address": "DUMMY C/Oaddress",
        "street_address": Address,
        "postal_code": structurePart[0]["zip"],
        "area_code": "area code",
        "city": structurePart[0]["city"],
        "phone_no": "phone number",
        "mobile_no": "mobile phone",
        "longitude": structurePart[0]["coordinates"][0],
        "latitude": structurePart[0]["coordinates"][1]
    }
    
    return structure