from modules.execution import ExecutionModule

def main():
    exec_mod = ExecutionModule()

    print("[+] RedOpsSim Module 1: Execution")

    print("\n[+] Running whoami")
    print(exec_mod.run_cmd("whoami"))

    print("\n[+] Running PowerShell command")
    print(exec_mod.run_powershell("Get-Date"))

    print("\n[+] Running Encoded PowerShell")
    print(exec_mod.run_encoded_powershell("Write-Output 'Encoded execution successful'"))

if __name__ == "__main__":
    main()
