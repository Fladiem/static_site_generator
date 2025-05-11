from htmlnode import *
from textnode import *

test_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),
              TextNode("This is text with a **bold** word", TextType.TEXT),
              TextNode("This is text with a **BOUWLD** word", TextType.TEXT)]
junk_nodes= TextNode("This is **chazztastic**", TextType.TEXT)
#temporary test_nodes list content holder: 

def split_nodes_delimiter(old_nodes, delimiter, text_type): #converts old_nodes into, potentially, a list of multiple new TextType nodes.
    #handles inline code, bold and italic text
    # ** = bold
    # _ = italic
    # ` = code
    valid_delimiters = ["**", "_", "`"]
    new_nodes = [] #holds values to be added to added to nodes_out
    nodes_out = []

    if isinstance(old_nodes, list) == False: #allows function to work when old_nodes is one TextNode rather than a list
        old_nodes = [old_nodes]
    if delimiter not in valid_delimiters:    
        raise Exception('Invalid Markdown Syntax in delimiter. Valid arguments are "**", "_", "`"')
    
      
    for node in old_nodes: #add node to list as is
       
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
    
    for node in old_nodes: #create list of new TextNodes
        
        if delimiter in node.text and node.text_type == TextType.TEXT:
            plist = node.text.split(delimiter)
            
            for text in plist:
                if text == plist[1]:
                    nu_node = TextNode(text, text_type)
                    new_nodes.append(nu_node)
                
                else:
                    nu_node = TextNode(text, node.text_type)
                    new_nodes.append(nu_node)
    
    
    
    
    nodes_out.extend(new_nodes)
    """      
    count = 0               #removes TextNodes with empty contents
    for node in nodes_out:
        count += 1
        if node.text == '':
            del nodes_out[count-1]
          """  

    #print(nodes_out)
    return nodes_out

split_nodes_delimiter(junk_nodes, "**", TextType.BOLD)

