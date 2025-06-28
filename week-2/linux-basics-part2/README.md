# Day 10 - Linux Basics Part 2 🧠🐧

This session builds on Day 9 by diving deeper into essential Linux administration concepts: process management, user/group handling, networking, environment variables, and basic bash scripting.

---

## ⚙️ Process Management

```bash
ps aux                  # View all running processes
ps -ef                  # Alternative view
top                     # Live system monitor
htop                    # Better system monitor (install: sudo apt install htop)
kill <PID>              # Terminate a process
kill -9 <PID>           # Force kill
killall <name>          # Kill all processes by name

sleep 100 &             # Run in background
jobs                    # Show background jobs
fg                      # Bring job to foreground
bg                      # Resume stopped job in background
```

## 👥 User & Group Management
```bash
whoami                  # Current user
id                      # UID, GID, groups

sudo adduser testuser   # Add new user
su - testuser           # Switch to user
sudo usermod -aG sudo testuser  # Add to sudo group
groups testuser         # Show user groups

cat /etc/passwd         # User database
cat /etc/group          # Group database
```

## 🌐 Networking Commands
```bash
ip a                    # Show IP addresses
ping google.com         # Test network connectivity
hostname                # Show system name
sudo hostname mylab     # Change hostname (temporary)

curl https://example.com   # Fetch data from web
wget https://example.com   # Download web content

netstat -tuln           # View open ports (requires net-tools)
ss -tuln                # Alternative to netstat
```

## 🌱 Environment Variables
```bash
env                     # Show environment variables
printenv                # Same as above
echo $HOME              # Access specific variable

export MY_NAME="Rohan"  # Set temporary variable
echo $MY_NAME

echo 'export MY_NAME="Rohan"' >> ~/.bashrc
source ~/.bashrc        # Make it permanent
```

## 🖋️ Bash Scripting

### ✅ How to create and run a bash script

1. Create a file using the nano text editor:
```bash
nano script-name.sh
```

2. Paste your script code (examples below)

3. Save and exit:
    - Press ```Ctrl + O``` to save
    - Press ```Enter``` to confirm
    - Press ```Ctrl + X``` to exit

4. Make it executable:
```bash
chmod +x script-name.sh
```

5. Run it:
```bash
./script-name.sh
```

### 📄 ```hello.sh```
```bash
#!/bin/bash
echo "Hello, $USER!"
echo "Today is $(date)"
echo "You are in $(pwd)"
```

### 📄 ```check-user.sh```
```bash
#!/bin/bash

if [ "$USER" == "root" ]; then
  echo "You are root!"
else
  echo "You are $USER, not root."
fi
```

### 📄 ```loop.sh```
```bash
#!/bin/bash

for i in 1 2 3
do
  echo "Looping ... number $i"
done
```

## ✅ Summary

Day 10 covered:
- Process management with ```ps```, ```top```, ```kill```, and background jobs

- User and group management with ```adduser```, ```su```, ```usermod```, and ```/etc/passwd```

- Networking tools like ```ip```, ```ping```, ```curl```, ```wget```, ```netstat```, and ```ss```

- Understanding and using environment variables with ```export```, ```echo```, and ```.bashrc```

- Writing, saving, and running bash scripts step-by-step

#### This README serves as a hands-on reference for foundational Linux administration.