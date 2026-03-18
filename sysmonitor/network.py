import socket
import time

import psutil
from scapy.all import ARP, Ether, srp


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
        except Exception:
            nome = "Desconhecido"

        dispositivos.append((ip, mac, nome))

    print("IP".ljust(16), "MAC".ljust(20), "NOME")
    print("-" * 50)

    for ip, mac, nome in dispositivos:
        print(ip.ljust(16), mac.ljust(20), nome)
