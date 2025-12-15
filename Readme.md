# RedOpsSim — Offensive Security Attack Simulation Framework

RedOpsSim is a **lab-only offensive security simulation framework** designed to demonstrate how attackers operate **after gaining initial execution** in a Windows Active Directory environment.

This project focuses on **attacker behavior**, **automation**, and **MITRE ATT&CK–aligned attack flow**, not real-world exploitation or malware development.

---

<img src =".\screenshots\discover,Token.png">


## 🎯 Project Objectives

- Simulate real-world attacker post-exploitation behavior in enterprise environments
- Demonstrate automated execution, discovery, and privilege-context awareness
- Collect and exfiltrate results to an attacker-controlled system (C2-style)
- Simulate attacker impact and malware behavior in a **safe, controlled manner**
- Bridge offensive techniques with SOC / detection understanding
- Map every activity to the MITRE ATT&CK framework


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


## 🔥 Advanced Simulation Modules (Safe & Optional)

---

### 🔹 Module 7 — Impact Simulation (Ransomware-like)
- Controlled ransomware **impact simulation**
- Operates only inside a dedicated test directory
- Renames dummy files to simulate encryption
- Drops a clear simulation ransom note
- Exfiltrates structured impact report

⚠️ **No real encryption or data damage**

**MITRE ATT&CK:**  
T1486 (Simulated)

---

### 🔹 Module 8 — Malware Behavior Simulation
- Simulates malware lifecycle behavior
- Creates infection marker file
- Collects host and user context
- Exfiltrates infection status to attacker

**MITRE ATT&CK:**  
T1059, T1105, T1119

---

### 🔹 Module 9 — Detection-Focused Ransomware Simulation (SOC View)
- Simulates ransomware detection indicators
- Rapid file-renaming activity
- Suspicious extension generation
- Produces SOC-focused detection report

Designed to demonstrate **how defenders detect ransomware**, not how attackers evade detection.

**MITRE ATT&CK:**  
T1486 (Simulated), T1119

---

## 🏗️ Lab Architecture

- **Attacker:** Kali Linux
- **Victim:** Windows 11 (Domain-joined)
- **Domain Controller:** Windows Server (Active Directory)
- **Communication:** HTTP (Lab-safe)
- **Scope:** Isolated virtual lab only


---
## 👤 Author
**Harsh**  
Aspiring SOC Analyst / Cybersecurity Specialist
