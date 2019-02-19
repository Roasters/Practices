import os
os.chdir(r'C:\Users\sjhon\Documents\PythonScripts\LB&C')

f = open('04_sample01.txt', encoding='utf-8')
text = f.readlines()
f.close() 

# 1. Search 'AI' and add \t

out = open('out.txt', 'w', encoding='utf-8') 
for line in text:
    if 'AI' in line:
        out.write(line.replace('AI', '\tAI\t'))
out.close()    


# 2. 'AI' and' '인공지능' both in line

out = open('out.txt', 'w', encoding='utf-8') 
for line in text:
    if 'AI' in line and '인공지능' in line:
        out.write(line)
out.close()        


# 3. Words of length >= 5

f = open('04_sample01.txt', encoding='utf-8')
text = f.read().split()
f.close()

out = open('out2.txt', 'w', encoding='utf-8')
out.writelines([word+'\n' for word in text if len(word) >= 5])
out.close()

out = open('out2.txt', 'w', encoding='utf-8')
for word in text:
    if len(word) >= 5:
        out.write(word+'\n')
out.close()        

# 4. Words of length>=5 with ordering number

out = open('out3.txt', 'w', encoding='utf-8')
word_list = [word for word in text if len(word) >= 5]
out.writelines([str(i+1)+'\t'+word+'\n' for i, word in enumerate(word_list)])
out.close()
 

# Without enumerate function
out = open('out3.txt', 'w', encoding='utf-8')
word_list = [word for word in text if len(word) >= 5]

i = 1
while i < len(word_list):
    out.write(str(i)+'\t'+word_list[i-1]+'\n')
    i += 1  
            
out.close()

# Without enumerate function and loop comprehension
out = open('out3.txt', 'w', encoding='utf-8')

i = 1
j = 0
while j < len(text):
    if len(text[j]) >= 5:
        out.write(str(i)+'\t'+text[j]+'\n')
        i += 1
    j += 1    
            
out.close() 

out = open('out3.txt', 'w', encoding='utf-8')
i = 0
for word in text:
    if len(word) >= 5: 
        i += 1
        out.write(str(i) + '\t' + word + '\n')
out.close()        

