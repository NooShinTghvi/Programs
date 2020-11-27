# Telegram Channel

This is python code to get data from Telegram channels. This saves this data into JSON files.

## Requirements

I used `telethon`, a Python package to work with Telegram!

    pip3 install telethon

To connect to Telegram, we need an `api_id` and an `api_hash`. To get these parameters, you need to login to your [Telegram core](https://my.telegram.org/) and go to the [API development tools](https://my.telegram.org/apps) area. There is a form that you need to fill out, and after that, you can receive your `api_id` and `api_hash`.

 To avoid security issues, we put our API credentials in another file called **config.ini** .   just change *config.ini.example* file to *config.ini* .
 

### Session File
After run, program create a *.session [file](https://docs.telethon.dev/en/latest/concepts/sessions.html) for caching and handling your authorization key. 

