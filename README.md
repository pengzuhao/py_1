# my django alert system
# auth: pengzuhao
# date: 2018.3.20

# 一，项目环境
centos7.4 ＜/br＞
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
export dbname=***＜/br＞
export dbhost=***＜/br＞
export dbport=***＜/br＞
export dbuser=***＜/br＞
export dbpwd=***＜/br＞
export keyone=***＜/br＞
export keytwo=***＜/br＞
export mailfromuser=***＜/br＞
export smtpserver=***＜/br＞
export smtpport=***＜/br＞
export smtppwd=***＜/br＞
export smtpadmin=***＜/br＞

# 四，数据库初始化
# 1，
python manage.py makemigrations＜/br＞
是在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，＜/br＞
但是这个改动还没有作用到数据库文件，数据库没有增加新的表
# 2,
python manage.py migrate＜/br＞
执行migrate，这时候才真的把作用到数据库文件，产生对应的表＜/br＞
python manage.py migrate --database=sockas 指定对应的表＜/br＞
python manage.py migrate sockalert 指定对应项目
# 3，
python manage.py flush 清空默认表＜/br＞
python manage.py flush --database=sockas 清空指定表

# 五，日志切割
cat >> /etc/logrotate.d/sockalert<<EOF＜/br＞
$pjpath/projectone/logs/admin.log {＜/br＞
    compress＜/br＞
    delaycompress＜/br＞
    missingok＜/br＞
    notifempty＜/br＞
    daily＜/br＞
    rotate 5＜/br＞
    size 1k＜/br＞
    olddir $pjpath/projectone/logs/＜/br＞
    dateext＜/br＞
    create 0644 root root＜/br＞
    postrotate＜/br＞
 	    source /etc/profile &>/dev/null  && sh  $pjpath/restart.sh && cd /devops_1/projectone && nohup /usr/bin/python manage.py runserver 0.0.0.0:80 &＜/br＞
        endscript＜/br＞
}＜/br＞
service rsyslog restart

# 六，FAQ
# 1.
报错Database returned an invalid value in QuerySet.datetimes(). Are time zone definitions for your database and pytz installed?＜/br＞
解决：＜/br＞
在终端输入以下代码＜/br＞
mysql_tzinfo_to_sql?/usr/share/zoneinfo?|?mysql?-u root?-p mysql＜/br＞
输入mysql密码即可（注意上面语句中的mysql不是密码）＜/br＞
# 2.
需开启mysql严格模式＜/br＞
vim /etc/my.cnf #添加：＜/br＞
[mysqld]＜/br＞
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES

