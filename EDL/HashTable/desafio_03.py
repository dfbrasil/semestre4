from random import randint

hash_table = {}

for id in range(1, 30):
    sensor_readings = [randint(1, 300), randint(1, 300)]
    hash_table[id] = sensor_readings

while True:
    id_sensor = int(input("Informe o id do sensor: "))
    if id_sensor in hash_table:
        print(f"Leituras recentes: {hash_table[id_sensor]}")

        print("Quer ver outro sensor?")
        print("[1] Sim \n[2] Não")
        opcao = int(input())

        if opcao == 2:
            break
    else:
        print("Este sensor não existe.")
