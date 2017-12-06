# cryptoz

dockerized python crypto app

# build

docker build --tag erangaeb/cryptoz:0.1 .
docker build --tag erangaeb/cryptoz:0.1 . --no-cache

# run

docker run erangaeb
docker run -a stdin -a stdout -i -t erangaeb/cryptoz:0.1
