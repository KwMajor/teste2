def inverter_string(s):
    string_invertida = ""
    tamanho = len(s)

    for i in range(tamanho - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida 

string_original = input("Informe uma string para inverter: ")

resultado = inverter_string(string_original)

print("String original:", string_original)
print("String invertida:", resultado)
