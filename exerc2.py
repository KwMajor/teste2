def pertence_fibonacci(num):
    a, b = 0, 1
    fibonacci = [a, b]
    while b < num:
        a, b = b, a + b
        fibonacci.append(b)
    if num in fibonacci:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
numero = int(input("Informe o número: "))
pertence_fibonacci(numero)

