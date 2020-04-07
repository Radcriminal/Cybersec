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
