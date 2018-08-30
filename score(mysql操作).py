import pymysql.cursors

#作者       Voyage
#创建时间   2018/8/30  16:01   当前系统时间
#文件       Score
#IDE       PyCharm

"""CREATE TABLE 'users' ('id' INT(11) NOT NULL AUTO_INCREMENT,    
'StuNo' INT(11) NOT NULL,    
'Age' INT(11) NOT NULL,    
'Sex' VARCHAR(255) COLLATE utf8_bin NOT NULL,  
'Name' VARCHAR(255) COLLATE utf8_bin NOT NULL,  
'Score' INT(11) NOT NULL,   
PRIMARY KEY ('id') ) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1
"""

connection = pymysql.connect (host='127.0.0.1', port=3306, user='root', password='123456', db='score',
                                  cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor ()   #获取游标

def insert():   #插入数据
    StuNo = int(input('请输入学号(后4位)'))
    if len(str(StuNo)) != 4:
        print('位数错误,请重新输入')
        return insert()
    Age = int(input ('请输入年龄(0-100)'))
    if Age < 0 or Age > 100:
        print ('输入错误,请重新输入')
        return insert ()
    Sex = input('请输入性别')
    Name = input('请输入姓名')
    Score = int(input ('请输入分数'))
    if Score < 0 or Score > 100:
        print ('输入错误,请重新输入')
        return insert ()
    value = [StuNo,Age,Sex,Name,Score]   #插入的数据列表
    sql = "INSERT INTO users (StuNo, Age,Sex,Name,Score) VALUES (%s,%s,%s,%s,%s)"  #数据插入
    cursor.execute (sql,value)
    connection.commit ()  #事务提交
    connection.close() #关闭连接
    print('插入成功')

def search():       #查询信息
    stuNo = int(input('请输入要查找的学号'))
    sql = "SELECT StuNo,Age,Sex,Name,Score FROM users WHERE StuNo='{0}'".format(stuNo)
    re = cursor.execute (sql)
    if re == 0:
        print('该学号不存在,是否添加')
    key = int(input('1.添加 2.取消'))
    if key == 1:
        return insert()
    else:
        return  None
    # result = cursor.fetchone () #查询单条数据
    # print (result)
    result = cursor.fetchall () #查询多条数据
    for data in result:
        print (data)
    connection.close()  #关闭数据连接

def update():  #更新
    stuNo = int (input ('请输入要修改的学号'))
    sqls = "SELECT StuNo FROM users WHERE StuNo = '{0}' ".format(stuNo)
    re = cursor.execute (sqls)
    if re == 0:
        print('没有该学生，请重新输入')
        return  update()
    Score = int (input ('请输入修改后的成绩'))
    if Score < 0 or Score > 100:
        print ('成绩输入错误,请重新输入')
        update ()
    sql = "UPDATE users SET Score = '{0}' WHERE StuNo = '{1}'".format(Score,stuNo)
    try:
        cursor.execute(sql)
        connection.commit()
        print('修改成功')
    except:
        connection.rollback()#回滚

def remove():
    StuNo = input('请输入你要删除的学号')
    sqls = "SELECT StuNo FROM users WHERE StuNo = '{0}' ".format (StuNo)
    re = cursor.execute (sqls)
    if re == 0:
        print ('没有该学生，请重新输入')
        return remove ()
    sql = "DELETE FROM users WHERE StuNo = '{0}'".format(StuNo)
    try:
        cursor.execute(sql)
        connection.commit()
    except:
        connection.rollback()

    print('删除成功')
    connection.close()

def show():  #显示所有信息
    sql ="SELECT StuNo,Age,Sex,Name,Score FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
    connection.close()

def sort():  #按成绩降序
    sql = "SELECT * from users ORDER BY Score DESC"
    cursor.execute (sql)
    result = cursor.fetchall ()  # 查询多条数据
    for data in result:
        print (data)
    connection.close ()  # 关闭数据连接

def main():
    print('1. 添加 2. 查找 3.修改 4. 删除 5.排序 6.显示所有信息 7.退出')
    key  = int(input('请输入'))
    if key == 1:
        insert()
    if key == 2:
        search()
    if key == 3:
        update()
    if key == 4:
        remove()
    if key == 5:
        sort()
    if key == 6:
        show()
    if key == 7:
        return None


if __name__ == '__main__':
    main()
