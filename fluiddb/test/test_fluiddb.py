import fluiddb
import unittest

class FluiddbTest(unittest.TestCase):
    def test_fluiddb_call(self):
        """this test will test fluiddb call"""
        status, result = fluiddb.call('GET', '/objects', query='fluiddb/users/username = "igorgue"')
        assert status == 200
        assert result == {u'ids': [u'71d5aa6f-d5fa-4578-9301-411fd92b1727']}

if __name__ == '__main__':
    unittest.main()
