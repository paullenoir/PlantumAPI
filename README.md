# PlantumAPI
## Installation
pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy
pip install python-dotenv
pip install pydantic
sudo apt-get install libmysqlclient-dev
sudo apt-get install python3-dev
pip install mysqlclient

## Local run
uvicorn main:app --reload
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/sensors

## AWS EC2
sudo apt-get update
sudo apt-get upgrade

## AWS EC2 Nginx
sudo apt install -y python3-pip nginx
sudo nano /etc/nginx/sites-enabled/plantumFastapi_nginx
server{
    listen 80;
    server_name 18.191.167.216;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
sudo service nginx restart
sudo systemctl status nginx


## AWS EC2 FastAPI
cd /var/www/html
apt install python3-pip
pip install fastapi
pip install "uvicorn[standard]"
cd /var/www/html/Plantum/FastAPI

run local dans instance EC2
uvicorn main:app --reload

## Gunicorn
run prod fastAPI meme si le terminal est ferme
sudo apt install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

main:app fait référence au fichier principal (par exemple, main.py) et à l'instance de votre application FastAPI.
-w 4 spécifie le nombre de travailleurs (workers) Gunicorn à lancer. Vous pouvez ajuster ce nombre en fonction des besoins de votre application.
-k uvicorn.workers.UvicornWorker indique à Gunicorn d'utiliser le worker Uvicorn pour gérer les requêtes entrantes. Uvicorn est le serveur ASGI utilisé par FastAPI.

ps aux | grep gunicorn
kill <PID>

-------------
Requete POST SENSOR
{
    "time": "te",
    "sensor_name": "Capteur2",
    "sensor_value": "35",
    "created_at" : "t",
    "updated_at": "t"
}


--------------
sudo rm -r -f dossier
telnet database-1.cwwiilc5uwry.us-east-2.rds.amazonaws.com 3306
--------------
# GIT
generer un token dans github: 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
sudo git clone https://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:x-oauth-basic@github.com/paullenoir/Plantum.git
sudo php artisan serve --host=0.0.0.0 --port=8000
sudo apt-get install php-mysql

sudo rm -r -f dossier
http://3.129.60.30:80
cd /var/www/html/Plantum/API/api-plantum

sudo apt-get install git
sudo apt-get install zip unzip
---
ssh-keygen -t rsa -b 4096 -C "github"
cd .ssh
ll
cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOwSMXKm/aJ+hg46hc4dujB3xN/qzjxDirTiXIosRZscx66sSszhgkslbk2O3rs/A6WdrxhKqgKffewM9c1vkBMGhd+eY9SKcJxxniEHtOgT9wWrQDaV2Tpah/r92/Xl5S415PluiYZ1mBM9/i4GZdeJEj9Dh7vJ8tleuaHjhroHUJMNKi3OkGvwwEMBp7q2+gw7ed555U0z+RzvY6Pfi2n+0PfzQ0zJEn9R6H1zJi1rzXH7jBc0awHujaZuCJPpBxonTFaMa8HQ6hhn5hIS45zLpXgDiFAHjTxS8xxv+O75nv8LLkZq0ZfztEmrE/E5714CUHSs6vAnfuJLz0FJZodLjgD5mxVkE7yTuhA4Kfjis18PY1NeTTqaf1HNq23S51SJS+JZEkfIGXgN5ixeyXdnPQu3VAacmozVAUMyMzHtxtT5V5GcCv1cuiztsQXUojSBkw8/chh+Q7Sya7WVIETEjHCQvIDlA9TyGSdbQlAz1GB2P2IOXT5kxouztU6MgQIRLn7yPeE/kM0gg2CEd1pnQyunWY3nCgClPxjjreob3FndCExmsUjt+3yKZVp9ig7PAfrVpndpGV2dUkTx9+Gy9kLrvOChzewZoz5/k0L0w7eTNA0OrHCmGcBt4o45sKgpaTIThT/vNhsFHe3MagjAyrfNGZU93nbzDk2O5IUw== github

coller id_rsa.pub dans github/nomprojet/setting/deploy key/add deploy key/
---
sudo git clone https://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:x-oauth-basic@github.com/paullenoir/Plantum.git html
