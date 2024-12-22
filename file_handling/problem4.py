words=["XYZ","ABC"]
with open("D:\\c drive\\cs\Sem6\\Python-harry\\file_handling\\file2.txt","r") as f:
    
    content=f.read()
for word in words:
    
     
    content=content.replace(word,"#"*len(word))
with open("D:\\c drive\\cs\Sem6\\Python-harry\\file_handling\\file2.txt","w") as f:
    f.write(content)
print("Sucessufuly changes the words")