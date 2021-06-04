# 基于 Django 的博客系统

### 安装

    pipenv install 

### 虚拟环境

查看：

    pipenv --venv
激活：

    pipenv shell
    
退出激活：

    exit
### 启动
    

    cd blogproject

    python3 manage.py runserver



### admin账户：

    admin
    123
    
### 找回用户名和密码：

    pipenv shell

    python manage.py shell 

    from django.contrib.auth.models import User        

    user =User.objects.get(username='admin')

    user.set_password('new_password')  

    user.save()

### 上线


