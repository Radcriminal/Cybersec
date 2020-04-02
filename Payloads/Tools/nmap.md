# Nmap cheatsheet

## Scan for vulnerabilities

```
nmap <ip_address> --script vuln
```

## Scan all or selected TCP ports

```
nmap -p- <ip_address>     //all ports
namp -p100,200,300-400    //scan for ports 100,200 and from 300 to 400
```
