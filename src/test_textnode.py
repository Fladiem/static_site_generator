import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node3 = "spaghettmo" #TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2, node3)
    def test_URL_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None) 
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)    #default for no input should be None
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()