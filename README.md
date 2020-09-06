# altpapierBot
Telegram Bot um sich zu Karton- sowie Papierabfuhr erinnern zu lassen
[https://telegram.me/altpapierbot](https://telegram.me/altpapierbot)

## Funktionsweise
Detailiertere Informationen zur Nutzung und Funktionsweise sind unter [https://dgnaegi.ch/2020/09/06/altpapierbot/](https://dgnaegi.ch/2020/09/06/altpapierbot/)

## Datengrundlage
Die Abfuhrdaten werden von der [Open Erz Api](https://www.stadt-zuerich.ch/portal/de/index/ogd/anwendungen/2019/open_erz_api.html) respektive der [API der Stadt St.Gallen](https://daten.stadt.sg.ch/api/v1/console/datasets/1.0/search/)
 bezogen 

## Requirements
python-telegram-bot mit [pip](https://pip.pypa.io/en/stable/) installieren

```bash
pip3 install python-telegram-bot
pip3 install request
mysql-connector-python
```
[Telegram Bot erstellen und Token erhalten](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)

## Setup
1. Datenbank anhand createDatabase.sql Script erstellen
2. config.json anpassen
3. altpapierNotifier.py als Task in gewünschten Intervallen einrichten (aktuell bspw. 5 Uhr morgens sowie 20:30 Uhr Abends)
4. main.py in der Bash laufen lassen