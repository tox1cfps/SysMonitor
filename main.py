import psutil
import time
import datetime
import webbrowser
import platform
from scapy.all import ARP, Ether, srp
import socket
import os
import wmi

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
        print("[7] -  DISPOSITIVOS CONECTADOS")
        print("[8] - MONITOR EM TEMPO REAL")
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
        elif opcao == 7:
            rede_info()
        elif opcao == 8:
            monitor_tempo_real()
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
    for particao in psutil.disk_partitions():
        disk = psutil.disk_usage(particao.mountpoint)

        print(f"\nDisco: {particao.device}")
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

    while True:
        print("\nDeseja encerrar algum processo?")

        print("\n[1] - Sim")
        print("\n[2] - Não")

        try:
            opcao = int(input("\nSelecione sua opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            pid = input("Digite o número PID do processo: ")
            try:
                int_pid = int(pid)
                end_process(int_pid)
                break
            except ValueError:
                print("Erro: O PID deve ser um número inteiro.")
        if opcao == 2:
            break

def end_process(process_pid):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_pid == proc.info['pid']:
                print(f"Encontrado: {proc.info['name']} (PID: {proc.info['pid']})")
                
                proc.terminate()

                gone, alive = psutil.wait_procs([proc], timeout=3)

                if alive:
                    print(f"Processo {proc.info['pid']} não respondeu, forçando Kill...")
                    proc.kill()
                else:
                    print("Processo encerrado com sucesso")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


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

def rede_info():
    rede = "192.168.20.0/24"

    print("\nEscaneando rede...\n")

    arp = ARP(pdst=rede)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    pacote = ether / arp

    resultado = srp(pacote, timeout=2, verbose=False)[0]

    dispositivos = []

    for enviado, recebido in resultado:
        ip = recebido.psrc
        mac = recebido.hwsrc

        try:
            nome = socket.gethostbyaddr(ip)[0]
        except:
            nome = "Desconhecido"

        dispositivos.append((ip, mac, nome))

    print("IP".ljust(16), "MAC".ljust(20), "NOME")
    print("-" * 50)

    for ip, mac, nome in dispositivos:
        print(ip.ljust(16), mac.ljust(20), nome)

def monitor_tempo_real():
    while True:
        os.system("cls")

        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("C:")

        print("------ SYS MONITOR ------\n")

        print(f"CPU: {cpu}%")
        print(f"RAM: {mem.percent}%")
        print(f"DISCO: {disk.percent}%")

        net = psutil.net_io_counters()

        print(f"\nUpload total: {net.bytes_sent / (1024**2):.2f} MB")
        print(f"Download total: {net.bytes_recv / (1024**2):.2f} MB")

        print("\nPressione CTRL+C para sair")

        time.sleep(1)

def boot_info():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    agora = datetime.datetime.now()
    uptime = agora - boot_time

    c = wmi.WMI()
    cpu_name = "Desconhecido"

    for cpu in c.Win32_Processor():
        cpu_name = cpu.Name

    print("\n------ SISTEMA ------\n")

    print("Sistema:", platform.system())
    print("Versão:", platform.version())
    print("Arquitetura:", platform.machine())
    print("Processador:", cpu_name)

    print("\nSistema iniciado em:", boot_time)
    print("Tempo ligado:", uptime)

def main():
    menu()















if __name__ == "__main__":
    main()
