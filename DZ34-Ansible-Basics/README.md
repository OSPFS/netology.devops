## Доработка домашней работы по занятию "08.01 Введение в Ansible"

Алексей, добрый день! 

Во первых, не привет, а здравствуйте. На "ты" мы с Вами не переходили и нужно учитывать, что некоторым людям на курсе может идти 5й десяток лет. Ну да ладно, я не гордый и раз Вам так удобно давайте на ты.

Во вторых, у некоторых студентов, в жизни кроме учебы ещё есть работа, семья и дети. Поэтому я не стал расписывать каждый пункт (тем более не совсем ясно, что там писать), выполнил задание полностью, результаты выполнения привел в ответе, думаю из них видно, что тему я усвоил.

В третьих, о каком самоконтроле идет речь? Ни в одном из пунктов задания ничего подобного не упоминается.

1) 12
2) Что Вы тут от меня ждёте увидеть?
3) см. п2
4) 
```
TASK [Print fact] ************************************************************************************************************************************
ok: [centos] => {
    "msg": "el"
}
ok: [ubuntu] => {
    "msg": "deb"
}
```
5-8)
```
$ ansible-playbook site.yml -i inventory/prod.yml --ask-vault-pass
Vault password:

PLAY [Print os facts] ********************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
ok: [ubuntu]
ok: [centos]

TASK [Print OS] **************************************************************************************************************************************
ok: [centos] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ************************************************************************************************************************************
ok: [centos] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}

PLAY RECAP *******************************************************************************************************************************************
centos                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
9) local                          execute on controller
10-11)

```
ansible-playbook ../site.yml -i ../inventory/prod.yml --vault-password-file ~/npass

PLAY [Print os facts] ********************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
[WARNING]: Platform darwin on host ::1 is using the discovered Python interpreter at /usr/bin/python, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible/2.10/reference_appendices/interpreter_discovery.html for more
information.
ok: [::1]
ok: [ubuntu]
ok: [centos]

TASK [Print OS] **************************************************************************************************************************************
ok: [::1] => {
    "msg": "MacOSX"
}
ok: [centos] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] ************************************************************************************************************************************
ok: [::1] => {
    "msg": "all default fact"
}
ok: [centos] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}

PLAY RECAP *******************************************************************************************************************************************
::1                        : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
centos                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
