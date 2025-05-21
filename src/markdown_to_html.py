from textnode import *
from markdown_processing import markdown_to_blocks, text_to_textnodes
from block_type import *
import re
from htmlnode import *

MD_sample = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
This is the same paragraph on a new line.

```
This is code that unleashes the **power within**
the **power within**
```

> This is a quote from the famous philosopher _Shrek_
> Ogres are like onions, they have layers


- This is the _first_ list item in a list block
- This is a `list` item
- This is **another** list item

1. This is the `first` list item in a list block
2. This is the _second_ item in a list block
3. This is the **third** item in a list block
"""

ex_para = """
This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
This is the same paragraph on a new line.
"""

test_block_code = """
```
This is code that unleashes the power within
the power within
```
"""

def leaf_value_to_html(block):
    leafnodes = []
    text_nodes = text_to_textnodes(block)
    html_to_be_joined = []
    for node in text_nodes:
        leafnodes.append(text_node_to_html_node(node))
    for leaf in leafnodes:
        html_to_be_joined.append(leaf.to_html())
    #print(html_to_be_joined)
    joined_html = ''.join(html_to_be_joined)
    #print(joined_html)
    return joined_html
#leaf_value_to_html(ex_para)

def remove_newline(block):
    out_list = []
    lines = block.split("\n")
    #print(lines)
    for line in lines:
        if line != '':
            out_list.append(line)
    out = " ".join(out_list)
    #print(out)
    return out
#remove_newline(ex_para)

def remove_markdown_code_format(block):
    lines = block.split("\n")
    stripped_lines = []
    out_lines = []
    for line in lines:
        #print(line)
        if line != '':
            stripped_lines.append(f'{line.strip("`")}\n') # strips backticks, re-adds newlines
    #print(stripped_lines)
    for s_line in stripped_lines:
        if s_line != '\n':  #eliminates excess newlines from adding newline to blanks
            out_lines.append(s_line)
    #print(out_lines)


    out = "".join(out_lines)
    #print(out)
    return out
#remove_markdown_code_format(test_block_code)

def code_block_to_parent_child(block, outer_tag, inner_tag):
    child = LeafNode(inner_tag, block)
    parent = ParentNode(outer_tag, [child]) #child must be list to be iterable, necessary for .to_html
    #print("parent:", parent)
    #print("child:", child)
    return parent
#block_to_parent_child(test_block, "pre", "code")

test_block_quote = '''
> This is a quote from the famous philosopher Shrek
> Ogres are like onions, they have layers
'''
def remove_markdown_quote_format(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if line != '':
            stripped_lines.append(f'{line[2:len(line)]}\n')
    #print(stripped_lines)
    out = "".join(stripped_lines)
    #print(stripped_lines[0] + out.strip("\n"))
    return "\n" + out

remove_markdown_quote_format(test_block_quote)
unordered_example = """
- This is the first list item in a list block
- This is a list item
- This is another list item
"""

def remove_markdown_unordered_list_format(block): #prepares text to be HTMLNode value
    lines = block.split("\n")
    stripped_lines = []
    
    for line in lines:
        if line != '' and line != line[0]:
            stripped_lines.append(f'{line.strip('- ')}\n')
    pre_out = "".join(stripped_lines)
    out = (pre_out.strip("\n")) #previously added newline to start of pre_out
    #print(out)
    return out

#remove_markdown_list_format(unordered_example, "- ")
ordered_example = """
1. This is the first list item in a list block
2. This is the second item in a list block
3. This is the third item in a list block
"""

def remove_markdown_ordered_list_format(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if line != '':
            stripped_lines.append(f'{line[3:(len(line))]}\n')
    pre_out = "".join(stripped_lines)
    out = pre_out.strip("\n")
    #print(out)
    return out
    
#remove_markdown_ordered_list_format(ordered_example)

def markdown_ordered_list_to_parent_child(block):
    children = []
    value_to_be = remove_markdown_ordered_list_format(leaf_value_to_html(block))
    lines = value_to_be.split("\n")
    for line in lines:
        children.append(LeafNode("li", f'{line}'))
    parent = ParentNode("ol", children)
    return parent

def markdown_unordered_list_to_parent_child(block, outer_tag, inner_tag):
    children = []
    value_to_be = remove_markdown_unordered_list_format(leaf_value_to_html(block))
    lines = value_to_be.split("\n")
    for line in lines:
        children.append(LeafNode(inner_tag, f'{line}'))
    parent = ParentNode(outer_tag, children)
    return parent

#markdown_list_to_parent_child(unordered_example, "ul", "li")


def markdown_to_html_node(markdown_doc):
    blocks = markdown_to_blocks(markdown_doc)
    html_nodes = []
    for block in blocks:
        heading_number = re.findall(r"\#{1,10}\s", block)
        bl_type = block_to_block_type(block)
        if bl_type == BlockType.PARA:
            html_nodes.append(LeafNode("p", remove_newline(leaf_value_to_html(block)))) #<p>
        if bl_type == BlockType.HEAD:
            html_nodes.append(LeafNode(f"h{len(heading_number[0])-1}", leaf_value_to_html(block.strip("# ")))) #<h1> - <h6>
        if bl_type == BlockType.CODE:
            html_nodes.append(code_block_to_parent_child(remove_markdown_code_format(block), "pre","code")) #<pre><code>
        if bl_type == BlockType.QUOTE:
            html_nodes.append(LeafNode("blockquote", remove_markdown_quote_format(leaf_value_to_html(block)))) #<blockquote>
        if bl_type == BlockType.UNORDERED: # <ul> <li>
            html_nodes.append(markdown_unordered_list_to_parent_child(block, "ul", "li"))
        if bl_type == BlockType.ORDERED: #<ol> <li>
            html_nodes.append(markdown_ordered_list_to_parent_child(block))

        #print("block:", block, "type:", bl_type)
        #print("type:", bl_type)
    #print(html_nodes)
    div_parent = ParentNode("div", html_nodes)

    #print(div_parent.to_html())
    return div_parent

trouble = """
This is text with _an_ image ![fake image](www.loweffort.com/&*44LAZY.nope)
and a second **image** ![potato](www.notareal_linktoapotatoimage.com)
"""
markdown_to_html_node(trouble)