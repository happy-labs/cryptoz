# cryptoz

dockerized python crypto app

# run mysql

```
# without volume mapping
docker run -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8.0.0

# with volume mapping
docker run -e MYSQL_ROOT_PASSWORD=root -v /private/var/services/mysql:/var/lib/mysql -p 3306:3306 -d mysql:8.0.0
```


# build cryptoz

```
docker build --tag erangaeb/cryptoz:0.1 .
docker build --tag erangaeb/cryptoz:0.1 . --no-cache
```

# run cryptoz

```
# without env variable
docker run -it -a stdin -a stdout erangaeb/cryptoz:0.1

# with env variable
docker run -it -a stdin -a stdout -e DB_HOST=10.2.2.1 erangaeb/cryptoz:0.1  
```

# instruction
```
1. docker inspect 
2. env variables  
3. remove database container  
4. volume mapping mysql data  
5. multi container links   
6. docker compose  
```
