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
        

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_link(self):
        nodes = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
        new_nodes = [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode(
            "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
        ),
    ]
        self.assertEqual(split_nodes_link(nodes), new_nodes)
    def test_split_link_extras(self):
        nodes = [TextNode("This is **bold** text", TextType.BOLD),
                 TextNode("This is text with a link to [Gameinformer](https://www.gameinformer.com/) and to [python.org](https://docs.python.org/3/library/stdtypes.html#str.split) and also nothing", TextType.TEXT),
                 TextNode("This is text with an image ![fake image](www.loweffort.com/&*44LAZY.nope)", TextType.IMAGE)]
        new_nodes = [TextNode("This is **bold** text", TextType.BOLD),
                     TextNode("This is text with a link to ", TextType.TEXT),
                     TextNode("Gameinformer", TextType.LINK, "https://www.gameinformer.com/"),
                     TextNode(" and to ", TextType.TEXT),
                     TextNode("python.org", TextType.LINK, "https://docs.python.org/3/library/stdtypes.html#str.split"),
                     TextNode(" and also nothing", TextType.TEXT),
                     TextNode("This is text with an image ![fake image](www.loweffort.com/&*44LAZY.nope)", TextType.IMAGE)]
        self.assertEqual(split_nodes_link(nodes), new_nodes)

    def test_split_image_extras(self):
        nodes = [TextNode("This is **bold** text", TextType.BOLD),
                 TextNode("This is text with a link to [Gameinformer](https://www.gameinformer.com/) and to [python.org](https://docs.python.org/3/library/stdtypes.html#str.split) and also nothing", TextType.TEXT),
                 TextNode("This is text with an image ![fake image](www.loweffort.com/&*44LAZY.nope) and also nothing.", TextType.TEXT)]
        new_nodes = [TextNode("This is **bold** text", TextType.BOLD),
                     TextNode("This is text with a link to [Gameinformer](https://www.gameinformer.com/) and to [python.org](https://docs.python.org/3/library/stdtypes.html#str.split) and also nothing", TextType.TEXT),
                     TextNode("This is text with an image ", TextType.TEXT),
                     TextNode("fake image", TextType.IMAGE, "www.loweffort.com/&*44LAZY.nope"),
                     TextNode(" and also nothing.", TextType.TEXT)]
        self.assertEqual(split_nodes_image(nodes), new_nodes)
    def test_split_images_basic(self):
        node = TextNode("This is a chicken wing", TextType.TEXT)
        new_nodes = [TextNode("This is a chicken wing", TextType.TEXT)]
        self.assertEqual(split_nodes_link(node), new_nodes)
    
    def test_split_link_basic(self):
        node = TextNode("This is a thimble of https://www.gobbagooblin.com/butter", TextType.TEXT)
        new_nodes = [TextNode("This is a thimble of https://www.gobbagooblin.com/butter", TextType.TEXT)]
        self.assertEqual(split_nodes_link(node), new_nodes)
    
    def test_text_to_textnodes(self):
        node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes =[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
        self.assertEqual(text_to_textnodes(node), new_nodes)
    def test_text_to_textnodes_oppositeorder(self):
        #![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) [link](https://boot.dev)
        node = "This is text with a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev). There's also a `code block`, _italic word_ and a **bold word**."
        new_nodes =[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
    TextNode(". There's also a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(", ", TextType.TEXT),
    TextNode("italic word", TextType.ITALIC),
    TextNode(" and a ", TextType.TEXT),
    TextNode("bold word", TextType.BOLD),
    TextNode(".", TextType.TEXT)
]
        self.assertEqual(text_to_textnodes(node), new_nodes)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        ) 
    
    def test_markdown_to_blocks_extra_newlines(self):
        md = '''
# This is a heading.

The heading is terrified of all the newlines.




Newlines everywhere




in the walls



there is no escape from the newlines
NO ESCAPE




'''
        blocks = markdown_to_blocks(md)
        test_blocks = [
            "# This is a heading.", 
            "The heading is terrified of all the newlines.",
            "Newlines everywhere",
            "in the walls",
            "there is no escape from the newlines\nNO ESCAPE"
        ]
        self.assertEqual(blocks, test_blocks)
    def test_markdown_blocks_jank(self):
        md = """ &&*&^This is a chicken wingThisisachickenwing
golfingpotato
fig newnuton

nest
needle

normandy




bort """
        blocks = markdown_to_blocks(md)
        test_blocks = ["&&*&^This is a chicken wingThisisachickenwing\ngolfingpotato\nfig newnuton",
                       "nest\nneedle",
                       "normandy",
                       "bort"]
        self.assertEqual(blocks, test_blocks)

     
if __name__ == "__main__":
    unittest.main()