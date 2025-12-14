🟥 PHASE 1 — Setup Windows Server 2019 as Domain Controller (AD DS)

Everything below happens inside Windows Server 2019 VM.

✅ STEP 1 — Set a Static IP on Windows Server 2019

AD needs a fixed IP.

1️⃣ Open:
Control Panel → Network and Internet → Network and Sharing Center
Click “Ethernet” → Properties

2️⃣ Select:
Internet Protocol Version 4 (TCP/IPv4)

3️⃣ Set:
Setting	Value
IP Address	192.168.100.5
Subnet Mask	255.255.255.0
Gateway	192.168.100.1 (or empty if NAT)
DNS Server	Set DNS to itself → 192.168.100.5

Click OK.

✅ STEP 2 — Rename the Server (Important)

Open Server Manager → Local Server → Computer Name → Change

Set name to:

DC1


Restart when asked.

🟦 STEP 3 — Install Active Directory Domain Services (AD DS)

Inside Server Manager:

1️⃣ Click:
Manage → Add Roles and Features

2️⃣ In the wizard select:

Role-based installation

Select DC1 (local server)

Install Active Directory Domain Services

3️⃣ Add required features → NEXT → INSTALL

Wait for installation to finish.

🟩 STEP 4 — Promote Server to Domain Controller

After install, a yellow flag appears → click Promote this server to a domain controller.

In the wizard:

Choose:

👉 Add a new forest

Domain Name:
redops.local


This becomes your central domain for attacks.

Enter Directory Services Restore Mode (DSRM) password:

Use something simple like:

Password@123


Click Next → Next → Install.

Server reboots.

🟧 STEP 5 — Create AD Users + OUs (Organizational Units)

After reboot:

1️⃣ Open:
Active Directory Users and Computers

2️⃣ Create OUs:

Workstations

Servers

Users

3️⃣ Create Users:
Username	Role
admin1	Domain Admin
user1	Normal User
user2	Normal User
4️⃣ Add admin1 to:
Domain Admins
Enterprise Admins
Administrators

✅ STEP 5.1 — Open Active Directory Users and Computers

Click Start

Type:

Active Directory Users and Computers


or open from Server Manager → Tools

You should see a window like:

redops.local
  |— Builtin
  |— Computers
  |— Domain Controllers
  |— Users

🟧 STEP 5.2 — Create Organizational Units (OUs)

OUs help you structure your AD like a real company.

Create 3 OUs:
✔ Users
✔ Workstations
✔ Servers
HOW TO CREATE AN OU:

Right-click redops.local

Click New → Organizational Unit

Name it:

Users

Workstations

Servers

Make sure Protect container from accidental deletion is checked.

You should end up with:

redops.local
  ├── Users
  ├── Workstations
  ├── Servers

🟨 STEP 5.3 — Create User Accounts

Now create 3 users:

admin1 → Domain Administrator

user1 → Normal user

user2 → Normal user

HOW TO CREATE A USER:

Right-click Users OU

Click New → User

Fill fields:

For admin1:
Field	Value
First name	admin
Last name	one
User logon name	admin1

Click Next

Enter password:

Password@123


⚠️ Uncheck:

User must change password at next logon

Click Finish

Repeat same steps for:

user1

user2

🟥 STEP 5.4 — Give Administrator Privileges to admin1

This gives admin1 full domain control.

1. Open:
redops.local → Users OU


Right-click admin1 → Add to a group…

Add admin1 to these groups:
Type these groups one by one:
Domain Admins
Enterprise Admins
Administrators


Press Check Names → OK.

Now admin1 is a full domain admin.
