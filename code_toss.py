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

"""
def block_to_parent_child(block, outer_tag, inner_tag):
    child = LeafNode(inner_tag, block)
    parent = ParentNode(outer_tag, child)
    #print("parent:", parent)
    #print("child:", child)
    return parent, child
#block_to_parent_child(test_block, "pre", "code")
"""
'block_to_parent_child(block.strip("`"), "pre","code")' #previously implemented for BlockType.CODE in markdown_to_html
 #returns parent, child combination based tags provided. Created with focus on...
#code blocks.
"""
        filepath = current_filepath + "/" + path

        if path is None:
            filepath_storage.append(filepath)
            print("if:", filepath_storage)
        else:
            filepath_storage.extend(static_to_public(filepath))
            print("else:", filepath_storage)
"""
### Maybe be relevant to HTML formatting
"""def create_markdown_image(alt_text):
    MD_text = f'![{alt_text}]'
    #print(MD_text)
    def create_URL(url):
    
        MD_url = url.replace('(', '%28')  ###
        MD_url = MD_url.replace(')', '%29') ###
        MD_url = f'({MD_url})'
        MD_T_URL = MD_text + MD_url
        def create_title(title=None):   #establishes None as default, making the following if statement work
            if title:      #if title is not None...
                MD_title = f'"{title}"'
                rm_par = MD_T_URL.strip(')')
                MD_T_URL_ti = f'{rm_par} {MD_title})'   #rm_par + ' ' + MD_title + ')'
                return MD_T_URL_ti
            
            return MD_T_URL
        return create_title
    return create_URL"""
###May be relevant to HTML formatting

"""current_filepath = f'{parent_directory}'
    dir_list = []
    filepath_storage = []
    directories = {}
    if os.path.isdir(current_filepath):
         dir_list.append(os.listdir(current_filepath))
         iterable_list = os.listdir(current_filepath)
         for a_path in iterable_list:
              current_filepath = current_filepath + "/" + a_path
              if os.path.isdir(current_filepath):
                   dir_list.append(os.listdir(current_filepath))
                   print(current_filepath)
              current_filepath = current_filepath
    else: 
         return""" #attempt at static_to_public

"""base_filepath = f'{parent_directory}'
        current_filepath = f'{parent_directory}'
        for a_path in initial_list:
            current_filepath = current_filepath + "/" + a_path
            if os.path.isdir(current_filepath): #recursively call here
                new_list = os.listdir(current_filepath)
                interact_check.append(current_filepath)
                print('new list:', new_list)
                print(current_filepath)
                copy_to_public(new_list)
                current_filepath = base_filepath
                

                if os.path.isdir(a_path) == False:
                    current_filepath = current_filepath + "/" + a_path
                    interact_check.append(current_filepath)
                    #print (a_path)
                    print("filepath:", current_filepath)
                    current_filepath = base_filepath
            else:
                print(interact_check)""" #attempt at static_to_public
####
#### Recursion? How does that work?
"""filepath_storage = []
    dir_list = os.listdir(initial_filepath)
    for content in dir_list:
        current_filepath = initial_filepath + '/' + content
        
        if os.path.isdir(current_filepath) != True:
            filepath_storage.append(current_filepath)
            

        else:
            filepath_storage.extend(static_to_public(current_filepath, initial_filepath))
    print(filepath_storage)"""
####
#Initial attempt to generate webpages, only works for directories one layer deep: ex_dir/file
"""
    if os.path.exists(dest_path):
        HTML_page = open(dest_path, mode="w")
        HTML_page.write("")
        HTML_page.write(rep_template)
        HTML_page.close()

    elif os.path.exists(dest_path) != True:
        if os.path.isdir(dest_path) != True:  #dest_path_list[0]
            os.makedirs(dest_path)
        #HTML_page = open(dest_path, mode="x")
        #HTML_page.write(rep_template)
        #HTML_page.close()
"""
#Initial attempt to generate webpages, only works for directories one layer deep: ex_dir/file


#implementation of two separate functions for splitting images and links causes errors on lists including consecutive links or images, based on what is called first
#in text_to_text_nodes, replaced with one function

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

##implementation of two separate functions for splitting images and links causes errors on lists including consecutive links or images, based on what is called first
#in text_to_text_nodes, replaced with one function


#### or not? Combined function difficult to make work the same way
def split_nodes_images_and_links(old_nodes):
    img_nodes = []
    link_nodes = []
    out_nodes = []
    extracted_images = []
    extracted_links = []

    if isinstance(old_nodes, list) == False: #allows function to work if old_nodes a single text node.
        old_nodes = [old_nodes]
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
                img_nodes.append(node)    #nodes that do not need editing are appended to out_nodes

        extracted_images = extract_markdown_images(node.text)
        extracted_links = extract_markdown_links(node.text)
        #print("images:", extracted_images)
        #print("links:", extracted_links)
        
        if extracted_images != []:

            if extract_markdown_images == [] and node not in img_nodes:
                img_nodes.append(node)
            for alt, ilink in extracted_images:
                img_section = node.text.split(f'![{alt}]({ilink})', 1)
                if img_section[0]:
                    img_nodes.append(TextNode(img_section[0], TextType.TEXT))
                node.text = img_section[1]
                img_nodes.append(TextNode(alt, TextType.IMAGE, ilink))
                if alt == extracted_images[[-1][0]]:  #When final image is reached split one more time
                    last_image_section = original_text.split(f"[{alt}]({ilink})")
                    img_nodes.append(TextNode(last_image_section[1], TextType.TEXT))

            out_nodes.extend(img_nodes)
            

        if extracted_links != []:

            if extract_markdown_links == [] and node not in link_nodes:
                link_nodes.append(node)
            for anchor, link in extracted_links:
                link_section = node.text.split(f"[{anchor}]({link})", 1)  #split non link text from link text
                if link_section[0]:
                    link_nodes.append(TextNode(link_section[0], TextType.TEXT))  #convert text before first link to TextNode with TextType.TEXT
                node.text = link_section[1]
                link_nodes.append(TextNode(anchor, TextType.LINK, link))
                if anchor == extracted_links[-1][0]:
                    last_link_section = original_text.split(f"[{anchor}]({link})")
                    #print(last_link_sections)
                    link_nodes.append(TextNode(last_link_section[1], TextType.TEXT))
                   
            out_nodes.extend(link_nodes)
    count = 0
    for node in out_nodes:
        count += 1
        if node.text == '':
            del out_nodes[count - 1]
    
    
    #print(out_nodes)
    return out_nodes
#### or not? Combined function difficuklt to make work the same way
