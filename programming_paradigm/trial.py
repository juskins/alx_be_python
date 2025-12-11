import unittest
def find_sqr(number):
    """Returns the square of the given number."""
    return number * number 

# Write test code to verify the function works as expected

class TestFindSqr(unittest.TestCase):
    def test_positive_integer(self):
        """Test with a positive integer."""
        self.assertEqual(find_sqr(3), 9)

    def test_negative_integer(self):
        """Test with a negative integer."""
        self.assertEqual(find_sqr(-4), 16)

    def test_zero(self):
        """Test with zero."""
        self.assertEqual(find_sqr(0), 0)

    def test_positive_float(self):
        """Test with a positive float."""
        self.assertAlmostEqual(find_sqr(2.5), 6.25)

    def test_negative_float(self):
        """Test with a negative float."""
        self.assertAlmostEqual(find_sqr(-3.5), 12.25)
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    


# import json

# def process_json(data: dict, filename: str):
    
#     # Serialize the dictionary to a JSON file
#     json_string = json.dumps(data, indent=4)
#     with open(filename, 'w') as json_file:
#         json_file.write(json_string)

# process_json({'name': 'Alice', 'age': 30, 'city': 'New York'}, 'output.json')