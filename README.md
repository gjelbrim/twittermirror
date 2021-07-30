![GitHub last commit](https://img.shields.io/github/last-commit/gjelbrim/twittermirror?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/gjelbrim/twittermirror?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/gjelbrim/twittermirror?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/gjelbrim/twittermirror?style=for-the-badge)
# twittermirror

A python script that allows you to mirror a specific Twitter user's (i.e. a user who bulk blocks) tweets.

## Installation

run:

```bash
python3 install.py
```

to start the installation process. This will also install the required pip packages. If this fails run:

```bash
pip3 install -r requirements.txt
```

During the installation process you will be asked to enter the API Keys and Tokens of two accounts. The first one will read the Tweets the second one will tweet them. Both accounts can be the same. In the last step you will be asked to enter the twitter handle of the user you want to mirror.

## Start the programm

run:

```bash
python3 twittermirror.py
```

## Configuration

The Configuration is stored in `config.ini`:

```ini
[sender] #this account will send the tweet it reads to the reciver
apikey = 
apisecretkey = 
accesstoken = 
accesstokensecret = 

[receiver] #this account will receive the tweets from the sender at tweet them
apikey = 
apisecretkey = 
accesstoken = 
accesstokensecret = 

[user]
twitterhandle = #it must start with '@'
```