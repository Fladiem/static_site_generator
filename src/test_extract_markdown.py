from extract_markdown import *
#import re
import unittest

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches =  extract_markdown_links(
           "This is text with a link to [to_Gameinformer](https://www.gameinformer.com/) and to [to Regexer](https://regexr.com/)" 
        )
        self.assertListEqual([("to_Gameinformer", "https://www.gameinformer.com/"), ("to Regexer", "https://regexr.com/")], matches)

    def test_extract_title(self):
        blank = ""
        header_ex ="""
# The Last Roaming Glacier

content

## The Tlingit Tribe's Traditional Woodworking
"""
        blankmatch = extract_title(blank)
        match = extract_title(header_ex)
        self.assertEqual(match, "The Last Roaming Glacier")
        self.assertEqual(blankmatch, "No header detected! Example: # header1")
        #with self.assertRaises(Exception) as context:
            #extract_title(blank)
        #self.assertTrue("No header detected! Example: # header1" in str(context.exception))
        #Checking for Exception does not work here because the exception is handled...
        #through a Try block

if __name__ == "__main__":
    unittest.main()