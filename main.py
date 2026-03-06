import psutil
import time

def main():

    while True:
        print("\n------MONITORAMENTO DO SISTEMA-------")

        print("\n------OPÇÕES-----")
        print("\n[1] -  CPU")
        print("[2] -  MEMORIA")
        print("[3] -  DISCO")
        print("[4] -  PROCESSOS")
        print("[5] -  INTERNET")
        print("[0] -  FECHAR")

        opcao = int(input("\nSelecione sua opção: "))

        cpu_logical = psutil.cpu_count()
        cpu_fisico = psutil.cpu_count(logical=False)
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('C:\\')
        net1 = psutil.net_io_counters()
        time.sleep(1)
        net2 = psutil.net_io_counters()

        download = net2.bytes_recv - net1.bytes_recv
        upload = net2.bytes_sent - net1.bytes_sent

        if opcao == 1:
            print(f"\nNúmero total de Núcleos: {cpu_logical}")
            print(f"Número total de Núcleos físicos: {cpu_fisico}")
            print(f"CPU Usada: {cpu_percent}%\n")  
        elif opcao == 2:
            print(f"\nMemória total: {mem.total / (1024**3):.2f} GB")
            print(f"Memória Disponível: {mem.available / (1024**3):.2f} GB")
            if mem.percent > 60:
                print(f"Alto uso de memória avistado: {mem.percent}%")
            else:
                print(f"Memória Usada: {mem.percent}%")
        elif opcao == 3:
            print(f"\nEspaço total do Disco: {disk.total / (1024**3):.2f} GB")
            print(f"Espaço em uso do Disco: {disk.used / (1024**3):.2f} GB")
            print(f"Porcentagem de uso do Disco: {disk.percent}%")
        elif opcao == 4:
            print("\nProcessos")

            for processo in psutil.process_iter(['pid', 'name', 'status']):
                print(f"\n{processo.info}")
        elif opcao == 5:
            print(f"\n{net1.bytes_sent / (1024**2):.2f} MBs Enviados")
            print(f"{net1.bytes_recv / (1024**2):.2f} MBs Recebidos")
            print(f"Download: {download / (1024**2):.2f} MB/s")
            print(f"Upload: {upload / (1024**2):.2f} MB/s")
            print("-" * 20)
        elif opcao == 0:
            print("Fechando...")
            break
        else:
            print("Opção Inválida!")
        


























































if __name__ == "__main__":
    main()