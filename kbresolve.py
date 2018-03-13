# coding:utf-8
import re
import urllib.request

KBListFileName = 'KBList.md'
targetFileName = 'target.txt'
while True:
    operation = input('1.更新补丁列表  2.对比\n')
    if operation == '1':
        try:
            print('正在更新……')
            urllib.request.urlretrieve('https://github.com/SecWiki/windows-kernel-exploits/raw/master/README.md', KBListFileName)
            print('已更新\n')
        except:
            print("更新失败，请检查网络")
    elif operation == '2':
        osVersion=input('输入操作系统（2000/XP/2003/Vista/7/8/10/...): ')
        with open(KBListFileName, 'r', encoding='utf-8') as KBListFile:
            pattern = re.compile(r'^(.*?\[KB)(\d{6,7})(\].*?)$',re.M)
            KBList = pattern.finditer(KBListFile.read())
            buji=[]
            finalresult=[]
            with open(targetFileName,'r',encoding='utf-8') as targetFile:
                pattern=re.compile(r'KB\d{6,7}')
                targetKBList=pattern.findall(targetFile.read())
                for item in KBList:
                    exsit=False
                    for item2 in targetKBList:
                        if item.group(2)==item2[2:]:
                            exsit=True
                            break
                    if not exsit:
                        buji.append(item)
            for item in buji:
                finalresult.append(''.join(item.groups()))
            for item in list(filter(lambda x: osVersion in x,finalresult)):
                print(item)
        exit()
