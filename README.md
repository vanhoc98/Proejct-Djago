# ĐỒ ÁN 1 - 2020.2 - HUST
##### Sinh viên thực hiện: Nguyễn Trần Thức
##### Giảng viên hướng dẫn: TS. Nguyễn Huy Trường

### Công nghệ sử dụng
Django, Heroku, Freenom

### Cài đặt trên local Window OS

Tạo thư mục dự án

```sh
mkdir my_project && cd my_project
```

Cài và setup môi trường ảo

```sh
pip install virtualenv
py -m venv env
cd env/Scripts
activate
cd..
cd..
```

Clone code và chạy trên local

```sh
git clone https://github.com/tranthuc99/project1-django.git
cd project1-django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Nhập url: http://127.0.0.1:8000/ trên trình duyệt web!

### Creating an admin user
First we’ll need to create a user who can login to the admin site. Run the following command:
```sh
python manage.py createsuperuser
```

Enter your desired username and press enter.
```
Username: admin
```

You will then be prompted for your desired email address:
```
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```

Now, open a web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/.


### Báo cáo LaTeX
https://www.overleaf.com/read/hhzhfvjhppys

### Demo 

http://project1.thucnguyen.tk/

(hoặc: http://2but1.ml/)

(hoặc: https://doan1-2but1store.herokuapp.com/)
