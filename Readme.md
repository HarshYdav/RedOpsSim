# RedOpsSim — Offensive Security Attack Simulation Framework

RedOpsSim is a **lab-only offensive security simulation framework** designed to demonstrate how attackers operate **after gaining initial execution** in a Windows Active Directory environment.

This project focuses on **attacker behavior**, **automation**, and **MITRE ATT&CK–aligned attack flow**, not real-world exploitation or malware development.

---

## 🎯 Project Objectives

- Simulate real-world attacker post-exploitation behavior
- Demonstrate automated execution, discovery, and privilege analysis
- Collect and exfiltrate results to an attacker-controlled system
- Map every action to the MITRE ATT&CK framework
- Help SOC and security teams understand attacker techniques


RedOpsSim acts as a **mini command-and-control (C2) style agent** in a controlled lab.

---

## 🧩 Implemented Modules

### 🔹 Module 1 — Execution
- Automated command execution
- PowerShell and encoded PowerShell execution
- Payload delivery over HTTP

**MITRE ATT&CK:**  
T1059, T1059.001, T1027, T1105

---

### 🔹 Module 2 — Discovery
- Domain enumeration
- User and group discovery
- Network and process enumeration

**MITRE ATT&CK:**  
T1033, T1087, T1016, T1057

---

### 🔹 Module 3 — Privilege Escalation (Context Awareness)
- Admin privilege checks
- Token privilege inspection
- UAC configuration checks
- Patch awareness

**MITRE ATT&CK:**  
T1068, T1548

---

### 🔹 Module X — Output Collection & Exfiltration
- Structured result collection
- JSON-based data handling
- HTTP-based exfiltration to attacker system

**MITRE ATT&CK:**  
T1119, T1041

---

## 🏗️ Lab Architecture

- **Attacker:** Kali Linux
- **Victim:** Windows 11 (Domain-joined)
- **Domain Controller:** Windows Server
- **Communication:** HTTP (Lab-safe)

---
## 👤 Author
**Harsh**  
Aspiring SOC Analyst / Cybersecurity Specialist
