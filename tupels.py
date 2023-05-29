#('ihr', 'nǐmen', '你们','<img src="你.gif">','<img src="们.gif">','','')

german = open('txt/german.txt','r')
ger = german.readlines()
german.close()

chinese = open('txt/chinese.txt','r')
chi = chinese.readlines()
chinese.close()

pinyin = open('txt/pinyin.txt','r')
pin = pinyin.readlines()
pinyin.close()

for x in range(len(ger)):
    arr = ['','','','','']
    for y in range(len(chi[x].replace("\n",""))):
        #print(len(chi[x]))
        z = chi[x][y].replace("\n","")
        arr[y] = f'<img src="{z}.gif">'
    a = ger[x].replace('\n','')
    b = pin[x].replace('\n','')
    c = chi[x].replace('\n','')
    print(f"('{a}', '{b}', '{c}', '{arr[0]}', '{arr[1]}', '{arr[2]}', '{arr[3]}', '{arr[4]}'),")
    