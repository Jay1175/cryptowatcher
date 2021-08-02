# CryptoWatcher

Cryptowatcher is a discord.py script you must run with your own bot account. It tracks ethereum prices and will send them to a user defined channel on a user defined loop (default every 6 hours). It also lets you get ethereum, btc, and dogecoin prices on demand with !eth, !btc, and !doge respectively. Prices are in USD.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirements.txt
```

**Need help installing and using python? I recommend using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) if on windows to create a virtual environment specifically for this bot.**

After installing conda, create an environment

```cmd
C:\discordbots\CryptoWatcher>conda create --name cryptowatcher python=3.8
```
Activate your new environment
```cmd
C:\discordbots\CryptoWatcher>activate cryptowatcher
```
You should see your environment name at the far left of your command line, now verify your python installation and making sure you have pip:
```cmd
(cryptowatcher) C:\discordbots\Cryptowatcher>python --version
Python 3.8.10

(cryptowatcher) C:\discordbots\Cryptowatcher>pip --version
pip 21.1.3 from C:\Users\YourName\Anaconda3\envs\cryptowatcher\lib\site-packages\pip (python 3.8)
```
Finish up by installing the packages with pip.

## Usage

Copy config.json.example to config.json. In config.json, fill out each line with the appropriate data. It should look similar to the example below:

```json
{
    "token":"aBcdEfGhijKlMnoPQRstuVwXYZ0123456789",
    "autoscrape":"eth"
    "autoscrape_time_minutes":360,
    "autoscrape_channel_ID":1234567890987654321
}
```

Autoscrape can be set to "eth", "btc", or "doge". If it isn't set to one of these values, it will default to ethereum.

Need help creating a bot and getting your token? Follow [this guide](https://www.writebots.com/discord-bot-token/).

Need help finding your channel ID? Follow [this guide](https://www.remote.tools/remote-work/how-to-find-discord-id).

Once your config.json file has been filled in and your pip packages are downloaded, run the bot.

```python
C:\discordbots\CryptoWatcher>python main.py
Autoscraping ethereum every 360 minutes
YourDiscordBotsName#0000 ready
```
Now your bot should have automatically grabbed and reported a crypto price automatically.

If you want an immediate update, you can get one.

!eth, !btc, !doge will get an immediate update of their respective coin.