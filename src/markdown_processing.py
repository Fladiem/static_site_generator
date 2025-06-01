
from htmlnode import *
from textnode import *
from extract_markdown import extract_markdown_images, extract_markdown_links

uno_list_trouble = """
- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
"""
uno_list_tnode = [TextNode('''
- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)'''
, TextType.TEXT, None)]
unoLT_image_check = """  
- ![alt text](url)
- ![2alt](2rl)
- ![3alt](3rl)
"""
unoLT_imte_node = [TextNode('''  
- ![alt text](url)
- ![2alt](2rl)
- ![3alt](3rl)'''
, TextType.TEXT, None)]

combined_test = [TextNode('''  
- ![alt text](url)
- ![2alt](2rl)
- ![3alt](3rl)'''
, TextType.TEXT, None), TextNode('''
- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty) **haberber**'''
, TextType.TEXT, None)]

def split_nodes_delimiter(old_nodes, delimiter, text_type): #converts old_nodes into, potentially, a list of multiple new TextType nodes.
    #handles inline code, bold and italic text
    # ** = bold
    # _ = italic
    # ` = code
    valid_delimiters = ["**", "_", "`"]
    
    new_nodes = [] #holds values to be added to nodes_out
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
    img_nodes = []
    out_nodes = []

    if isinstance(old_nodes,list) == False:   #allows function to work when old_nodes is one TextNode rather than a list
        old_nodes = [old_nodes]

    for node in old_nodes: 
        original_text = node.text
        if node.text_type != TextType.TEXT:  #add node to list as is
            img_nodes.append(node)
            
        else:    #if node.text_type == TextType.TEXT
               
               extracted_images = extract_markdown_images(node.text)
               if extracted_images == [] and node not in img_nodes: #If extraction returns nothing, add node to list as is
                   img_nodes.append(node)
               
               for alt, ilink in extracted_images:
    
                   section = node.text.split(f"![{alt}]({ilink})", 1)
                   #print(sections)

                   if section[0]:
                       img_nodes.append(TextNode(section[0], TextType.TEXT))
                   node.text = section[1]
 
                   img_nodes.append(TextNode(alt, TextType.IMAGE, ilink))
                   if alt == extracted_images[-1][0]:
                
                     last_sections = original_text.split(f"[{alt}]({ilink})")
                     img_nodes.append(TextNode(last_sections[1], TextType.TEXT))
                              
    out_nodes.extend(img_nodes)
         
    count = 0               #removes TextNodes with empty contents
    for node in out_nodes:
        count += 1
        if node.text == '':
            del out_nodes[count-1]              
    
    #print(img_nodes)
    #print(out_nodes)
    return out_nodes
#split_nodes_image(uno_list_tnode)
                   
def split_nodes_link(old_nodes):
    new_nodes = []
    out_nodes = []
    
    if isinstance(old_nodes, list) == False:  #Allows function to work when old_nodes is not a list
        old_nodes = [old_nodes]
    for node in old_nodes:
        original_text = node.text
        #print(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        extracted_links = extract_markdown_links(node.text)
        if extracted_links == [] and node not in new_nodes: #adds node to new_nodes unmodified if no matches are returned
            new_nodes.append(node)
        for anchor, link in extracted_links:
            #print(extracted_links[-1][0])
            #print (anchor, link)
            section = node.text.split(f"[{anchor}]({link})", 1) ## edited for error Ch5 - 3, forgot max split
            #print(section)
            if section[0]:
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            node.text = section[1]
            new_nodes.append(TextNode(anchor, TextType.LINK, link))
            if anchor == extracted_links[-1][0]:
                #print(original_text)
                last_sections = original_text.split(f"[{anchor}]({link})")
                new_nodes.append(TextNode(last_sections[1], TextType.TEXT))        
    out_nodes.extend(new_nodes)

    count = 0
    for node in new_nodes:
        count += 1
        if node.text == '':
            del new_nodes[count-1]
    #print(new_nodes)
    return new_nodes
#split_nodes_link(uno_list_tnode)
        
#split_nodes_images_and_links(uno_list_tnode)
#split_nodes_images_and_links(unoLT_imte_node)
#split_nodes_images_and_links(combined_test)
          
def text_to_textnodes(text): #This function uses the previous functions to convert markdown text to a list of nodes.
    out = []
    if isinstance(text, str):
        old_nodes = [TextNode(text, TextType.TEXT)]
        #print(old_nodes)
        
    if isinstance(text, TextNode):
        old_nodes = [text]
    
    if isinstance(text, list):
        old_nodes = text
        
    for node in old_nodes:  #modifies nodes individually with all split_nodes functions
        #print(old_nodes, node)
        #print(node)
        nodes = node
        if extract_markdown_images(node.text) !=[]:
            nodes = split_nodes_image(nodes)
        if extract_markdown_links(node.text) != []:
            nodes = split_nodes_link(nodes)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        
        out.extend(nodes) #adds processed nodes to output for return
    #print(out)
    return out
#text_to_textnodes(combined_test)

def markdown_to_blocks(text):   #Ch4 section 1  Converts markdown to blocks  blocks are a list
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
#markdown_to_blocks(uno_list_trouble)
#markdown_to_blocks(tolk_trouble)


