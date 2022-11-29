class Create_Bid(BaseCacheHandler):

    BASE_KEY = "v1_bid_{prodId}"
    TIMEOUT = 60 * 60 * 1   # 1 hour

    def __init__(self, prodId):
        self.prodId = prodId
        self.key = Create_Bid.BASE_KEY.format(prodId=self.prodId)
        super().__init__(
            self.key,
            Create_Bid.TIMEOUT
        )

        self.bid = bid
    def get_configuration(self):
        _cached_content = cache.get(
            self.key
        )
        
        if _cached_content:
            print(f"Create_Bid: {self.key} From Cache")
            self.bid = _cached_content["bid"]

        else:
            print(f"Create_Bid: {self.key} From DB")
            try:
                # outgoing = Movement.objects.filter(origin_premise_id=self.premise_id).aggregate(Sum('items_moved'))[
                #                "items_moved__sum"] or 0
                # incoming = Movement.objects.filter(destination_premise_id=self.premise_id).aggregate(Sum('items_moved'))[
                #                "items_moved__sum"] or 0
                # self.population_count = int(incoming - outgoing)


                # print(f"{self.premise_id} total animal: {self.population_count}")
                self._save_config_to_cache()
            except:
                print("Error in Create Bid") 
    
    def _save_config_to_cache(self):
        _cache_content = {
            "bid": self.bid,
        }
        self.set_configuration(_cache_content)
