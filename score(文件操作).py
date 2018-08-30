import json

#作者       Voyage
#创建时间   2018/8/30  16:01   当前系统时间
#文件       Score
#IDE       PyCharm


class Student():   #学生类
    def __init__(self):
        self.name = ''
        self.no = ''
        self.age = ''
        self.sex = ''
        self.score = ''

    def get_message(self):   #返回所有信息
        filename = 'data.json'
        li = []
        with open (filename, 'r', encoding='utf-8') as f:
            r = f.readlines ()
            for i in r:
                li.append(json.loads (i))  # 转化成字典格式
        return li

    def add(self):   #添加，将数据写入json文件
        dic = {}
        name = input('请输入姓名：')  #将信息存放到字典中
        while True:
            if is_Chinese(name) ==False:
                print('请重新输入，中文')
                print ('-' * 60)
                name = input ('请输入姓名：')
            else:
                dic['姓名'] = name
                break

        no = input ('请输入学号(后4位):')
        list = self.get_message()       #返回所有信息
        while True:
            for dict in list:       #判断学号是否已存在
                if dict['学号'] == no:
                    print('该学号已存在,请重新输入')
                    no = input ('请输入学号(后4位):')
                else:
                    continue
            if len(no) != 4 or not no.isdigit():
                print('输入错误，请重新输入')
                print ('-' * 60)
                no = input ('请输入学号(后4位):')
            else:
                dic['学号'] = no
                break

        age = input ('请输入年龄:')
        while True:
            try:
                if int(age) <0 or int(age) >100:
                    print('年龄输入错误，请重新输入')
                    age = input ('请输入年龄:')
                else:
                    dic['年龄'] = age
                    break
            except ValueError:
                print('请输入数字,重新输入信息')
                print ('-' * 60)
                age = input ('请输入年龄:')

        sex = input ('请输入性别:')
        while True:
            if not is_sex(sex):
                print('输入错误,重新输入')
                print ('-' * 60)
                sex = input ('请输入性别:')
            else:
                dic['性别'] = sex
                break

        score = input ('请输入成绩:')
        while True:
            try:
                if int(score) <0 or int(score) >100:
                    print('成绩输入错误，请重新输入')
                    print ('-' * 60)
                    score = input ('请输入成绩:')
                else:
                    dic['分数'] = score
                    break
            except ValueError:
                print('请输入数字,重新输入信息')
                print ('-' * 60)
                score = input ('请输入成绩:')

        filename = 'data.json'
        with open(filename,'a',encoding='utf-8') as f:   #encoding设置编码
            f.write(json.dumps(dic,ensure_ascii=False)) #ensure_ascii=False 禁止使用unicode编码
            f.write('\n')
        print('添加成功！！！')
        temp = int(input ('1.继续添加 2.返回主页面 3.退出(任意键)'))
        if temp == 1:
            return self.add()
        elif temp == 2:
            return main()
        else:
            return  None


    def show(self): #显示所有信息
        filename = 'data.json'
        with open(filename,'r',encoding='utf-8') as f:
            r = f.readlines()     #r为列表，如果没有长度则说明为空
            if not len(r):  #判断是否存在学生信息
                print('暂无学生信息')
                return None
            print('-'*74)
            for i in r:
                print(json.loads(i))    #转化成字典格式
        print ('-' * 74)
        temp = int (input ('1.返回主页面 2.退出(任意键)'))
        if temp == 1:
            return main ()
        else:
            return None

    def search(self):    #查找
        filename = 'data.json'
        key = input ('请输入要查找的学号:')
        temp = 0
        with open (filename, 'r',encoding="utf-8") as f:
            r = f.readlines ()          #读取文件内容
            for i in r:
                data = json.loads(i)    #将每条信息转换成dict格式
                if data['学号'] == key:  #判断是否相等
                    temp = 1
                    print('-'*60)
                    for ke in data:      #如果相等，直接输出该条内容的所有信息
                        print(ke,':',data[ke])
        if temp == 0:
            print('找不到该同学!')
        print ('-' * 74)
        temp = int (input ('1.返回主页面 2.退出(任意键)'))
        if temp == 1:
            return main ()
        else:
            return None

    def update(self):   #修改成绩
        da = []
        filename = 'data.json'
        key = input ('请输入要修改的学号:')
        temp = 0
        with open(filename,'r',encoding="utf-8") as f:
            r = f.readlines ()   #读取文件内容
            for i in r:
                data = json.loads(i)    #转换成dict格式
                if data['学号'] != key:  #不存在的时候，直接添加到新列表
                    da.append (data)
                    continue
                if data['学号'] == key:  #存在的时候，输入修改的成绩然后追加到新列表中
                    temp = 1
                    data['分数'] = input('输入修改后的成绩:')
                    da.append(data)
        if temp == 0:
            print('找不到该学生')
            return None
        with open(filename,'w',encoding="utf-8") as f:
            f.truncate ()               #清空文件内容
            for d in da:
                f.write(json.dumps(d))   #重新将新列表写入文件
                f.write('\n')
        print('修改成功')
        print ('-' * 74)
        temp = int (input ('1.返回主页面 2.退出(任意键)'))
        if temp == 1:
            return main ()
        else:
            return None

    def remove(self):  #删除
        da = []
        filename = 'data.json'
        te = 0
        key = input ('请输入要删除的学号:')
        with open (filename, 'r',encoding="utf-8") as f:
            r = f.readlines ()
            for i in r:
                data = json.loads (i)
                if data['学号'] != key:  #如果不是要删除的学生，则将内容保存到新的列表中
                    da.append (data)
                    continue
                if data['学号'] == key:  #如果是要删除的学生，则提示是否要删除，然后continue直接略过该学生，不保存到新列表
                    print('-'*50)
                    print(data)
                    temp = input ('确定?(y/n):')  #最后将新列表写入原文件中
                    if temp == 'n' or temp == 'N':
                        print('取消成功')
                        return None
                    if temp =='y' or temp == 'Y':
                        te = 1
                        continue
                    else:
                        da.append (data)
                        continue
        if te == 0:
            print('找不到该学生')
            return None
        with open (filename, 'w',ensure_ascii=False) as f:  # 重新将内容写入文件
            f.truncate ()
            for d in da:
                f.write (json.dumps (d))
                f.write ('\n')
        print('删除成功')
        print ('-' * 74)
        temp = int (input ('1.返回主页面 2.退出(任意键)'))
        if temp == 1:
            return main ()
        else:
            return None

    def sort(self): #排序
        filename = 'data.json'
        list = []  #存放成绩的列表
        li = []   #对成绩进行排序后，根据成绩一个个将字典按list列表的顺序取出来
        list1= []  #同上
        li1 = []
        print('1.按分数降序 2.按学号降序')
        temp = int(input('请输入:'))
        if temp !=1 and temp != 2:
            print('输入错误')
            return None
        if temp == 1:    #判断语句
            with open (filename, 'r',encoding="utf-8") as f:
                r = f.readlines ()    #读取内容
                for i in r:
                    data = json.loads (i)   #str转换成dict格式
                    list.append(data['分数']) #追加到list中
            list.sort(reverse=True)  #对列表进行降序
            # print(list)
            print('-'*75)
            with open (filename, 'r',encoding="utf-8") as f:
                r = f.readlines ()
                for j in range (len (list)):    #进行list长度次循环，对应成绩降序一个个将字典追加到li列表中
                    for i in r:
                        data = json.loads (i)
                        if data['分数']  == list[j]:
                            li.append(data)
            for ii in li:
                print(ii)
        if temp == 2:
            with open (filename, 'r',encoding="utf-8") as f:
                r = f.readlines ()
                for i in r:
                    data = json.loads (i)
                    list1.append(data['学号'])
            list1.sort(reverse=True)
            # print(list1)
            print ('-' * 75)
            with open (filename, 'r',encoding="utf-8") as f:
                r = f.readlines ()
                for j in range (len (list1)):
                    for i in r:
                        data = json.loads (i)
                        if data['学号']  == list1[j]:
                            li1.append(data)
            for ii in li1:
                print(ii)
        print ('-' * 74)
        temp = int (input ('1.返回主页面 2.退出(任意键)'))
        if temp == 1:
            return main ()
        else:
            return None

def is_sex(sex):   #判断输入的是男或者是女
    if sex == '男' or sex == '女':
        return True
    else:
        return False

def is_Chinese(word): #判断输入的是否为汉字
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def main():
    print('-'*30,'成绩管理系统1.0','-'*30)
    print('1.添加   2.显示所有信息   3.查找   4.修改   5.删除   6.排序   7.退出')
    print ('-' * 76)
    stu = Student()
    while True:
        try:
            key = int (input ('请输入:'))
        except ValueError:
            print('请输入数字')
            continue
        if key == 1:
            stu.add()
            break
        elif key == 2:
            stu.show()
            break
        elif key == 3:
            stu.search()
            break
        elif key == 4:
            stu.update()
            break
        elif key == 5:
            stu.remove()
            break
        elif key == 6:
            stu.sort()
            break
        elif key == 7:
            print('退出成功!')
            return  None
        else:
            print('输入有误重新输入!')
            continue


if __name__ == '__main__':
    main()
