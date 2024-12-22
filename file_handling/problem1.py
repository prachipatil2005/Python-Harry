f=open("D:\\c drive\\cs\\Sem6\\Python-harry\\file_handling\\poem.txt")
content=(f.read())
if("twinkle" in content):
    print("twinkle  is present in the content")
else:
    print("twinkle is not present in content")
f.close()