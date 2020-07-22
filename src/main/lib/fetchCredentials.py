import requests, json, os

# if os.path.exists('../resources/tempOrgDetails/tempOrgDetails copy.json'):
with open('../resources/tempOrgDetails/tempOrgDetails_copy.json', '+r') as f:
    pay=json.load(f)
    print(pay)

        
        # playlist = json.load(f)
        # f.seek(0)
        # f.truncate()
        # json.dump(playlist,f)

    # url = "https://pim.unbxd.io/pim-rails/api/v1/orgList"

    # payload = {}
    # headers = {
    #     'Cookie': '_un_sso_uid=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjpudWxsLCJleHBpcnkiOiIyMDIwLTA3LTI5IDE3OjEyOjQwIFVUQyIsImVtYWlsIjoibmlraGlsLm1pcmFuZGErODBAdW5ieGQuY29tIiwicmVnaW9ucyI6e319.1Kalgd19RdLVC3Zi_oz56VBSAtJXkhQkVewWKnqV9QE; JSESSIONID=O01-UztHU8IZQsyC1IT1PHxtYz_ckg4a5uRvacmI',
    #     'Content-Type': 'application/json'
    # }

    # response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text.encode('utf8'))