## Домашняя работа к занятию "7.1. Инфраструктура как код"

#### Задача 1

1) Какой тип инфраструктуры будем использовать для этого проекта: изменяемый или не изменяемый?
- изменяемый
2) Будет ли центральный сервер для управления инфраструктурой?
- нет
3) Будут ли агенты на серверах?
- нет
4) Будут ли использованы средства для управления конфигурацией или инициализации ресурсов?
- Будут использованы средства для управления конфигурацией

Какие инструменты из уже используемых вы хотели бы использовать для нового проекта?
- Ansible
- TeamCity
- Kubernetes
- Docker
- Terraform
- Packer

Хотите ли рассмотреть возможность внедрения новых инструментов для этого проекта?
- нет

#### Задача 2

```
[ sander@imac-home ~ ]$ terraform --version
Terraform v0.14.0
```

#### Задача 3

```
[ sander@imac-home ~ ]$ /usr/local/Cellar/terraform/0.14.0/bin/terraform -v
Terraform v0.14.0

[ sander@imac-home ~ ]$ ~/Downloads/terraform -v
Terraform v0.12.0

Your version of Terraform is out of date! The latest version
is 0.14.0. You can update by downloading from www.terraform.io/downloads.html
[ sander@imac-home ~ ]$
```

