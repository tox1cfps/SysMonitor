import psutil
import webbrowser


def mem_info():
    mem = psutil.virtual_memory()

    print(f"\nMemória total: {mem.total / (1024**3):.2f} GB")
    print(f"Memória Disponível: {mem.available / (1024**3):.2f} GB")
    if mem.percent > 60:
        print(f"Alto uso de memória avistado: {mem.percent}%")
        webbrowser.open('https://learn.microsoft.com/pt-br/answers/questions/4220859/windows-10-consumindo-muita-mem-ria-ram')
    else:
        print(f"Memória Usada: {mem.percent}%")
