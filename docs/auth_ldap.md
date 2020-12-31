#### django auth ldap
- https://github.com/django-auth-ldap/django-auth-ldap

#### about open-ldap service
[home page]
- https://www.openldap.org/doc/admin24/quickstart.html
- https://www.openldap.org/doc/admin24/

[docker]
- https://github.com/osixia/docker-openldap

[ldapsearch ldapmodify cmdline]
- https://www.cnblogs.com/adam1991/p/7656108.html
- php ldap admin
```
docker run -p 6443:443 \
                --env PHPLDAPADMIN_LDAP_HOSTS=192.168.9.4 \
                                --detach --name my-phpldapadmin osixia/phpldapadmin:0.9.0
```