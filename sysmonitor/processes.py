"""Process management helper functions."""

import psutil


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
