* SockAlert
* auth: `pyt`
* date: 2018.3.20

# һ����Ŀ����
centos7.4
python2.7

# �������谲װģ��
        yum -y install python-pip gcc gcc-c++ mysql-devel python-devel
        pip install --upgrade pip
        pip install django
        pip install bootstrap-admin
        pip install mysqlclient
        pip install django-crontab
        pip install apscheduler==2.1.2
        pip install pycrypto

# ��������ϵͳ��������
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

# �ģ����ݿ��ʼ��
# 1��
        python manage.py makemigrations
        ���ڸ�app�½��� migrationsĿ¼������¼�������еĹ���modes.py�ĸĶ���
        ��������Ķ���û�����õ����ݿ��ļ������ݿ�û�������µı�
# 2,
        python manage.py migrate
        ִ��migrate����ʱ�����İ����õ����ݿ��ļ���������Ӧ�ı�
        python manage.py migrate --database=sockas ָ����Ӧ�ı�
        python manage.py migrate sockalert ָ����Ӧ��Ŀ
# 3��
        python manage.py flush ���Ĭ�ϱ�
        python manage.py flush --database=sockas ���ָ����

# �壬��־�и�
        cat >> /etc/logrotate.d/sockalert<<EOF
        $pjpath/projectone/logs/admin.log {
            compress
            delaycompress
            missingok
            notifempty
            daily
            rotate 30
            size 10M
            olddir $pjpath/projectone/logs/
            dateext
            create 0644 root root
            postrotate
                source /etc/profile &>/dev/null  && sh  $pjpath/restart.sh && cd /devops_1/projectone && nohup /usr/bin/python manage.py runserver 0.0.0.0:80 &
                endscript
        }
        service rsyslog restart

# ����FAQ
# 1.
        ����Database returned an invalid value in QuerySet.datetimes(). Are time zone definitions for your database and pytz installed?
        �����
        ���ն��������´���
        mysql_tzinfo_to_sql?/usr/share/zoneinfo?|?mysql?-u root?-p mysql
        ����mysql���뼴�ɣ�ע����������е�mysql�������룩

# 2.
        �迪��mysql�ϸ�ģʽ
        vim /etc/my.cnf #��ӣ�
        [mysqld]
        sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES