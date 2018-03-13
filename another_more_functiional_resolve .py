# coding:utf-8
import re
import urllib.request

KBListFileName = 'KBList.md'
targetFileName = 'target.txt'

def update():
    try:
        print('正在更新……')
        urllib.request.urlretrieve('https://github.com/SecWiki/windows-kernel-exploits/raw/master/README.md',
                                   KBListFileName)
        print('已更新\n')
    except:
        print("更新失败，请检查网络\n")

while True:
    operation = input('1.更新补丁列表  2.对比\n')
    if operation == '1':
        update()
    elif operation == '2':
        try:
            with open(KBListFileName, 'r', encoding='utf-8') as KBListFile:
                osVersion = input('输入操作系统（2000/XP/2003/Vista/7/8/10/...): ')
                pattern = re.compile(r'KB\d{6,7}')
                content = KBListFile.read()
                KBList = pattern.findall(content)
                with open(targetFileName, 'r', encoding='utf-8') as targetFile:
                    targetKBList = pattern.findall(targetFile.read())
                    buji = [x for x in KBList if x not in targetKBList]
                print('\n'.join(list(filter(lambda line: [KBNumber for KBNumber in buji if KBNumber in line and osVersion in line].__len__() != 0,
                       content.splitlines(keepends=False)))))
                # 函数式编程真好用
            exit(0)
        except IOError:
            print('找不到补丁列表，准备下载')
            update()

