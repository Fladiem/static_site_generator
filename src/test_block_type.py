import unittest
from block_type import BlockType, block_to_block_type

class test_BT(unittest.TestCase):

    def test_paragraph(self):
        
        paragraph = "This is just a normal paragraph.\nMost humble."
        correct_BT = BlockType.PARA
        self.assertEqual(block_to_block_type(paragraph), correct_BT)
    def test_heading(self):
        blank = ''
        not_heading = "# This is a heading\n## This is a second heading\n### third\n#### fourth\n##### fifth\n###### sixth\n####### seventh"
        heading = "# This is a heading\n## This is a second heading\n### third\n#### fourth\n##### fifth\n###### sixth"
        correct_BT = BlockType.HEAD
        self.assertEqual(block_to_block_type(heading), correct_BT)
        self.assertNotEqual(block_to_block_type(not_heading), correct_BT)
        self.assertNotEqual(block_to_block_type(blank), correct_BT)
    def test_code(self):
        blank = ''
        not_code = "````\nThis is not code\n````"
        code = "```\nThis is code\n```"
        correct_BT = BlockType.CODE
        self.assertEqual(block_to_block_type(code), correct_BT)
        self.assertNotEqual(block_to_block_type(not_code), correct_BT)
        self.assertNotEqual(block_to_block_type(blank), correct_BT)
    def test_quote(self):
        blank = ''
        not_quote = ">> This is a quote\n> From the famous philosopher Lord Farquad"
        quote = "> This is a quote\n> From the famous philosopher Shrek"
        correct_BT =BlockType.QUOTE
        self.assertEqual(block_to_block_type(quote), correct_BT)
        self.assertNotEqual(block_to_block_type(not_quote), correct_BT)
        self.assertNotEqual(block_to_block_type(blank), correct_BT)
    def test_unordered(self):
        blank = ''
        not_unordered = "- This is the first ordered entry\n2. This is the second ordered entry"
        unordered = "- This is the first list entry\n- This is the second list entry"
        correct_BT = BlockType.UNORDERED
        self.assertEqual(block_to_block_type(unordered), correct_BT)
        self.assertNotEqual(block_to_block_type(not_unordered), correct_BT)
        self.assertNotEqual(block_to_block_type(blank), correct_BT)
    def test_ordered(self):
        blank = ''
        not_ordered = "1. This is the first list entry\n- This is the second list entry"
        ordered = "1. This is the first ordered entry\n2. This is the second ordered entry"
        correct_BT = BlockType.ORDERED
        self.assertEqual(block_to_block_type(ordered), correct_BT)
        self.assertNotEqual(block_to_block_type(not_ordered), correct_BT)
        self.assertNotEqual(block_to_block_type(blank), correct_BT)

if __name__ == "__main__":
    unittest.main()