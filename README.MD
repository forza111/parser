# Scraper

Scraper for the famous store https://www.timberland.com/sale.html   
Allows you to parse the site (only the products section) in two modes - web service mode and script mode.

## How to use

```docker-compose up --build```

### Web service mode

Visit page http://localhost:8000/docs in a browser for help.

### Script mode

1. Start an interactive shell in a container
2. Get more information on a command 

```  
1. docker-compose exec web bash
2. python console_scraper.py --h
```  

#### Example use
```python console_scraper.py https://www.timberland.com/shop/mens-boots --width 30 --save```  
Displays information from the specified URL to the console, line width 30, 
also saves the result to content/mens-boots-2022-01-14.txt (Request made on 2022/01/14, so this date appears in the file name)

