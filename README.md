#### for django learning

#### write a blog web for python django web frame learning
> Note: These blog code not my own code, I just write for  learning. All copyrights are owned by the original author

> code from [github link](https://github.com/HaddyYang/django2.0-course)

> auth video [bilibili link](https://space.bilibili.com/252028233)

#### learn django authentication and session



#### how to initiate development environment.
#### start dependent services.
```
cd scripts/deploy
docker-compose up -d
```
#### initiate database data.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

#### create super user.
```
python3 manage.py createsuperuser
```