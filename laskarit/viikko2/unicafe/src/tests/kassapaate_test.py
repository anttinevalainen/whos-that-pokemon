import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    #Testien alustus ja kassapäätteen alkutilanne
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.rahaaOn = Maksukortti(10000)
        self.rahaaEiOle = Maksukortti(33)

    def test_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_maara_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_maara_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Käteismaksujen toimivuus
        #Onnistunut maksu
    def test_edullinen_kateinen_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukas_kateinen_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_kateinen_palauttaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_maukas_kateinen_palauttaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_edullinen_kateinen_nostaa_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 3)

    def test_maukas_kateinen_nostaa_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 3)

        #Epäonnistunut maksu
    def test_edullinen_epaonnistunut_kateinen_ei_nosta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_epaonnistunut_kateinen_ei_nosta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_epaonnistunu_kateinen_palauttaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_maukas_epaonnistunu_kateinen_palauttaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_edullinen_epaonnistunut_kateinen_ei_nosta_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_epaonnistunut_kateinen_ei_nosta_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Korttimaksujen toimivuus
        #Onnistunut maksu
    def test_edullinen_korttimaksu_veloitetaan_kortilta(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.rahaaOn))

    def test_maukas_korttimaksu_veloitetaan_kortilta(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.rahaaOn))

    def test_edullinen_korttimaksu_nostaa_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rahaaOn)
        self.kassapaate.syo_edullisesti_kortilla(self.rahaaOn)
        self.kassapaate.syo_edullisesti_kortilla(self.rahaaOn)
        self.assertEqual(self.kassapaate.edulliset, 3)

    def test_maukas_korttimaksu_nostaa_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rahaaOn)
        self.kassapaate.syo_maukkaasti_kortilla(self.rahaaOn)
        self.kassapaate.syo_maukkaasti_kortilla(self.rahaaOn)
        self.assertEqual(self.kassapaate.maukkaat, 3)

    def test_edullinen_korttimaksu_ei_nosta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rahaaOn)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttimaksu_ei_nosta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rahaaOn)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        #Epäonnistunut maksu
    def test_edullinen_epaonnistunut_korttimaksu_ei_veloiteta_kortilta(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.rahaaEiOle))

    def test_maukas_epaonnistunut_korttimaksu_ei_veloiteta_kortilta(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.rahaaEiOle))

    def test_edullinen_epaonnistunut_korttimaksu_ei_nosta_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rahaaEiOle)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_epaonnistunut_korttimaksu_ei_nosta_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rahaaEiOle)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_epaonnistunut_korttimaksu_ei_nosta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.rahaaEiOle)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_epaonnistunut_korttimaksu_ei_nosta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.rahaaEiOle)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        #Maksukortin lataus
    def test_onnistunut_kortinlataus_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.rahaaOn, 333)
        self.assertEqual(self.rahaaOn.saldo, 10333)

    def test_onnistunut_kortinlataus_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.rahaaOn, 333)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100333)

    def test_kortille_ei_voi_ladata_negatiivista_arvoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.rahaaOn, -333)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)