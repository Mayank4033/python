terrorist_organizations = ["LET", "JEM", "HM", "IM", "United Liberation Front of Asom", "National Democratic Front of Bodoland", "People’s Liberation Army", "Communist Party of India (Maoist)"]

class bannedwords(Exception):
    pass
while True:
    try:
        domain=input("enter domain name you want to book : ")
        if domain in terrorist_organizations:
            raise bannedwords
        else:
            print(f"you can book this domain {domain}")
            break
    except bannedwords:
        print("a domain cannot be bought of this name ")