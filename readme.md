# Template for ec2 ssh
```
Host my-ec2-instance
    HostName ec2-XX-XXX-XX-XXX.compute-1.amazonaws.com
    User ec2-user
    IdentityFile /path/to/your/key.pem
```

# Instructions for plain ec2 instance
1. Python
```
sudo yum update
sudo yum install python
sudo yum install python-pip

pip install Flask
pip install flask-cors
pip install joblib
pip install sklearn
pip install pandas

<!-- build the model using "modelbuilding.py" script-->

```

1.1 Running application in background (python)
```
nohup python app.py &
kill [PID]
<!-- to kill -->
ps ax | grep app.py

```

2. Express js
```
sudo yum update
sudo yum install nodejs
sudo yum install npm
npm i python-shell
npm i cors
npm i express
```

2.2 Running application in background (node)
```
nohup node app.js &
ps ax | grep app.js
```