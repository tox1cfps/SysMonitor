"""Disk-related helper functions."""

import psutil


def disk_info():
    for particao in psutil.disk_partitions():
        disk = psutil.disk_usage(particao.mountpoint)

        print(f"\nDisco: {particao.device}")
        print(f"\nEspaço total do Disco: {disk.total / (1024**3):.2f} GB")
        print(f"Espaço em uso do Disco: {disk.used / (1024**3):.2f} GB")
        print(f"Porcentagem de uso do Disco: {disk.percent}%")
