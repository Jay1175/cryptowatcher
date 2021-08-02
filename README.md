# CryptoWatcher

Cryptowatcher is a discord.py script you must run with your own bot account. It tracks ethereum prices and will send them to a user defined channel on a user defined loop (default every 6 hours). It also lets you get ethereum, btc, and dogecoin prices on demand with !eth, !btc, and !doge respectively. Prices are in USD.

## Installation

Use the package manager to install required packages.

```bash
pip install -r requirements.txt
```

**Need help installing and using python?** Follow these steps below.

If you're on windows, I recommend using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) to create a python environment specific to this bot instead of a direct install of python.

After installing conda open it and create an environment

```cmd
conda create --name cryptowatcher python=3.8
```
Activate your new environment
```cmd
conda activate cryptowatcher
```
You should see your environment name at the far left of your command line, now verify your python installation and making sure you have pip:
```cmd
python --version
Python 3.8.10

pip --version
pip 21.1.3 from C:\Users\YourName\Anaconda3\envs\cryptowatcher\lib\site-packages\pip (python 3.8)
```
Finish up by installing the packages with pip at the beginning of this section.

## Usage

Make a copy config.json.example and rename it to config.json. Open it up with notepad or whatever you use and fill out each line with the appropriate data. It should look similar to the example below.

Autoscrape can be set to "eth", "btc", or "doge". If it isn't set to one of these values, it will default to ethereum.

autoscrape_time_minutes should be set to a reasonable number of minutes. It defaults to 360, or every 6 hours.

*Note - this is an example file, your token and channel ID will be different. See below if you need help finding them.*

```bash
{
    "token":"aBcdEfGhijKlMnoPQRstuVwXYZ0123456789",
    "autoscrape":"eth"
    "autoscrape_time_minutes":360,
    "autoscrape_channel_ID":1234567890987654321
}
```

Need help creating a bot and getting your token? Follow [this guide](https://www.writebots.com/discord-bot-token/).

Need help finding your channel ID? Follow [this guide](https://www.remote.tools/remote-work/how-to-find-discord-id).

Once your config.json file has been filled in and your pip packages are downloaded, run the bot. If you have the config file set up correctly, it will show you what currency is being autoscraped and how often as well as what bot your token is tied to.

```python
python main.py
Autoscraping ethereum every 360 minutes
YourDiscordBotsName#0000 ready
```
Now your bot should have automatically grabbed and reported a crypto price automatically to your desired discord channel.

If you want an immediate update, you can get one.

!eth, !btc, !doge will get an immediate update of their respective coin.