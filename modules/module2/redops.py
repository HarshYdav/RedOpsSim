from modules.execution import ExecutionModule
from modules.discovery import DiscoveryModule

def main():
    print("[+] RedOpsSim Starting")

    exec_mod = ExecutionModule()
    disc_mod = DiscoveryModule()

    print("\n[+] MODULE 1: EXECUTION")
    print(exec_mod.run_cmd("whoami"))

    print("\n[+] MODULE 2: DISCOVERY")

    print("\n[+] Current User")
    print(disc_mod.current_user())

    print("\n[+] User Groups")
    print(disc_mod.user_groups())

    print("\n[+] Hostname")
    print(disc_mod.hostname())

    print("\n[+] Domain Information")
    print(disc_mod.domain_info())

    print("\n[+] Logged-on Users")
    print(disc_mod.logged_on_users())

    print("\n[+] Local Users")
    print(disc_mod.local_users())

    print("\n[+] Domain Users")
    print(disc_mod.domain_users())

    print("\n[+] Network Configuration")
    print(disc_mod.network_info())

    print("\n[+] Running Processes")
    print(disc_mod.processes())

if __name__ == "__main__":
    main()
