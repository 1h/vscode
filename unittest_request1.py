'''
作者：大石
功能：自动生成pyunit框架下的接口测试用例
环境：python2.7.6
用法：将用户给的参数处理成对应格式,然后调用模块类生成函数，并将参数传入即可
'''

from string import Template
# 动态生成单个测试用例函数字符串


def singleMethodCreate(MethodList, interfaceNamePara):
    code = Template('''\n    def test_${testcase}(self):
        u"""${testcaseName}"""
        headers = $headers
        data = $data
        re = requests.$method(url='$url',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'返回状态码是'+s+'-'*5)
        logging.info('-'*5+'返回结果集是'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'
''')

    string = code.substitute(testcase=MethodList["testcase"], testcaseName=MethodList["TestcaseName"],
                             method=MethodList['method'], url=MethodList['url'], headers=MethodList['headers'], data=MethodList['data'],
                             )
    return string

# 拼接单个的测试用例函数字符串为完整字符串并传回主函数
# MethodParaList获取测试用例部分list


def methodCreate(MethodParaList, interfaceNamePara):
    string = ""
    for MethodPara in MethodParaList:
        string2 = singleMethodCreate(MethodPara, interfaceNamePara)
        string = string+string2
    return string

# 构造单个测试集


def singleTestsuitCreate(MethodList, parameters):
    code = Template('''suite.addTest(${className}("test_${testcase}"))''')
    string = code.substitute(
        testcase=MethodList["testcase"], className=parameters[0])
    return string

# 添加测试集


def addtestsuit(MethodParaList, interfaceNamePara):
    string = ""
    for MethodPara in MethodParaList:
        string2 = singleTestsuitCreate(MethodPara, interfaceNamePara)
        string = string+string2
    return string

# 生成测试用例类函数字符串


def modelClassCreate(parameters):
    modelCode = methodCreate(parameters[2], parameters[1])
    adtestsuit = addtestsuit(parameters[2], parameters)
    code = Template('''#coding: utf-8
"""
作者：大石
功能：待执行的接口测试用例
环境：python2.7.6
用法：通过框架自动触发调用
"""
import unittest,requests,datetime,sys,logging,BSTestRunner,time,os
from Log import Log
class ${className}(unittest.TestCase):
    u"""待测试接口：${interfaceName}"""
    def setUp(self):
        logging.info('-'*5+"begin test"+"-"*5)
    def tearDown(self):
        logging.info('-'*5+"end test"+'-'*5)
    ${model}
if __name__ == "__main__":
    #解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造测试集
    suite = unittest.TestSuite()
    ${testsuite}
    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time1=time.strftime("%H%M%S")
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #创建路径
    path='F:/test/study/yaml/test_log/'+now+"/"
    #解决多次执行时报路径已存在的错误
    try:
        os.makedirs(path)
    except:
        if path!= None:
            logging.error(u'当前路径已经存在')
    filename=path+'Report.html'
    fp=file(filename,'wb')
    #日志记录
    Log.log()
    #执行测试
    runner =BSTestRunner.BSTestRunner(stream=fp,title=u'下单平台接口测试用例',description=u'接口用例列表：')
    runner.run(suite)
    fp.close()
''')
    fileStr = code.substitute(
        className=parameters[0], interfaceName=parameters[1], testsuite=adtestsuit, model=modelCode)
    f = open(parameters[0]+".py", 'w')
    f.write(fileStr)
    f.close()
