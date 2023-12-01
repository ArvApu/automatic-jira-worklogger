# Automatic JIRA worklogger

This tool helps to automaticly push worklog to Jira's Tempo. All you need to do is to create predifend configuration for days in `.config.json` file (example provided in templates).

## Usage and setup

1. Add `.config.json`
2. Add `.env` and fill it with personal access token from JIRA and Base URL.
3. Launch the script: /usr/local/bin/python3.9 main.py

Extra: You could add this as a cron job so that for example every friday the script would run and fill your worklog

1. Go to  crontab config page:
```
crontab -e
```
2. Add this line
```
0 11 * * 5 /path/to/python /path/to/main.py
```

Now every friday on 11 oclock you will get filled worklog
