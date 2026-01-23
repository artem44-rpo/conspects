### Просмотр списка пользователей

```cmd
net users
```

### Изменение пароля пользователя

```cmd
net user UserName New-Password
```

### Просмотр данных пользователей

```cmd
net user <UserName>
```

### Просмотр локальных групп

```cmd
net local group
```

### Назначения пользователя в локальную группу

```cmd
whoami и whoami /user
```

### Запрет на изменение пароля/его бесконечность

```cmd
net accounts /maxpwage:unlimited
```

### Удаление пользователя

```cmd
net user /delete
```
