# my django alert system
# auth: pengzuhao
# date: 2018.3.20

# 一，项目环境
centos7.4
python2.7

# 二，所需安装模块
# 1.
yum -y install python-pip gcc gcc-c++ mysql-devel python-devel
# 2.
pip install --upgrade pip
# 3.
pip install django
# 4.
pip install bootstrap-admin
# 5.
pip install mysqlclient
# 6.
pip install django-crontab
# 7.
pip install apscheduler==2.1.2
# 8.
pip install pycrypto

# 三，所需系统环境变量
# 1.
export dbname=***
# 2.
export dbhost=***
# 3.
export dbport=***
# 4.
export dbuser=***
# 5.
export dbpwd=***
# 6.
export keyone=***
# 7.
export keytwo=***
# 8.
export mailfromuser=***
# 9.
export smtpserver=***
# 10.
export smtpport=***
# 11.
export smtppwd=***
# 12.
export smtpadmin=***

# 四，数据库初始化
# 1，
python manage.py makemigrations
是在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，
但是这个改动还没有作用到数据库文件，数据库没有增加新的表
# 2,
python manage.py migrate
执行migrate，这时候才真的把作用到数据库文件，产生对应的表
python manage.py migrate --database=sockas 指定对应的表
python manage.py migrate sockalert 指定对应项目
# 3，
python manage.py flush 清空默认表
python manage.py flush --database=sockas 清空指定表

# 五，日志切割
#
cat >> /etc/logrotate.d/sockalert<<EOF
$pjpath/projectone/logs/admin.log {
    compress
    delaycompress
    missingok
    notifempty
    daily
    rotate 5
    size 1k
    olddir $pjpath/projectone/logs/
    dateext
    create 0644 root root
    postrotate
 	    source /etc/profile &>/dev/null  && sh  $pjpath/restart.sh && cd /devops_1/projectone && nohup /usr/bin/python manage.py runserver 0.0.0.0:80 &
        endscript
}
#
service rsyslog restart

# 六，FAQ
# 1.
报错Database returned an invalid value in QuerySet.datetimes(). Are time zone definitions for your database and pytz installed?
解决：
在终端输入以下代码
mysql_tzinfo_to_sql?/usr/share/zoneinfo?|?mysql?-u root?-p mysql
输入mysql密码即可（注意上面语句中的mysql不是密码）
# 2.
需开启mysql严格模式
vim /etc/my.cnf #添加：
[mysqld]
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES

