import unittest
import GGlib

class function_test_4_GGlib(unittest.TestCase):
	def test_deg_to_sud(self):
		x,y = GGlib.deg2sud(51.47795, -0.00168)
		self.assertEqual(x,'51°28’40’’N')
		self.assertEqual(y, '0°0’6’’W')

	def test_sud_to_deg(self):
		lat,lon = GGlib.sud2deg('51°28’40’’N','0°0’6’’W')
		self.assertAlmostEqual(lat, 51.478,delta=0.001 )
		self.assertAlmostEqual(lon, 0.0017, delta=0.001)

	def test_is_it_in_poly(self):
		polygon = [[-65.3, 47.937], [-65.3, 47.907], [-64.6, 48.105], [-64.6, 48.201], [-65.3, 47.937]]
		p1 = [-64.6161111111111, 48.14]
		p2 = (-64.6161111111111, 48.14)
		p3 = (0,0)
		self.assertTrue(GGlib.is_it_in_poly(p1, polygon))
		self.assertTrue(GGlib.is_it_in_poly(p2, polygon))
		self.assertFalse(GGlib.is_it_in_poly(p3, polygon))


if __name__ == '__main__':
	unittest.main()