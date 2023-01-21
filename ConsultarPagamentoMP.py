import requests,sys




#import json
#import shlex,sys,subprocess,json

#ID_Pagamento = str(sys.argv[1])
#TOKEN_MP = str(sys.argv[2])
#ID_Pagamento = "19381613063"
#TOKEN_MP = "APP_USR-6440360573202921-010718-21d6c85c58f645e82e7a9e65d33ad113-681410939"

#try:
#    cURL = f"""curl -X GET
#        'https://api.mercadopago.com/v1/payments/{ID_Pagamento}'
#        -H 'Authorization: Bearer {TOKEN_MP}'"""
#    lCmd = shlex.split(cURL)
#    p = subprocess.Popen(lCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#    out, err = p.communicate()
#except Exception as e:
#    print(e)
#
#try:
#    json_data = json.loads(out.decode("utf-8"))
#    print(json_data['status_detail'])
#    print(json_data['transaction_amount'])
#except Exception as e:
#    print(e)


try:
    ID_Pagamento = str(sys.argv[1])
    TOKEN_MP = str(sys.argv[2])
    #ID_Pagamento = "19381613063"
    #TOKEN_MP = "APP_USR-6440360573202921-010718-21d6c85c58f645e82e7a9e65d33ad113-681410939"

    url = f"https://api.mercadopago.com/v1/payments/{ID_Pagamento}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {TOKEN_MP}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    print(data["status_detail"])
    print(data["transaction_amount"])
except Exception as e:
    print(e)
