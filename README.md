![GitHub Workflow Status](https://github.com/gjelbrim/twittermirror/actions/workflows/pylint.yml)
![GitHub](https://github.com/gjelbrim/twittermirror/blob/main/LICENSE)
![GitHub last commit](https://github.com/gjelbrim/twittermirror/commits/main)
![GitHub repo size](https://github.com/gjelbrim/twittermirror)
![Lines of code](https://github.com/gjelbrim/twittermirror)
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
