import scrapy


class IkeaSpider(scrapy.Spider):
    name = "ikea"
    allowed_domains = ["ikea.com"]

    def __init__(self, url, *args, **kwargs):
        super(IkeaSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        json_product = response.xpath('//div[contains(@class, "pip-product__subgrid")]')

        data_product_id = json_product.xpath('./@data-product-id').get()
        data_product_no = json_product.xpath('./@data-product-no').get()
        data_product_type = json_product.xpath('./@data-product-type').get()
        data_product_name = json_product.xpath('./@data-product-name').get()
        data_product_rating = json_product.xpath('./@data-product-rating').get()
        data_online_sellable = json_product.xpath('./@data-online-sellable').get()
        data_product_price = json_product.xpath('./@data-product-price').get()
        data_use_observe_product_details = json_product.xpath('./@data-use-observe-product-details').get()

        # data_hydration_props have all the product data (images, reviews, product details, etc.)
        data_hydration_props = json_product.xpath('./@data-hydration-props').get()

        yield {
            'data_product_id': data_product_id,
            'data_product_type': data_product_type,
            'data_product_rating': data_product_rating,
            'data_online_sellable': data_online_sellable,
            'data_product_price': data_product_price,
            'data_use_observe_product_details': data_use_observe_product_details,
            'data_product_name': data_product_name,
        }
