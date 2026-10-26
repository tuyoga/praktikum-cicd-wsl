import unittest
from app import tambah


class TestTambah(unittest.TestCase):
    def test_penjumlahan_positif(self):
        self.assertEqual(tambah(10, 5), 15)

    def test_penjumlahan_nol(self):
        self.assertEqual(tambah(0, 5), 5)

    def test_penjumlahan_negatif(self):
        self.assertEqual(tambah(-2, 5), 3)


if __name__ == "__main__":
    unittest.main()
