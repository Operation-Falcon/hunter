import requests

def emailfinder_domain(domain, api, output):
    r=requests.get(f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api}")
    data=r.json()["data"]["emails"]
    with open(output, "w") as file:
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" %(data[i]["value"]))
                print("%s\n" %(data[i]["value"]))
            except Exception as e:
                pass

def emailpresence(domain, first, last, api, output):
    r=requests.get(f"https://api.hunter.io/v2/email-finder?domain={domain}&first_name={first}&last_name={last}&api_key={api}")
    data=r.json()["data"]
    with open(output, "w") as file:
        file.writelines("%s%s\n" % ("First Name :",data["first_name"]))
        print("%s%s\n" % ("First Name :",data["first_name"]))
        file.writelines("%s%s\n" % ("Last Name :", data["last_name"]))
        print("%s%s\n" % ("Last Name :", data["last_name"]))
        file.writelines("%s%s\n" % ("Email  :", data["email"]))
        print("%s%s\n" % ("Email  :", data["email"]))
        file.writelines("%s%s\n" % ("Linkedin  :", data["linkedin_url"]))
        print("%s%s\n" % ("Linkedin  :", data["linkedin_url"]))
        file.writelines("%s%s\n" % ("Phone Number  :", data["phone_number"]))
        print("%s%s\n" % ("Phone Number  :", data["phone_number"]))
        file.writelines("%s%s\n" % ("Company  :", data["company"]))
        print("%s%s\n" % ("Company  :", data["company"]))
        for i in range(0, len(data["sources"])):
            file.writelines("%s%s%s%s%s\n" % ("Domain :",data["sources"][i]["domain"], "  ", "Url :", data["sources"][i]["uri"]))
            print("%s%s%s%s%s\n" % ("Domain :",data["sources"][i]["domain"], "  ", "Url :", data["sources"][i]["uri"]))



def emailverify(email, api, output):
    r=requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api}")
    data1=r.json()
    with open(output, "w") as file:
        file.writelines("%s%s\n" % ("Is disposable : ", data1["data"]["disposable"]))
        print("%s%s\n" % ("Is disposable : ", data1["data"]["disposable"]))
        file.writelines("%s%s\n" % ("Is webmail : ", data1["data"]["webmail"]))
        print("%s%s\n" % ("Is webmail : ", data1["data"]["webmail"]))
        file.writelines("%s%s\n" % ("Mx records  : ", data1["data"]["mx_records"]))
        print("%s%s\n" % ("Mx records  : ", data1["data"]["mx_records"]))
        file.writelines("%s%s\n" % ("SMTP Server  : ", data1["data"]["smtp_server"]))
        print("%s%s\n" % ("SMTP Server  : ", data1["data"]["smtp_server"]))
        file.writelines("%s%s\n" % ("SMTP Check  : ", data1["data"]["smtp_check"]))
        print("%s%s\n" % ("SMTP Check  : ", data1["data"]["smtp_check"]))
        for i in range(0, len(data1["data"]["sources"])):
            file.writelines("%s%s%s%s%s\n" % ("Domain :", data1["data"]["sources"][i]["domain"], "  ", "Url :", data1["data"]["sources"][i]["uri"]))
            print("%s%s%s%s%s\n" % ("Domain :", data1["data"]["sources"][i]["domain"], "  ", "Url :", data1["data"]["sources"][i]["uri"]))


