"""Entry point for SysMonitor.

This file is intentionally small and only wires up the CLI menu.
"""

from sysmonitor.ui import menu


def main():
    menu()


if __name__ == "__main__":
    main()
