## Machine_learning_project_1
### Software and account requirenments.

 1. [Github](https://github.com/)
 2. [heroku account](https://www.heroku.com/)
 3. [VS code](https://code.visualstudio.com/)
 4. [Git Cli](https://git-scm.com/downloads)
 5. [Git Documentation](https://git-scm.com/doc)


 creating conda environment
 ```
 conda create -p venv python==3.7 -y
 ```
 activate conda virtual environment
 ```
 conda activate venv OR conda activate venv/
 ```
 create requirement.txt file and install reuirements in it
 ```
 pip install -r Requirement.txt
 ```
 create python app and run the flask code in it
 ```
 app.py
```
To add file to git
```
git add <filename>
```
To add all files to git
```
git add .
```
To check git status
```
git status
```
To check all versions
```
git log
```
To create version/commit all achanges by git
```
git commit -m "msg"
```
To send changes
```
git push origin main
```
To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = sricharan.karingula@gmail.com
2. HEROKU_API_KEY = d94c80ff-8a6a-4bc0-b47f-3dd4fb9678a7
3. HEROKU_APP_NAME = 

```
BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname>
```

```
python setup.py install
```
