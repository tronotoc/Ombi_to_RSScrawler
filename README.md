# Ombi_to_RSScrawler
Ombi_to_RSScrawler sendet die genehmigten Filmrequests eures Ombiservers an euer RSScrawler. Hierdurch wird es möglich Ombi direkt mit OCH und JDownloader zu verknüpfen.

## Vorraussetzungen
* [Python](https://www.python.org/downloads/)
* [Ombi](https://ombi.io/)
* [RSScrawler](https://github.com/rix1337/RSScrawler)
* [Zusatzpakete]

## Nutzung
Folgende Daten müssen in die secrets.py eingetragen werden:  
  ```OmbiUrl='<URL des OmbiServer>'```  
  ```OmbiApi='<ApiKey des OmbiServer>'```  
  ```tMDbApiKey='<tMDbApiKey>'```Muss unter (https://www.themoviedb.org/settings/api) angefordert werden
  ```RSScrawlerURL='<RSScrawlerURL>'``` z.B. '192.168.178.2:9000'

## Ombi_to_RSScrawler starten
```python ombi_to_rsscrawler.py```führt das Skript aus
