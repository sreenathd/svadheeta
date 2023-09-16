sudo docker stop svadheeta
sudo docker rm svadheeta
sudo docker build -t svadheeta .
sudo docker run -itd -p 80:5000 --name svadheeta  svadheeta
sudo docker image prune -a
