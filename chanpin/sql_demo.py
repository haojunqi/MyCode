import pymysql
from flask import Flask,render_template,url_for
import json
app=Flask(__name__)
@app.route("/")
def my_tem():
#在浏览器上渲染my_templaces.html模板
    return render_template('finished_product.html')
@app.route("/数量分布")
def diqufenbu():           #大数据招聘岗位数量分布图
    return render_template('dili_demo.html')
@app.route("/薪资水平")
def xinzishuiping():
    return render_template('big_data_bar.html')
@app.route("/薪资分布")
def xinzifenbu():            #大数据岗位平均薪资分布图
    return render_template('xinzifenbu_demo.html')
@app.route("/词云")
def ciyun():
    return  render_template('big_data_ciyun.html')

#添加一个请求头得函数，由于跨域需要，
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response  #返回请求头
@app.route("/count")
#定义一个获取职位总量数据的函数
def get_count():
    conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='mydb',port=3306,charset='utf8')
    cur=conn.cursor()  #获取一个游标
    sql = """
                select*from geshengdashuju"""
    cur.execute(sql)
    see=cur.fetchall()  #展示从数据库中取出的所有数据
    json1={}
    jsonData=[]
    for i in see:
        #jsonData2={}
        jsonData.append({"name":i[0],"value":i[1]})
    #print(jsonData)
    json1['items']=jsonData
    j = json.dumps(json1)
    cur.close()
    return j
@app.route("/xinzifenbu")
    #定义一个获取大数据职位分布信息的函数
def get_bigdata_xinzifenbu():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mydb', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """
                    select*from pingjunxinzi"""
    cur.execute(sql)
    see = cur.fetchall()
    json2={}
    jsonData=[]
    for i in see:
        #jsonData2={}
        jsonData.append({"name":i[0],"value":i[1]})
    #print(jsonData)
    json2['items']=jsonData
    #print(json2)
    s = json.dumps(json2)
    cur.close()
    return s
@app.route("/bigdataxinzi")
def get_bigdata_xinzi():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mydb', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """
                        select*from dashujuxinzi"""
    cur.execute(sql)
    see = cur.fetchall()
    #print(see)
    ##print(sql)
    # print(see)
    zhiwei = []
    maxxinzi = []
    minxinzi=[]
    counts=[]
    min_pingjun=[]
    max_pingjun=[]
    jsonData = {}
    for i in see:
        #print(i)
        zhiwei.append(i[0])
        maxxinzi.append(i[1])
        minxinzi.append(i[2])
        counts.append(i[3])
        min_pingjun.append(i[4])
        max_pingjun.append(i[5])
    jsonData['zhiwei'] = zhiwei
    jsonData['maxxinzi'] = maxxinzi
    jsonData['minxinzi']=minxinzi
    jsonData['counts']=counts
    jsonData['min_p']=min_pingjun
    jsonData['max_p']=max_pingjun
    a= json.dumps(jsonData)
    #print(a)
    cur.close()
    return a
@app.route("/dataciyun")
def get_bigdataciyun():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mydb', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """
                            select*from big_dataciyun"""
    cur.execute(sql)
    see = cur.fetchall()
    #print(see)
    json3 = {}
    jsonData = []
    for i in see:
        # jsonData2={}
        jsonData.append({"name": i[0], "value": i[1]})
    # print(jsonData)
    json3['items'] = jsonData
    d = json.dumps(json3)
    cur.close()
    return d
if __name__=="__main__":
    #get_bigdataciyun()
    app.run(debug=True)