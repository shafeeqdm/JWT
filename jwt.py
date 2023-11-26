from jose import jwt
secret = "asfdadsgsdgasgsd"
payload = {"name":"shafeeq","age":25,}
encoded = jwt.encode(payload,secret,"HS256")
print(encoded) 
decoded = jwt.decode(encoded,secret,"HS256")
print(decoded)