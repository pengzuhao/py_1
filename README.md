# my django alert system
# auth: pengzuhao
# date: 2018.3.20

һ����Ŀ����
centos7.4
python2.7

�������谲װģ��
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
pip?install?apscheduler==2.1.2
# 8.
pip install pycrypto

��������ϵͳ��������
export dbname=***
export dbhost=***
export dbport=***
export dbuser=***
export dbpwd=***
export keyone=***
export keytwo=***
export mailfromuser=***
export smtpserver=***
export smtpport=***
export smtppwd=***
export smtpadmin=***

�ģ����ݿ��ʼ��
1��
python manage.py makemigrations
���ڸ�app�½��� migrationsĿ¼������¼�������еĹ���modes.py�ĸĶ���
��������Ķ���û�����õ����ݿ��ļ������ݿ�û�������µı�
2,
python manage.py migrate
ִ��migrate����ʱ�����İ����õ����ݿ��ļ���������Ӧ�ı�
python manage.py migrate --database=sockas ָ����Ӧ�ı�
python manage.py migrate sockalert ָ����Ӧ��Ŀ
3��
python manage.py flush ���Ĭ�ϱ�
python manage.py flush --database=sockas ���ָ����

�壬FAQ
1.
����Database returned an invalid value in QuerySet.datetimes(). Are time zone definitions for your database and pytz installed?
�����
���ն��������´���
mysql_tzinfo_to_sql?/usr/share/zoneinfo?|?mysql?-u root?-p mysql
����mysql���뼴�ɣ�ע����������е�mysql�������룩
2.
�迪��mysql�ϸ�ģʽ
vim /etc/my.cnf #��ӣ�
[mysqld]
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES