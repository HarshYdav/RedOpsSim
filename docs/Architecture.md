# RedOpsSim Architecture

RedOpsSim is designed as a modular attack simulation framework.

## Components

### Attacker System
- Kali Linux
- Hosts:
  - Payload delivery server
  - Exfiltration listener (C2-like)

### Victim System
- Windows 11
- Domain-joined to Active Directory
- Executes RedOpsSim agent

### Communication
- HTTP-based
- JSON payloads
- One-way exfiltration (victim → attacker)

---

## Design Philosophy

- Minimal dependencies
- Use of native OS tools (LOLBins)
- Clear separation of attack stages
- Emphasis on detection understanding

---

## Security Considerations

- No persistence mechanisms enabled by default
- No destructive actions
- Explicit lab-only usage
