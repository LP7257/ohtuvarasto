import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_asettaa_alkusaldon(self):
        varasto = Varasto(10, 5)
        self.assertAlmostEqual(varasto.saldo, 5)

    def test_konstruktori_rajoittaa_alkusaldon_tilavuuteen(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_liian_suuri_maara(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_maaran_lisaaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivisen_maaran_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-1)
        self.assertEqual(saatu, 0)
        self.assertEqual(self.varasto.saldo, 5)

    def test_ottaminen_vahemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(8)
        saatu = self.varasto.ota_varastosta(3)
        self.assertEqual(saatu, 3)
        self.assertEqual(self.varasto.saldo, 5)

    def test_ottaminen_tasmalleen_saldon_verran(self):
        self.varasto.lisaa_varastoon(5)

        saatu = self.varasto.ota_varastosta(5)

        self.assertEqual(saatu, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_ottaminen_nolla_maaraa(self):
        self.varasto.lisaa_varastoon(5)

        saatu = self.varasto.ota_varastosta(0)

        self.assertEqual(saatu, 0)
        self.assertEqual(self.varasto.saldo, 5)

    def test_ottaminen_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(5)

        saatu = self.varasto.ota_varastosta(8)

        self.assertEqual(saatu, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_varaston_merkkijonoesitys(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(
            str(self.varasto),
            "saldo = 5, vielä tilaa 5"
        )