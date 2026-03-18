import datetime
import platform

import psutil
import wmi


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
