from models import Product
from cacheHandler.basecache import BaseCacheHandler
class ProductCache(BaseCacheHandler):

    BASE_KEY = "v1_product_{prodId}"
    TIMEOUT = 60 * 60 * 1   # 1 hour

    def __init__(self, prodId, cache):
        self.cache = cache
        self.prodId = prodId
        self.key = ProductCache.BASE_KEY.format(prodId=self.prodId)
        super().__init__(
            cache,
            self.key,
            ProductCache.TIMEOUT
        )

        self.name = None
        self.initial_price = None
        self.photo = None
        self.deadline_date = None
        self.increment = None
        self.description = None

    def get_configuration(self):
        _cached_content = self.cache.get(
            self.key
        )
        
        if _cached_content:
            print(f"Product_Cache: {self.key} From Cache")
            self.name = _cached_content["name"]
            self.initial_price = _cached_content["initial_price"]
            self.photo = _cached_content["photo"]
            self.deadline_date = _cached_content["deadline_date"]
            self.increment = _cached_content["increment"]
            self.description = _cached_content["description"]

        else:
            print(f"Product_Cache: {self.key} From DB")
            try:
                instance = Product.query.filter_by(prod_id=self.prodId).first()
                self.name = instance.name
                self.initial_price = instance.initial_price
                self.photo = instance.photo
                self.deadline_date = instance.deadline_date
                self.increment = instance.increment
                self.description = instance.description
                self._save_config_to_cache()
            except:
                print("Error in Create Bid") 
    
    def _save_config_to_cache(self):
        _cache_content = {
            "name":self.name,
            "initial_price":self.initial_price,
            "photo":self.photo,
            "deadline_date":self.deadline_date,
            "increment":self.increment,
            "description":self.description
        }
        self.set_configuration(_cache_content)
