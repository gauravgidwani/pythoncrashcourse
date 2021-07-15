import unittest

def get_descriptive_name(year,make,model=''):
    if model:
        long_name = f"{year} {make} {model}"
    else:
        long_name = f"{year} {make}"
    return long_name.title()

class CarTestCase(unittest.TestCase):
    def test_car_name(self):
        formatted_name = get_descriptive_name(2022,'hi')
        self.assertEqual(formatted_name, '2022 Hi')
    def test_car_name2(self):
        formatted_name = get_descriptive_name(2022,'hi','bye')
        self.assertEqual(formatted_name, '2022 Hi Bye')

if __name__ == '__main__':
    unittest.main()
