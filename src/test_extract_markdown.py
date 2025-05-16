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


if __name__ == "__main__":
    unittest.main()