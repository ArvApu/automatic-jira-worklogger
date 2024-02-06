# Automatic JIRA worklogger

This tool helps to automaticly push worklog to Jira's Tempo. All you need to do is to create predifend configuration for days in `.config.json` file (example provided in templates).

## Usage and setup

1. Add `.config.json`
2. Add `.env` and fill it with personal access token (or API Token) from JIRA and Base URL.
3. Install dependencies `/path/to/pip install -r requirements.txt`
4. Launch the script: `/path/to/python /path/to/main.py`

__Extra:__ You could add this as a cron job so that for example every friday at 11 o'clock the script would run and fill out your worklog:

1. Go to  crontab config page:
    ```
    crontab -e
    ```
2. Add this line
    ```
    0 11 * * 5 /path/to/python /path/to/main.py
    ```
Now every friday at 11 o'clock you will get filled worklog
