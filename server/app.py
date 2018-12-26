import csv
import pymysql
import numpy as np
import pandas as pd
import re
from flask import Flask
import pymysql
import json
from flask_cors import CORS
from flask import make_response
app = Flask(__name__)
def isNaN(num):
    return num != num
### 查询数据库表并写入csv文件
connection = pymysql.connect(host='116.62.156.102',user='py_work',passwd='py123',db='xtl_py_database',port=3306,charset='utf8')
sqlSelect = 'select * from hz_job'
cr = connection.cursor()
with open('/Users/xtl/Desktop/大学/大三上/python/py文件/hz_job.csv','w',newline='') as filerWriter:
    fw = csv.writer(filerWriter)
    header = ['job_id','job_direction','job_name','money','job_location_area','job_location_detail','work_experience','education','company_name','company_size','market','date']
    fw.writerow(header)
    cr.execute(sqlSelect)
    rows = cr.fetchall()
    for i in rows:
        print(i)
        fw.writerow(i)

####导出csv为dataframe

#header=0。头部为表字段
count = 0
flag = 0
df = pd.DataFrame(pd.read_csv('/Users/xtl/Desktop/大学/大三上/python/py文件/hz_job.csv',header=0))
##杭州所有行业平均工资
for index in df.money:
    #匹配至少一个数字
    if isinstance(index,str):
        pattern = re.compile(r'\d+')   # 查找数字
        result = pattern.findall(index)
        if len(result) == 2:
            flag+=1
            count += int(result[0])
            count += int(result[1])
avg_money = count/(flag*2)
# print(avg_money)
##

##杭州各区工作机会分布
location_area = {}
location_result = []
for index in df.job_location_area:
    #判断是否存在该地点，存在则加1，不存在创建
    if index == None:
        print('YES')
    if index in location_area:
        location_area[index]+=1
    else:
        location_area[index]=1
for item in location_area:
    #跳过空值
    if isNaN(item):
        continue
    location_result.append({'location':item,'number':location_area[item]})
print(location_result)
##

##杭州工作机会分布(具体) nan 为未填写
location_detail = {}
detail_result = []
for index in df.job_location_detail:
    #判断是否存在该地点，存在则加1，不存在创建
    if index in location_detail:
        location_detail[index]+=1
    else:
        location_detail[index]=1
# print(location_detail)
for item in location_detail:
    #跳过空值
    if isNaN(item):
        continue
    detail_result.append({'detail':item,'number':location_detail[item]})
##


##发布工作较多的月份 数据存疑
month = {}
month_result = []
for index in df.date:
    #去除具体日期
    index=index[0:2]
    #判断是否存在该月份
    if index in month:
        month[index]+=1
    else:
        month[index]=1
for item in month:
    month_result.append({'month':item,'number':month[item]})
##

##学历要求
education = {}
education_result = []
for index in df.education:
    #判断是否存在该地点，存在则加1，不存在创建
    if index in education:
        education[index]+=1
    else:
        education[index]=1
# print(education)
for item in education:
    education_result.append({'education':item,'number':education[item]})
##

##工作经验要求
work_experience = {}
work_result = []
for index in df.work_experience:
    #判断是否存在该地点，存在则加1，不存在创建
    if index in work_experience:
        work_experience[index]+=1
    else:
        work_experience[index]=1
for item in work_experience:
    work_result.append({'work_experience':item,'number':work_experience[item]})
# print(work_experience)
##


##职位数量分布
job_direction = {}
direction_result = []
for index in df.job_direction:
    #判断是否存在该地点，存在则加1，不存在创建
    if index in job_direction:
        job_direction[index]+=1
    else:
        job_direction[index]=1
for item in job_direction:
    direction_result.append({'job_direction':item,'number':job_direction[item]})
##

##职位名称
job_name = {}
name_result = []
for index in df.job_name:
    #判断是否存在该地点，存在则加1，不存在创建
    if index in job_name:
        job_name[index]+=1
    else:
        job_name[index]=1
for item in job_name:
    name_result.append({'job_name':item,'number':job_name[item]})
##



CORS(app, resources=r'/*')
@app.route('/api',methods=['GET','POST'])
def getAllData():
    resultDict = {'avg_money':avg_money,'job_name':name_result,'job_direction':direction_result,'work_experience':work_result,'education':education_result,'month':month_result,'location_detail':detail_result,'location_area':location_result}
    response = make_response(json.dumps(resultDict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

    
if __name__ == '__main__':
    app.run()