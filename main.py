import psutil

def main():
    print("------MONITORAMENTO DO SISTEMA-------")

    cpu_logical = psutil.cpu_count()
    cpu_fisico = psutil.cpu_count(logical=False)
    cpu_percent = psutil.cpu_percent(interval=1)

    print(f"\nNúmero total de Núcleos: {cpu_logical}")
    print(f"Número total de Núcleos físicos: {cpu_fisico}")
    print(f"CPU Usada: {cpu_percent}%\n")

    mem = psutil.virtual_memory()

    print(f"Memória total: {mem.total / (1024**3):.2f} GB")
    print(f"Memória Disponível: {mem.available / (1024**3):.2f} GB")
    if mem.percent > 60:
        print(f"Alto uso de memória avistado: {mem.percent}%")
    else:
        print(f"Memória Usada: {mem.percent}%")

    disk = psutil.disk_usage('C:\\')

    print(f"\nEspaço total do Disco: {disk.total / (1024**3):.2f} GB")
    print(f"Espaço em uso do Disco: {disk.used / (1024**3):.2f} GB")
    print(f"Porcentagem de uso do Disco: {disk.percent}%")

    #for processo in psutil.process_iter(['pid', 'name', 'status']):
        #print(processo.info)


























































if __name__ == "__main__":
    main()