# python-mysql-
python成绩管理系统，使用mysql数据库,涉及数据库增删改查排序

workbench6.3.9
创建表
"""CREATE TABLE 'users' ('id' INT(11) NOT NULL AUTO_INCREMENT,    
'StuNo' INT(11) NOT NULL,    
'Age' INT(11) NOT NULL,    
'Sex' VARCHAR(255) COLLATE utf8_bin NOT NULL,  
'Name' VARCHAR(255) COLLATE utf8_bin NOT NULL,  
'Score' INT(11) NOT NULL,   
PRIMARY KEY ('id') ) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1
"""
