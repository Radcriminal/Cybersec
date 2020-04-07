# PowerShell cheatsheet
 
 * [Handy commands](#handy-commands)
 * [Filtering](#filtering)

## Handy commands  

### list all aliases
```powershell
Get-Alias
```

## Filtering

### select only one object

```powershell
Select-Object
```

Например, покажет только столбец Name из вывода команды Get-Alias

```powershell
Get-Alias | Select-Object Name
```
