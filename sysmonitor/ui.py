from .cpu import cpu_info
from .memory import mem_info
from .disk import disk_info
from .processes import process_info
from .network import internet_info, rede_info
from .realtime import monitor_tempo_real
from .system_info import boot_info


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
        print("[8] -  MONITOR EM TEMPO REAL")
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
