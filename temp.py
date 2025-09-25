dados = [
        {"dia": 12, "mes": 7, "ano": 2019, "temp": 30.5},
        {"dia": 18, "mes": 7, "ano": 2019, "temp": 28.5},
        {"dia": 21, "mes": 8, "ano": 2019, "temp": 25.0},
    ]
for i in dados:
    print(f'{i["dia"]}/{i["mes"]}/{i["ano"]}: Temperatura:{i["temp"]}')

