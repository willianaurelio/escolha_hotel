# importando bibliotecas para manipulação de datas em python
from datetime import timedelta, date


# variaveis dos hoteis
hotel = ["Lakewood", "Bridgewood", "Ridgewood"]
hotel_escolhido = ""
conta_hotel_l = 0
conta_hotel_b = 0
conta_hotel_r = 0
menor_valor = 10000000
nota_hote_l = 3
nota_hote_b = 4
nota_hote_r = 5


# dados de entrada do tipo de usuário
print("Digite o seu nívem de usuário:")
print("reward -> (Já fidelizado)")
print("regular -> (Ainda não fidelizou)")
user = input()

# dados para entrada da data de hospedágem
days_origin = int(input("Digite quantos dias você pretende se hospedar: "))
print("Digite a data que você pretende entrar: ")
day = int(input("Dia: "))
month = int(input("Mês: "))
year = int(input("Ano: "))

# manipulação das datas
data_origin = date(year, month, day)
data = data_origin
index_week = data.isoweekday()


# Hotel Lakewood - estadia
i = 0
days = days_origin
data = data_origin
index_week = data.isoweekday()
if user == "reward":
    for i in range(days):

        # final_de_semana
        if index_week == 6 or index_week == 7:
            conta_hotel_l = conta_hotel_l + 80
        # dia_de_semana
        if index_week == 1 or index_week == 2 or index_week == 3 or index_week == 4 or index_week == 5:
            conta_hotel_l = conta_hotel_l + 80

        data = data + timedelta(days=1)
        index_week = data.isoweekday()
        i = i - 1

if user == "regular":
    for i in range(days):
        # final_de_semana
        if index_week == 6 or index_week == 7:
            conta_hotel_l = conta_hotel_l + 90
        # dia_de_semana
        if index_week == 1 or index_week == 2 or index_week == 3 or index_week == 4 or index_week == 5:
            conta_hotel_l = conta_hotel_l + 110

        data = data + timedelta(days=1)
        index_week = data.isoweekday()
        i = i - 1


# Hotel Bridgewood - estadia
i = 0
days = days_origin
data = data_origin
index_week = data.isoweekday()
if user == "reward":
    for i in range(days):

        # final_de_semana
        if index_week == 6 or index_week == 7:
            conta_hotel_b = conta_hotel_b + 50
        # dia_de_semana
        if index_week == 1 or index_week == 2 or index_week == 3 or index_week == 4 or index_week == 5:
            conta_hotel_b = conta_hotel_b + 60

        index_week = data.isoweekday()
        data = data + timedelta(days=1)
        i = i - 1

if user == "regular":
    for i in range(days):
        # final_de_semana
        if index_week == 6 or index_week == 7:
            conta_hotel_b = conta_hotel_b + 110
        # dia_de_semana
        if index_week == 1 or index_week == 2 or index_week == 3 or index_week == 4 or index_week == 5:
            conta_hotel_b = conta_hotel_b + 160

        data = data + timedelta(days=1)
        index_week = data.isoweekday()
        i = i - 1

# Hotel Ridgewood - estadia
i = 0
days = days_origin
data = data_origin
index_week = data.isoweekday()
if user == "reward":
    for i in range(days):

        # final_de_semana
        if index_week == 6 or index_week == 7:
            conta_hotel_r = conta_hotel_r + 40
        # dia_de_semana
        if index_week == 1 or index_week == 2 or index_week == 3 or index_week == 4 or index_week == 5:
            conta_hotel_r = conta_hotel_r + 150

        index_week = data.isoweekday()
        data = data + timedelta(days=1)
        i = i - 1

if user == "regular":
    for i in range(days):
        # final_de_semana
        if index_week == 6 or index_week == 7:
            conta_hotel_r = conta_hotel_r + 100
        # dia_de_semana
        if index_week == 1 or index_week == 2 or index_week == 3 or index_week == 4 or index_week == 5:
            conta_hotel_r = conta_hotel_r + 220

        data = data + timedelta(days=1)
        index_week = data.isoweekday()
        i = i - 1


# validação do menor valor
if menor_valor > conta_hotel_l:
  menor_valor = conta_hotel_l
  hotel_escolhido = hotel[0]

if menor_valor > conta_hotel_b:
  menor_valor = conta_hotel_b
  hotel_escolhido = hotel[1]

if menor_valor > conta_hotel_r:
  menor_valor = conta_hotel_r
  hotel_escolhido = hotel[2]


print("Hotel:", hotel_escolhido)
