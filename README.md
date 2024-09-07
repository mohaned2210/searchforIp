# DorkforIp
دورك للايبي في متصفح بينق


طريقة الاستخدام:
```
python3 dorkforipBing.py -u path/to/file -m ip
```
طريقة تحميل جميع الايبهات من شودان ووضعها في ملف

```
1 to get your IPs for shordan dork 

shodan download --limit 1000 myresults.json.gz 'DORK'

2 to print the & filter the results to live

shodan parse --fields ip_str,port --separator " " myresults.json.gz | awk '{print$1":"$2}' | httpx -o live-IPs.txt

3 to grep only ip:
grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' live-IPs.txt | sort -u > ipOnly.txt
```


```
credit: 
https://youtu.be/vFk0XtHfuSg?si=HGC_NaM180QhpJUR
https://x.com/GodfatherOrwa
chatgpt
```
