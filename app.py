import flet as ft

def calcular_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main(page):
    page.title = "Calculadora de Fibonacci"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    entrada = ft.TextField(label="Número a ser calculado a sequencia de Fibonacci...", keyboard_type=ft.KeyboardType.NUMBER)
    resultado = ft.Text("Resultado:", size=20)

    def on_calcular_click(e):
        try:
            n = int(entrada.value)
            if n < 0:
                resultado.value = "Por favor, insira um número positivo."
            else:
                fib_sequence = calcular_fibonacci(n)
                resultado.value = f"Resultado Fibonacci: {fib_sequence}"
        except ValueError:
            resultado.value = "Por favor, insira um número válido."
        page.update()

    calcular_button = ft.ElevatedButton("Calcular", on_click=on_calcular_click)

    page.add(entrada, calcular_button, resultado)

ft.app(target=main)
