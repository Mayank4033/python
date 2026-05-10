string="""
<html>
<head><title>Mayank Santwani </title></head>
<p>
Hello ji
</p>
<ul>
<li>Mayank</li>
<li>Pakan</li>
<li>Ronak</li>
</ul>
</html>"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(string,"html.parser")
print(soup.title)
print(soup.p.text)