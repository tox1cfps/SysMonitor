import psutil
import webbrowser


def cpu_info():
    cpu_logical = psutil.cpu_count()
    cpu_fisico = psutil.cpu_count(logical=False)
    cpu_percent = psutil.cpu_percent(interval=1)

    print(f"\nNúmero total de Núcleos: {cpu_logical}")
    print(f"Número total de Núcleos físicos: {cpu_fisico}")
    if cpu_percent > 90:
        print(f"Alto uso de CPU Avistado: {cpu_percent}")
        webbrowser.open('https://www.avg.com/pt/signal/fix-high-cpu-usage')
    else:
        print(f"CPU Usada: {cpu_percent}%\n")

    while True:
        print("Deseja ver todos os núcleos?: ")
        print("[1] - Sim")
        print("[2] - Não")

        try:
            opcao = int(input("\nSelecione sua opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            print("\nUso por núcleo:")

            for i, porcentagem in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f"Core {i}: {porcentagem}%")
            break
        if opcao == 2:
            break
