# Day 9 - Linux Basics Part 1 🐧

This day focused on building core skills in Linux using the command line (WSL + Ubuntu). Covered areas include filesystem navigation, file manipulation, permissions, package management, search tools, and help documentation.

---

## 📁 Setup

```bash
mkdir -p ~/infra-lab/day9-linux-basics && cd ~/infra-lab/day9-linux-basics
```

## 🗂️ Navigation Commands
```bash
pwd           # Print current directory
ls            # List files and folders
ls -l         # Long format (permissions, size, etc.)
ls -a         # Show hidden files
cd ..         # Go up one directory
cd ~          # Go to home directory
cd -          # Switch to previous directory
tree          # Show directory tree (installed via: sudo apt install tree or snap)
```

## 📄 File & Directory Manipulation
```bash
touch file1.txt              # Create empty file
touch file2.txt              # Another empty file
mkdir myfolder               # Create folder
mv file1.txt myfolder/       # Move file1.txt into myfolder
mv myfolder/file1.txt .      # Move file1.txt back out
cp file2.txt copy2.txt       # Copy file2.txt to copy2.txt
rm copy2.txt                 # Delete copy
rm -r myfolder               # Delete myfolder and its contents
```

## 🔐 Permissions & Ownership
```bash
ls -l                        # View permissions
chmod u+x file1.txt          # Add execute for user
chmod o-r file1.txt          # Remove read for others
chmod 755 file1.txt          # rwxr-xr-x (numeric mode)
sudo chown rohan:rohan file1.txt  # Change ownership (if needed)
```

## 📦 Package Management (APT)
```bash
sudo apt update              # Refresh package list
sudo apt upgrade             # Upgrade installed packages
sudo apt install git         # Install Git
git --version                # Confirm Git installation
```

## 🔍 Search & Find
```bash
find . -name "*.txt"         # Find all .txt files
find . -type d -name "myfolder"  # Find a directory
grep "Hello" sample.txt      # Search inside file
grep -r "TODO" .             # Recursive grep
locate file1.txt             # Fast locate (after running: sudo updatedb)
```

## 📑 Help & Docs
```bash
man ls                       # Manual for command
ls --help                    # Quick help
info ls                      # Info system
man grep
grep --help
info grep
```

## ✅ Summary
Today’s session helped reinforce:

- Comfort with core Linux commands

- Practical file and directory management

- Real-world use of permissions and ownership

- Package management using APT

- Powerful search and discovery tools

- Using built-in documentation

#### This README documents all commands used and serves as a quick reference for future Linux work.