import mercadopago
import sys

#Valor = 100
#Titulo_Produto = "CREDITO BOT STORE"
Email = "test@test.com"
Primeiro_Nome = "Test"
Ultimo_Nome = "User"
Cpf = "191191191-00"
Zip_Code = "06233-200"
Nome_Rua = "Av. das Nações Unidas"
Numero_Rua = "3003"
Complemento_Vizinhaca = "Bonfim"
Cidade = "Osasco"
Unidade_Federal = "SP"

try:
    TOKEN_MP = sys.argv[1]
    VALOR_RECARGA = sys.argv[2]
    TITULO_PRODUTO = sys.argv[3]
    
    sdk = mercadopago.SDK(TOKEN_MP)
    payment_data = {
        "transaction_amount": float(VALOR_RECARGA),
        "description": TITULO_PRODUTO,
        "payment_method_id": "pix",
        "payer": {
            "email": Email,
            "first_name": Primeiro_Nome,
            "last_name": Ultimo_Nome,
            "identification": {
                "type": "CPF",
                "number": Cpf
            },
            "address": {
                "zip_code": Zip_Code,
                "street_name": Nome_Rua,
                "street_number": Numero_Rua,
                "neighborhood": Complemento_Vizinhaca,
                "city": Cidade,
                "federal_unit": Unidade_Federal
            }
        }
    }
    payment_response = sdk.payment().create(payment_data)
    if str(payment_response["status"]) == "401":
        print("Erro ao gerar chave pix! O desenvolvedor foi notificado!")
    else:
        payment = payment_response["response"]
        Link_Copia_Cola_Pix = payment["point_of_interaction"]["transaction_data"]["qr_code"]
        iD_Pagamento = payment["id"]
        print(f"{iD_Pagamento}|{Link_Copia_Cola_Pix}")


except Exception as e:
    print(e)