import requests
from bs4 import BeautifulSoup
import datetime
import time
import pymysql
#获得昨天函数
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday
    return '{}月{}日'.format(yesterday.month,yesterday.day)
#####工作方面
#工作方向
job_direction = []
#月薪
#工作名
job_name = []
money = []
#工作地点(市)
job_location_city = []
#工作地点(区)
job_location_area = []
#工作地点(路，街道)
job_location_detail = []
#工作经验
work_experience = []
#学历
education = []
##### 公司方面
#公司名称
company_name =  []
#公司规模
company_size = []
#上市情况
market = []
#####招聘信息
#时间
date = []
# https://www.zhipin.com/i100001-c101210100/?page=1&ka=page-1
# https://www.zhipin.com/i100002-c101210100/?page=1&ka=page-1
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
for page in range(1,11):
    url = 'https://www.zhipin.com/i100801-c101210100/?page={}&ka=page-{}'.format(page,page)
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text)
        #工作名
        #月薪
        #公司
    job_tag = soup.select("h3 a")
    i =0
    for index in job_tag:
        content = index.get_text(" ", strip=True)
        if i%2==0:
            job_name.append(content.split(' ')[0])
            money.append(content.split(' ')[1])
        else:
            company_name.append(content)
        i+=1


    #类型
    #是否上市
    #规模
    #学历要求
    #工作经验

    ####互联网部分
    # company_tag = soup.find_all('em',class_='vline')
    # i = 0
    # for index in company_tag:
    #     if index.find_parent('p')!=None:
    #         if i%2==0:
    #             if i %4 ==0:
    #                 content = index.find_parent('p').get_text(',')
    #                 job_direction.append(content.split(',')[0])
    #                 market.append(content.split(',')[1])
    #                 company_size.append(content.split(',')[2])
    #             else:
    #                 content = index.find_parent('p').get_text(' ').split(' ')
    #                 job_location_area.append(content[1])
    #                 job_location_detail.append(content[2])
    #                 work_experience.append(content[3])
    #                 education.append(content[4])
    #         i+=1

####电子商务
    # company_tag = soup.find_all('em',class_='vline')
    # i = 0
    # # print (company_tag)
    # for index in company_tag:
    #     # print(index.find_parent('p'))
    #     if index.find_parent('p')!=None:
    #         if i%2==0:
    #             content = index.find_parent('p').get_text(',').split(',')
    #             if content[0][0:2]=='杭州':
    #                 job_location_area.append(content[0].split(' ')[1])
    #                 job_location_detail.append(content[0].split(' ')[2])
    #                 work_experience.append(content[1])
    #                 education.append(content[2])
    #             else:
    #                 if len(content) == 2:
    #                     job_direction.append(content[0])
    #                     market.append('')
    #                     company_size.append(content[1])
    #                 else:
    #                     job_direction.append(content[0])
    #                     market.append(content[1])
    #                     company_size.append(content[2])
    #         i+=1
####游戏
    company_tag = soup.find_all('em',class_='vline')
    j = 0
    for index in company_tag:
        # print(index.find_parent('p'))
        if index.find_parent('p')!=None:
            if j%2==0:
                content = index.find_parent('p').get_text(',').split(',')
                if content[0][0:2]=='杭州':
                    job_location_area.append(content[0].split(' ')[1])
                    job_location_detail.append(content[0].split(' ')[2])
                    work_experience.append(content[1])
                    education.append(content[2])
                else:
                    if len(content) == 2:
                        job_direction.append(content[0])
                        market.append('')
                        company_size.append(content[1])
                    else:
                        job_direction.append(content[0])
                        market.append(content[1])
                        company_size.append(content[2])
            j+=1
    # print(job_location_area)
    # print(job_location_detail)
    # print(work_experience)
    # print(education)
    # print(job_direction)
    # print(market)


# print(education)
    #发布时间
    data_tag = soup.find_all('div',class_='info-publis')
    for index in data_tag:
        content = index.p.text
        if content.find('日') == -1:
            #昨天情况
            if content.find('天') !=-1:
                date.append(getYesterday())   
                #今天情况
            else:
                i = datetime.datetime.now()
                date.append('{}月{}日'.format(i.month,i.day))
        else:
            date.append(content[3:])

#####存入数据库
#数据库连接
connection = pymysql.connect(host='116.62.156.102',user='py_work',passwd='py123',db='xtl_py_database',port=3306,charset='utf8')
cs=connection.cursor()
index = 0
while (index<len(job_direction)):
    sqlInsert="insert into hz_job values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    count=cs.execute(sqlInsert,[job_direction[index],job_name[index],money[index],job_location_area[index],job_location_detail[index],work_experience[index],education[index],company_name[index],company_size[index],market[index],date[index]])
    index+=1
connection.commit()
connection.close()
