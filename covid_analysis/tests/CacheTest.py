import os
import unittest
from datetime import datetime, timedelta

from covid_analysis.utils import CacheObject


class CacheObjectTest(unittest.TestCase):
    def test_is_expired_after_expiration_date(self):
        a_value = 1
        object = CacheObject(a_value, expiration_date=datetime.now())
        self.assertEqual(True, object.has_expired)

    def test_is_not_expired_before_expiration_date(self):
        a_value = 1
        object = CacheObject(a_value, expiration_date=datetime.now() + timedelta(days=1))
        self.assertEqual(False, object.has_expired)



class CacheTest(unittest.TestCase):
    def test_it_can_be_saved_and_retrieved_with_a_key(self):
        a_value = 1
        CacheObject.save(a_value, key = '123', expiration_date=datetime.now() + timedelta(days=1))
        retrieved_object = CacheObject.retrieve(key = '123')
        self.assertEqual(a_value, retrieved_object)

        # 202cb962ac59075b964b07152d234b70 is hash of "123"
        os.remove("202cb962ac59075b964b07152d234b70.cache")

    def test_it_returns_none_if_cache_expired(self):
        a_value = 1
        CacheObject.save(a_value, key='123', expiration_date=datetime.now())
        retrieved_object = CacheObject.retrieve(key='123')
        self.assertIsNone(retrieved_object)

        # file has already been remove
        with self.assertRaises(FileNotFoundError):
            # 202cb962ac59075b964b07152d234b70 is hash of "123"
            os.remove("202cb962ac59075b964b07152d234b70.cache")

    def test_it_returns_none_if_cache_does_not_exist(self):
        retrieved_object = CacheObject.retrieve(key='123')
        self.assertIsNone(retrieved_object)

if __name__ == '__main__':
    unittest.main()
