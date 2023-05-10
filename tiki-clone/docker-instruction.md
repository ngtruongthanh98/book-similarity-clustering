cd tiki-clone

docker build -t tiki-clone:latest .

docker run -p 5173:5173 tiki-clone

( docker run -tid -p 5173:5173 --name tiki-clone-app --network host tiki-clone-app )

open browser, access http://localhost:5173

on the other hand, we can open the url expose from container: http://172.17.0.2:5173/

### RUN

docker run -tid -p 5173:5173 --name tiki-clone-app --network host tiki-clone-app

###### Docker list container

docker ps

###### docker remove container

docker rm -f container_name

####### TEST ######
docker build -t tiki-clone:test .

docker run -dit tiki-clone:test bash

docker ps

docker exec -it container_name bash

##########
