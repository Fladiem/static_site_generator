import unittest

from textnode import *
from htmlnode import *
class Test_text_node_to_html(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This text node is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, HTMLNode("b", "This text node is bold"))
    def test_italic(self):
        node = TextNode("italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, HTMLNode("i", "italic"))
    def test_code(self):
        node = TextNode("this is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, HTMLNode("code", "this is code"))
    def test_link(self):
        node = TextNode("link", TextType.LINK, "alex.yiik")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, HTMLNode("a", "link", None, {"href": "alex.yiik"}))
    def test_image(self):
        node = TextNode("image", TextType.IMAGE, "alex.yiik")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, HTMLNode("img", '', None, {"src": "alex.yiik", "alt": "image"}))


if __name__ == "__main__":
    unittest.main()