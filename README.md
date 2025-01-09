# mlops-from-zero

Live training with AWS pipeline

[![Python application test with Github Actions](https://github.com/speedwagon1299/mlops-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/speedwagon1299/mlops-from-zero/actions/workflows/main.yml)

### To call Microservice

something like this

```bash
curl -X 'POST' \
  'https://noahgift-functions-from-zero-r7g59wcxx6x-8080.githubpreview.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`

### Run container

something like this

`docker run -p 127.0.0.1:8080:8080 a81ce4f35866`

### Invoke POST request

run `invoke.sh`



# MAJOR LEARNINGS


1. Start AWS EC2 instance with KP-1.pem

2. ssh -i <path-to>.pem ec2-user@<public-ip>

3. Ensure IAM user has AmazonEC2ContainerRegistryFullAccess

4. Create repo in AWS ECR and use the given push commands

5. Open AWS App Runner

First time => Run the following commands (For Amazon Linux)

sudo yum update -y   
sudo yum install git -y   
sudo yum install python3 -y   
sudo yum install make
sudo yum install docker -y   
sudo service docker start
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
python3 -m venv .venv
source ~/.venv/bin/activate		# Add to ~/.bashrc file end
aws configure		# Give info available in aws' config and credentials




We just started with a function. 
We built up a tool, we built up a micro service, we containerized it. 
We pushed the containerized micro service into a docker container registry. 
And now we can link to it using this app runner service. 