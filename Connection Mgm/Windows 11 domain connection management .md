🟦 STEP 6 — Join Windows 11 to Domain: redops.local
✅ STEP 6.1 — Set DNS on Windows 11

This is CRITICAL.
Your Windows 11 must use Windows Server 2019's IP as DNS.

If your server static IP is:

192.168.100.5


Then set Windows 11 DNS to 192.168.100.5.

Steps:

Open:

Control Panel → Network and Internet → Network and Sharing Center


Click Ethernet

Click Properties

Double-click:

Internet Protocol Version 4 (TCP/IPv4)


Set:

Setting	Value
IP Address	keep automatic (DHCP)
DNS Server	192.168.100.5 (IMPORTANT)

Click OK → Close.

🟩 STEP 6.2 — Test Connectivity with Ping

Open Command Prompt and run:

ping 192.168.100.5


You should get reply.

Then test domain name:

ping redops.local


If you get replies → DNS is working → You can join domain.

🟧 STEP 6.3 — Join the Domain

Now go to:

Settings → System → About → Rename this PC (Advanced)


A new window appears → Click:

👉 Change

Under Member of, choose:

✔ Domain

Then type:

redops.local


Click OK.

🟥 STEP 6.4 — Enter Domain Credentials

Use the admin user you created in Step 5:

Username: admin1
Password: Password@123


If DNS is correct → It will show:

👉 “Welcome to the redops.local domain”

Click OK.

🟨 STEP 6.5 — Restart the Machine

Windows 11 will ask to restart → Click Restart Now.

🟫 STEP 6.6 — Log In with Domain Account

On login screen, click:

Other User

Then enter:

redops\admin1
Password@123


Or:

admin1@redops.local


Now you're logged into the domain, not the local machine.

⭐ If everything is correct, Windows 11 is now part of AD Domain.

Your AD structure is now ready for:

Lateral movement

Kerberos attacks

Pass-the-hash

RedOpsSim simulations

Credential dumping

Ransomware simulation

Persistence

Network discovery