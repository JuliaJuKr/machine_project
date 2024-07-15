"""
Einstiegsdatei in das Machine-Project
Informationen über das Betriebssystem mit dem platform - Modul
Das ist wie ein Hauptmodul
"""

import sys
import random
from Library import infos

# import check  # das ist unser eigener Modul. Es liegt im gleichen Verzeichnis, deswegen wird es auch gefunden
# from check import hello_again


# Es werden nur Module im gleichen Verzeichnis gefunden oder die,
# die unten liegen. Wenn ein modul im oberen Verzeichnis liegt, wird es nicht gefunden
# oder gehört dem Python (Standartmodul) z.B. random
# check Namespace via Dot-Notation
# check.say_hallo()
# hello_again()
# print(sys.path)
# for key, value in sys.modules.items():
#     print(key, value)


# def main():
#     print("System Infos")
#     print(infos.operating_system())


def main():
    print("*" * 40)
    print("System Infos")
    print(infos.computer_name())  # data
    print(infos.operating_system())
    print(infos.cpu())
    print(infos.machine())
    print(infos.version())  # ('3', '11', '3')
    print(infos.implementation)
    print(infos.system)
    print("*" * 40)


main()
