"""
KOMMT IN PCAP VOR !!!! WICHTIG!!!!
"""

import platform


def computer_name():
    print("""The networkname of the computer""")
    return platform.node()


def operating_system():
    print("operating system of machine:")
    return platform.platform()


def cpu():
    print("cpu")
    return platform.processor()


def machine():
    print("machine")
    return platform.machine()


def version():
    print("version")
    return platform.python_version_tuple()


def implementation():
    print("implementation")
    return platform.python_implementation()


def system():
    print("system")
    return platform.system(), platform.version()
