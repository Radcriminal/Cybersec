# PowerShell cheatsheet
 
 * [Handy commands](#handy-commands)
 * [Filtering](#filtering)

## Handy commands  

### Get information about cmdlet
```powershell
Get-Help *cmdlet*
```

### List all aliases
```powershell
Get-Alias
```

### List all attributes and methods
```powershell
Get-Member
```

For example, shows all avaliable methods and attributes for object **Name**
```powershell
Get-Alias | Select-Object Name | Get-Member
```

## Filtering

### Select only one object

```powershell
Select-Object
```

For example shows only column with **Name** objects

```powershell
Get-Alias | Select-Object Name
```

### Select only one row

```powershell
-First 1
```

For example shows only first row of **Get-Alias** command

```powershell
Get-Alias | Select-Object -Filter 1
```
> Also, there are **Last** and **Index** parameters 
