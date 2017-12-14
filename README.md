# cryptoz

dockerized python crypto app

# build

```
docker build --tag erangaeb/cryptoz:0.1 .  
docker build --tag erangaeb/cryptoz:0.1 . --no-cache  
```

# run

```
# without env variable 
docker run -it -a stdin -a stdout erangaeb/cryptoz:0.1  

# with env variable
docker run -it -a stdin -a stdout -e DB_HOST=10.2.2.1 erangaeb/cryptoz:0.1  
```
