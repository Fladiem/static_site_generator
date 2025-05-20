from htmlnode import *
from textnode import *
import re
from extract_markdown import extract_markdown_images, extract_markdown_links


linknode = [TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and to nothing",
    TextType.TEXT), TextNode("This is the second text with a link [to google](www.google.com)", TextType.TEXT), 
    TextNode("This is plain text with no link", TextType.TEXT),
    TextNode("This is text with an image ![fake image](www.loweffort.com/&*44LAZY.nope)", TextType.IMAGE)]
imagenode = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                     TextType.TEXT), TextNode("This is the second text with a ![grinch](https://giphy.com/gifs/thegoodfilms-vintage-cartoon-smiling-UTFiHeDL8cOSA)", TextType.TEXT),
                       TextNode("This is just text", TextType.TEXT)]
multitext = "This is _text_ with a **bold** word and a `code block` and a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
nonetext = "This is plain text with no **special** properties. I lied it has a bold word"
MD_sample = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
This is the same paragraph on a new line.





- This is the first list item in a list block
- This is a list item
- This is another list item
"""

md = """ &&*&^This is a chicken wingThisisachickenwing
golfingpotato
fig newnuton

nest
needle

normandy




bort """

#regardless of the scope MD text is in it should have no spaces or tabs before each line
#as above in MD_sample

def split_nodes_delimiter(old_nodes, delimiter, text_type): #converts old_nodes into, potentially, a list of multiple new TextType nodes.
    #handles inline code, bold and italic text
    # ** = bold
    # _ = italic
    # ` = code
    valid_delimiters = ["**", "_", "`"]
    
    new_nodes = [] #holds values to be added to added to nodes_out
    nodes_out = [] #final output of new nodes

    if isinstance(old_nodes, list) == False: #allows function to work when old_nodes is one TextNode rather than a list
        old_nodes = [old_nodes]
    
    if delimiter not in valid_delimiters:    
        raise Exception('Invalid Markdown Syntax in delimiter. Valid arguments are "**", "_", "`"')
      
    for node in old_nodes: #add node to list as is
       
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        if delimiter not in node.text and node.text_type == TextType.TEXT:
            new_nodes.append(node)
        
        if delimiter in node.text and node.text_type == TextType.TEXT:
            tlist = node.text.split(delimiter)
            if len(tlist) % 2 == 0:
                raise Exception('Invalid Markdown Syntax in text. Must have even number of delimiters. _italic_, not _italic')
           
            #The list will always follow the pattern [normal text, special text, normal text, special text]
            #Every other entry should have its text_type changed
            for i in range(0, len(tlist)):
                if (i+1) % 2 == 0:
                    nu_node = TextNode(tlist[i], text_type)
                    new_nodes.append(nu_node)
                else: #(i+1) % 2 != 0:
                    nu_node = TextNode(tlist[i], TextType.TEXT)
                    new_nodes.append(nu_node)

                #print(tlist[i], i)
                
    nodes_out.extend(new_nodes)
         
    count = 0               #removes TextNodes with empty contents
    for node in nodes_out:
        count += 1
        if node.text == '':
            del nodes_out[count-1]
           
    #print(nodes_out)
    return nodes_out

def split_nodes_image(old_nodes):
    #defaultTT = TextType.IMAGE
    new_nodes = []
    out_nodes = []

    if isinstance(old_nodes,list) == False:   #allows function to work when old_nodes is one TextNode rather than a list
        old_nodes = [old_nodes]

    for node in old_nodes: 
        original_text = node.text
        if node.text_type != TextType.TEXT:  #add node to list as is
            new_nodes.append(node)
            
            

        else:    #if node.text_type == TextType.TEXT
               
               extracted_images = extract_markdown_images(node.text)
               if extracted_images == [] and node not in new_nodes: #If extraction returns nothing, add node to list as is
                   new_nodes.append(node)
               
               for alt, ilink in extracted_images:
    
                   section = node.text.split(f"![{alt}]({ilink})", 1)
                   #print(sections)

                   if section[0]:
                       new_nodes.append(TextNode(section[0], TextType.TEXT))
                   node.text = section[1]
 
                   new_nodes.append(TextNode(alt, TextType.IMAGE, ilink))
                   if alt == extracted_images[-1][0]:
                
                     last_sections = original_text.split(f"[{alt}]({ilink})")
                     new_nodes.append(TextNode(last_sections[1], TextType.TEXT))
                   
                
               
    out_nodes.extend(new_nodes)
         
    count = 0               #removes TextNodes with empty contents
    for node in out_nodes:
        count += 1
        if node.text == '':
            del out_nodes[count-1]                
    
    #print(new_nodes)
    #print(out_nodes)
    return out_nodes
                   
def split_nodes_link(old_nodes):
    new_nodes = []
    section = []
    
    if isinstance(old_nodes, list) == False:  #Allows function to work when old_nodes is not a list
        old_nodes = [old_nodes]
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        
        extracted_links = extract_markdown_links(node.text)
        if extracted_links == [] and node not in new_nodes: #adds node to new_nodes unmodified if no matches are returned
            new_nodes.append(node)
        for anchor, link in extracted_links:
            #print(extracted_links[-1][0])
            #print (anchor, link)
            section = node.text.split(f"[{anchor}]({link})")
            #print(section)
            if section[0]:
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            node.text = section[1]
            new_nodes.append(TextNode(anchor, TextType.LINK, link))
            if anchor == extracted_links[-1][0]:
                #print(original_text)
                last_sections = original_text.split(f"[{anchor}]({link})")
                new_nodes.append(TextNode(last_sections[1], TextType.TEXT))

               
    #print(new_nodes)
    
    count = 0
    for node in new_nodes:
        count += 1
        if node.text == '':
            del new_nodes[count-1]
    
    return new_nodes
    
def text_to_textnodes(text): #This function uses the previous functions to convert markdown text to a list of nodes.
    out = []
    if isinstance(text, str):
        old_nodes = [TextNode(text, TextType.TEXT)]
        
    if isinstance(text, TextNode):
        old_nodes = [text]
    
    if isinstance(text, list):
        old_nodes = text
        #print(old_nodes)
    for node in old_nodes:  #modifies nodes individually with all split_nodes functions
        nodes = split_nodes_link(node)
        nodes = split_nodes_image(nodes)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        out.extend(nodes) #adds processed nodes to output for return
    #print(out)
    return out

def markdown_to_blocks(text):   #Ch4 section 1  Converts markdown to blocks
    blocks_index = 0
    stripped_blocks = []
    blocks = text.split("\n\n")
    #print(blocks, len(blocks))
    for block in blocks:
        blocks_index += 1
        if blocks[blocks_index-1] != '' and blocks[blocks_index-1] != '\n':
            
            #print("segment:", blocks[blocks_index-1])
            stripped_blocks.append(block.strip("\n "))  #strips whitespace and incorrect newlines
            #may need to specifically remove newline from index 0 only, but unlikely
    #print(stripped_blocks)
    return stripped_blocks

#split_nodes_link(linknode)
#text_to_textnodes(nonetext)
#markdown_to_blocks(MD_sample)
