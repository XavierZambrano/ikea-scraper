# Ikea Scraper

## Usage

### CLI

You can execute:
```
scrapy crawl ikea -a url=https://www.ikea.com/us/en/p/your-product/ -O result.csv
```

- `url`: Ikea Product Url

## Example

This command will scrape https://www.ikea.com/us/en/p/malm-6-drawer-dresser-white-30360468/ and save the result in result.csv

```
scrapy crawl ikea -a url=https://www.ikea.com/us/en/p/malm-6-drawer-dresser-white-30360468/ -O result.csv
```

[result example](assets/result_30360468.csv)

## Notes

- Actually only scrape basic data like name and price, but all the data (images, reviews, product details, etc.) is in [ikea.py](ikea_scraper/spiders/ikea.py) > `data_hydration_props` 
