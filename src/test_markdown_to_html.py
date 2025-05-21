import unittest
from textnode import *
from markdown_processing import markdown_to_blocks, text_to_textnodes
from block_type import *
import re
from htmlnode import *
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_quote(self):
        md = """
> This is a quote from the famous philosopher **Shrek**
> Ogres are like onions, they have layers
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>\nThis is a quote from the famous philosopher <b>Shrek</b>\nOgres are like onions, they have layers\n</blockquote></div>"
        )
    def test_link(self):
        md = """
This is a paragraph with a link [Gameinformer](https://www.gameinformer.com/)
_bro_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a paragraph with a link <a href="https://www.gameinformer.com/">Gameinformer</a> <i>bro</i></p></div>'
        )
    
    def test_image(self):
        md = """
    This is text with an image ![fake image](www.loweffort.com/&*44LAZY.nope)
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is text with an image <img src="www.loweffort.com/&*44LAZY.nope" alt="fake image" /></p></div>'
        )

if __name__ == "__main__":
    unittest.main()