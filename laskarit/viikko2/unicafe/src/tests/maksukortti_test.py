import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_oikein(self):
        syote = str(self.maksukortti)
        self.assertEqual(syote, "saldo: 10.0")
        
    def test_rahanlisays_toimii(self):
        self.maksukortti.lataa_rahaa(1000)
        syote = str(self.maksukortti)
        self.assertEqual(syote, "saldo: 20.0")
        
    def test_rahanotto_toimii(self):
        self.maksukortti.ota_rahaa(500)
        syote = str(self.maksukortti)
        self.assertEqual(syote, "saldo: 5.0")
        
    def test_rahanotto_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000)
        syote = str(self.maksukortti)
        self.assertEqual(syote, "saldo: 10.0")
        
    def test_rahanotto_vie_saldon_nollaan(self):
        self.maksukortti.ota_rahaa(1000)
        syote = str(self.maksukortti)
        self.assertEqual(syote, "saldo: 0.0")