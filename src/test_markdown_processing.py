import unittest
from markdown_processing import *
from textnode import *

class test_MD_processing(unittest.TestCase):
    def test_italics(self):  #nold (old_node)
        nold = [TextNode("This is text with a `code block` word", TextType.TEXT),
              TextNode("This text will be bold", TextType.BOLD),
              TextNode("This is text with a _italic_ word", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(nold, "_", TextType.ITALIC), 
                         [TextNode("This is text with a `code block` word", TextType.TEXT),
                          TextNode("This text will be bold", TextType.BOLD),
                          TextNode("This is text with a ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC),
                          TextNode(" word", TextType.TEXT)])
    def test_invalid_MD_syntax(self):
        nold = [TextNode("Chazz it _up_", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nold, "goose", TextType.TEXT)
            self.assertTrue('Invalid Markdown Syntax in delimiter. Valid arguments are "**", "_", "`"' in
            str(context.exception))
    def test_bold_italics_code(self):
        nold = [TextNode("Equals _italic_", TextType.TEXT),
                TextNode("Equals `code`", TextType.TEXT),
                TextNode("Equals **bold**", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(nold, "`", TextType.CODE),
                          [TextNode("Equals _italic_", TextType.TEXT),
                           TextNode("Equals ", TextType.TEXT),
                           TextNode("code", TextType.CODE),
                           TextNode("Equals **bold**", TextType.TEXT)])

        
if __name__ == "__main__":
    unittest.main()