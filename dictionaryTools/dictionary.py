from ast import NotIn
from asyncore import write
from re import I
import exrex
import sys

# 传入host, http://demo.webic.com. demo,webic 都可能作为字典的一部分
webWhite = ['com','cn','gov','edu','org','www']   # 网站白名单

def hostPara(host):
    # 对host进行分析,处理成我们想要的格式
    if '://' in host:
        host = host.split('://')[1].replace('/','')   # 切割取后面的一部分，并将'/'替换为空
    if '/' in host:
        host = host.replace('/','')

    return host

    # 我们希望将核心规则写入配置文件,方便后期使用
'''
    fRule = open('./rule.ini','r')
    for i in fRule:    # 导入配置数据
        if '#' in i[0]:
            print(i)
            rule = i
'''
def dicCreat(hosts):
    webDics = hosts.split('.')
    # 取出有用的东西，放入字典生成

    fPassOut = open('pass_1.txt','w')    # 保存密码到文件
    fPassOut.close()

    for webDic in webDics:
        if webDic not in webWhite:   # 去掉com
            fPass = open('./passwd.txt','r')
            for dicPass in fPass:
                # 定义规则,生成字典
                dics = list(exrex.generate('{webDic}[!@#]{dicPass}'.format(webDic=webDic,dicPass=dicPass.strip('\n'))))   

                for dic in dics:
                    if len(dic) > 3:
                        fPassOut = open('pass_1.txt','a+')
                        fPassOut.write(dic+'\n') 
                        fPassOut.close()
                        print(dic)

# dicCreat(hostPara('http://www.baidu.com'))

'''
if __name__ == '__main__':
    if len(sys.argv) == 2:
        dicCreat(hostPara(sys.argv[1]))
        sys.exit(0)
    else:
        print('Usage:%s www.demo.com'%sys.argv[0])
        sys.exit(-1)
'''