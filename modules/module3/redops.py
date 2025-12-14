from modules.execution import ExecutionModule
from modules.discovery import DiscoveryModule
from modules.privesc import PrivEscModule

def main():
    print("[+] RedOpsSim Starting")

    exec_mod = ExecutionModule()
    disc_mod = DiscoveryModule()
    pe_mod = PrivEscModule()

    print("\n[+] MODULE 1: EXECUTION")
    print(exec_mod.run_cmd("whoami"))

    print("\n[+] MODULE 2: DISCOVERY")
    print(disc_mod.domain_info())

    print("\n[+] MODULE 3: PRIVILEGE ESCALATION CHECKS")

    print("\n[+] Admin Check")
    print(pe_mod.check_admin())

    print("\n[+] Token Privileges")
    print(pe_mod.whoami_privs())

    print("\n[+] UAC Status")
    print(pe_mod.uac_status())

    print("\n[+] System Information")
    print(pe_mod.system_info())

    print("\n[+] Installed Updates")
    print(pe_mod.installed_updates())

if __name__ == "__main__":
    main()
