# PowerShell cheatsheet
 
 * [Handy commands](#handy-commands)
 * [Filtering](#filtering)
 * [Reading and writing information](#reading-and-writing-information)
 * [Working with files and directories](#working-with-files-and-directories)

## Handy commands  

### Get information about cmdlet
```powershell
Get-Help
```

Example
```powershell
Get-Help Select-Object
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

## Reading and writing information

### Getting text from file

```powershell
Get-Content
```

### Writing or working with data output

```powershell
Out-File
Out-Host
Out-Null
Out-String
```

For example, write information to file.txt
```powershell
Get-ChildItem | Out-File ./file.txt
```
> Or you can use Bash style: Get-ChildItem > ./file.txt

## Working with files and directories

### Creating files and directories

```powershell
New-Item -ItemType file ./file.txt
```
> To create directory do this: New-Item -ItemType directory
