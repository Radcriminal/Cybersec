# PowerShell cheatsheet
 
 * [Handy commands](#handy-commands)
 * [Filtering](#filtering)

## Handy commands  

### List all aliases
```powershell
Get-Alias
```

## Filtering

### Select only one object

```powershell
Select-Object
```

Например, покажет только столбец Name из вывода команды Get-Alias

```powershell
Get-Alias | Select-Object Name
```

### Select only one row

```powershell
-Filter 1
```

Например, покажет только первую строку вывода

```powershell
Get-Alias | Select-Object -Filter 1
```
