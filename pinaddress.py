import requests as re
pin = 827013
df = re.get(
    "https://www.postpincode.in/api/getPostalArea.php?pincode={}".format(pin))
ab = df.json()
postofficelist = []
print(len(ab))
for o in range(len(ab)):
    postofficelist.append(ab[o]['PostOfficeAddress'])
print(postofficelist)

html_list = ''
for value in postofficelist:
    html_list += '<option value="{0}">{0}</option>'.format(value)


html = """Content-type: text/html\n

<html>
<head>
</head>
<body>
<select>
   {OPTIONS}
</select>
</body>
</html>
""".format(
       OPTIONS=html_list,
)
print(html)
