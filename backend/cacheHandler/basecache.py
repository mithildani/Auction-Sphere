class BaseCacheHandler:
    BASE_KEY = None

    def __init__(self, key: str, timeout: int = 60, alias: str = "default", cache=cache):
        self.key = key
        self.timeout = timeout
        self.cache = cache

    def get_configuration(self):
        raise NotImplementedError('subclasses must provide this method')

    def set_configuration(self, content=None):
        if not content:
            raise Exception('no data while setting cache.')
        cache.set(
            self.key,
            content,
            timeout=self.timeout,
        )

    def invalidate_cache(self):
        cache.delete(
            self.key,
        )
