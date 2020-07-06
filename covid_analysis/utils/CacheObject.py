import os
import pickle
from datetime import datetime
import hashlib

class CacheObject:
    """
    Cache object definition, it holds a value and an expiration_date
    """
    def __init__(self, value: object, *args, expiration_date = None):
        self.value = value
        self.expiration_date = expiration_date or datetime.now()

    @property
    def has_expired(self):
        """
        Check whether the cached value has expired or not

        Returns
        -------
        True if expired, False otherwise
        """
        return self.expiration_date < datetime.now()

    @classmethod
    def save(cls, object, key, expiration_date):
        """
        Static method to store an object into cache

        Parameters
        ----------
        object: the object to save
        key: the string key to associate to cache element
        expiration_date: the date within the cache is considered valid

        Returns
        -------
        None
        """
        instance = CacheObject(object, expiration_date=expiration_date)
        hash_object = hashlib.md5(key.encode())
        cached_filename = cls._cache_filename(hash_object)

        with open(cached_filename, "wb") as f:
            pickle.dump(instance, f)

    @classmethod
    def retrieve(cls, key):
        """
        Retrieve an object from the cache

        Parameters
        ----------
        key: the string key to look for

        Returns
        -------
        object stored in the cache, None if not found
        """
        hash_object = hashlib.md5(key.encode())
        cached_filename = cls._cache_filename(hash_object)

        if (not os.path.exists(cached_filename)):
            return None

        with open(cached_filename, "rb") as f:
            unserialized = pickle.load(f)

        if (unserialized.has_expired):
            os.remove(cached_filename)
            return None

        return unserialized.value

    @classmethod
    def _cache_filename(cls, hash_object):
        cached_filename = hash_object.hexdigest() + ".cache"
        return cached_filename




def cache(*args, **kwargs):
    """
    cache decorator, it can store function results into file-based cache for a configurable amount of time

    Parameters
    ----------
    key: the key where to store the value
    expires_after: timedelta which stores cache validity period

    Returns
    -------
    object with the cached value, None if cache is expired or does not exist
    """
    def inner(func):
        key = kwargs["key"]
        expires_after = kwargs["expires_after"]

        def wrapper_func(*args, **kwargs):
            cached_data = CacheObject.retrieve(key=key)

            if (cached_data is not None):
                return cached_data

            fresh_data = func(*args, **kwargs)

            CacheObject.save(fresh_data, key=key, expiration_date=(datetime.now() + expires_after))

            return fresh_data

        return wrapper_func
    return inner