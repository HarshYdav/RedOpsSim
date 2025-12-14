# Attack Flow Explanation

This document explains the logical flow of RedOpsSim.

---

## Step 1 — Execution
The attacker achieves command execution on the victim system.
This represents phishing, macro abuse, or initial foothold.

---

## Step 2 — Discovery
The attacker enumerates:
- Current user
- Domain information
- Users and groups
- Network configuration
- Running processes

---

## Step 3 — Privilege Context Awareness
The attacker checks:
- Administrative privileges
- Token permissions
- UAC configuration
- Patch levels

No exploitation is performed at this stage.

---

## Step 4 — Data Collection
All results are collected in structured format.

---

## Step 5 — Exfiltration
Collected data is sent to the attacker machine using HTTP POST.

---

## Outcome
The attacker gains situational awareness without interacting with the victim system directly.
