class TestConversorRomano(unittest.TestCase):
    
    def test_i(self):
        self.assertEqual(converte("I"), 1)

    def test_v(self):
        self.assertEqual(converte("V"), 5)

    def test_ii(self):
        self.assertEqual(converte("II"), 2)

    def test_xxii(self):
        self.assertEqual(converte("XXII"), 22)

    def test_ix(self):
        self.assertEqual(converte("IX"), 9)

    def test_xxiv(self):
        self.assertEqual(converte("XXIV"), 24)

if __name__ == '__main__':
    unittest.main()
