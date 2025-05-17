"""
    if delimiter == None:
            for node in old_nodes:
                match(node.text_type):
                    case(TextType.TEXT):
                        pass#add code to append unaltered node to list
                    case(TextType.BOLD):
                        new_node = node.text.split("**")
                        new_nodes.extend(new_node)
                    case(TextType.ITALIC):
                        new_node = node.text.split("_")
                        new_nodes.extend(new_node)
                    case(TextType.CODE):
                        new_node - node.text.split("`")
                        new_nodes.extend(new_node)
                        """
    #attempt at  markdown_processing | split_nodes_delimiter
"""
    if delimiter == None:
        for node in old_nodes:
            if node.text_type == TextType.TEXT:
                pass
            if node.text_type == TextType.BOLD:
                content = node.text.split("**")
                for index_zero in content:
                    if index_zero == content[1]:
                        nu_node = TextNode(index_zero, TextType.BOLD)
                        new_nodes.append(nu_node)
                    else:
                        nu_node = TextNode(index_zero,TextType.TEXT )
                        new_nodes.append(nu_node)
            if node.text_type == TextType.ITALIC:
                pass
            if node.text_type == TextType.CODE:
                content = node.text.split("`")
                for index_zero in content:
                    if index_zero == content[1]:
                        nu_node = TextNode(index_zero, TextType.CODE)
                        new_nodes.append(nu_node)
                    else:
                        nu_node = TextNode(index_zero,TextType.TEXT )
                        new_nodes.append(nu_node)
    print(new_nodes)
"""
#attempt at  markdown_processing | split_nodes_delimiter, goes beyond scope of what is required
#likely needs to use recursion to produce a full list of TextNodes, perhaps break this into smaller functions lalter?

"""
else:    #if node.text_type == TextType.TEXT
               #sections = []
               sectionstwo = []
               extracted = extract_markdown_images(node.text)
               if extracted == []: #If extraction returns nothing, add node to list as is
                   new_nodes.append(node)
               for tuple in extracted:

                   alt = tuple[0]
                   ilink = tuple[1]
                   #print(alt, ilink)
                   sections = node.text.split(f"![{alt}]({ilink})")
                   for sect in sections:
                       
                    new_nodes.append(TextNode(sect, TextType.TEXT))
                    """
#attempted code for split_nodes_image in markdown processing, if this implementation were to
#work, it would require several convoluted steps and likely not cover all cases

"""nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    for node in nodes:
        bold_match = re.findall(r"\*(.*?)\*", node.text)
        italic_match = re.findall(r"\_(.*?)\_", node.text)
        code_match = re.findall(r"\`(.*?)\`", node.text)
        if bold_match != []:
            nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        if italic_match != []:
            nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        if code_match != []:
            nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    """