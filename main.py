import psutil
import time
import datetime
import webbrowser

def menu():
    while True:
        print("\n------MONITORAMENTO DO SISTEMA-------")

        print("\n------OPÇÕES-----")
        print("\n[1] -  CPU")
        print("[2] -  MEMORIA")
        print("[3] -  DISCO")
        print("[4] -  PROCESSOS")
        print("[5] -  INTERNET")
        print("[6] -  INFO SISTEMA")
        print("[0] -  FECHAR")

        try:
            opcao = int(input("\nSelecione sua opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            cpu_info()
        elif opcao == 2:
            mem_info()
        elif opcao == 3:
            disk_info()
        elif opcao == 4:
            process_info()
        elif opcao == 5:
            internet_info()
        elif opcao == 6:
            boot_info()
        elif opcao == 0:
            print("Fechando...")
            break
        else:
            print("Opção Inválida!")
        

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


def mem_info():
    mem = psutil.virtual_memory()

    print(f"\nMemória total: {mem.total / (1024**3):.2f} GB")
    print(f"Memória Disponível: {mem.available / (1024**3):.2f} GB")
    if mem.percent > 60:
        print(f"Alto uso de memória avistado: {mem.percent}%")
        webbrowser.open('https://learn.microsoft.com/pt-br/answers/questions/4220859/windows-10-consumindo-muita-mem-ria-ram')
    else:
        print(f"Memória Usada: {mem.percent}%")

def disk_info():
    disk = psutil.disk_usage('C:\\')

    print(f"\nEspaço total do Disco: {disk.total / (1024**3):.2f} GB")
    print(f"Espaço em uso do Disco: {disk.used / (1024**3):.2f} GB")
    print(f"Porcentagem de uso do Disco: {disk.percent}%")
    
def process_info():
    print("\nProcessos")

    processos = []

    for processo in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processo.cpu_percent(interval=None)
            processos.append(processo.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        top = sorted(processos, key=lambda x: x['memory_percent'], reverse=True)[:10]

    for proc in top:
            print(
                f"{proc['name']} (PID {proc['pid']}) "
                f"| RAM: {proc['memory_percent']:.2f}%"
            )

def internet_info():
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    download = net2.bytes_recv - net1.bytes_recv
    upload = net2.bytes_sent - net1.bytes_sent

    print(f"\n{net1.bytes_sent / (1024**2):.2f} MBs Enviados")
    print(f"{net1.bytes_recv / (1024**2):.2f} MBs Recebidos")
    print(f"Download: {download / (1024**2):.2f} MB/s")
    print(f"Upload: {upload / (1024**2):.2f} MB/s")
    print("-" * 20)

def boot_info():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    agora = datetime.datetime.now()
    uptime = agora - boot_time

    print("Sistema Iniciado em:", boot_time)
    print(f"Tempo Ligado: {uptime}")

def main():
    menu()















if __name__ == "__main__":
    main()
