import os
import pathlib
import sys
from textnode import *
from markdown_processing import markdown_to_blocks, text_to_textnodes
from extract_markdown import extract_title
from block_type import *
import re
from htmlnode import *


basepath = sys.argv[0]

#if sys.argv[0] == '':
    #basepath = "/"

uno_list_trouble = '- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)\n- [Why Tom Bombadil Was a Mistake](/blog/tom)\n- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)'

unoLT_image_check = """  
- ![alt text](url)
- ![2alt](2rl)
- **ollo** ![3alt](3rl)
"""
def leaf_value_to_html(block):
    leafnodes = []
    #print(block)
    text_nodes = text_to_textnodes(block)
    #print(text_nodes)
    html_to_be_joined = []
    for node in text_nodes:
        #print(node)
        #print(text_node_to_html_node(node))
        leafnodes.append(text_node_to_html_node(node))
    for leaf in leafnodes:
        html_to_be_joined.append(leaf.to_html())
    #print(html_to_be_joined)
    joined_html = ''.join(html_to_be_joined)
    #print(joined_html) ######## HERE, the problem is HERE   NEVERMIND, problem is - removal
    return joined_html
#leaf_value_to_html(uno_list_trouble)

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

def remove_markdown_quote_format(block):
    lines = block.split(">")
    stripped_lines = []
    for line in lines:
        if line != '':
            stripped_lines.append(line.strip(" "))
    #print(stripped_lines)
    out = "".join(stripped_lines)
    #print(out.strip("\n "))
    return out.strip("\n ") #previously adding newline in front of out? erroneous?

#remove_markdown_quote_format(test_block_quote)


def remove_markdown_unordered_list_format(block): #prepares text to be HTMLNode value
    lines = block.split("\n")
    stripped_lines = []
    #print(lines)
    
    for line in lines:
        #print(line)
        if line != '': #and line != line[0]:
            stripped_lines.append(f'{line[2:len(line)]}\n')  # f"{line.strip('- ')}"
    pre_out = "".join(stripped_lines)
    #print(pre_out)
    out = (pre_out.strip("\n")) #previously added newline to start of pre_out
    #print(out)
    return out

#remove_markdown_unordered_list_format(uno_list_trouble)

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

def markdown_unordered_list_to_parent_child(block): #, outer_tag, inner_tag
    children = []
    value_to_be = remove_markdown_unordered_list_format(block)
    #print("1", value_to_be)
    value_to_be = leaf_value_to_html(value_to_be)
    #print("2", value_to_be)
    lines = value_to_be.split("\n")
    for line in lines:
        children.append(LeafNode("li", f'{line}'))
    parent = ParentNode("ul", children)
    return parent

#markdown_unordered_list_to_parent_child(uno_list_trouble) ####examine


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
            edited = remove_markdown_quote_format(block)
            html_nodes.append(LeafNode("blockquote", leaf_value_to_html(edited))) #<blockquote>
        if bl_type == BlockType.UNORDERED: # <ul> <li>
            html_nodes.append(markdown_unordered_list_to_parent_child(block))
        if bl_type == BlockType.ORDERED: #<ol> <li>
            html_nodes.append(markdown_ordered_list_to_parent_child(block))

        #print("block:", block, "type:", bl_type)
        #print("type:", bl_type)
    #print(html_nodes)
    div_parent = ParentNode("div", html_nodes)

    #print(div_parent.to_html())
    return div_parent

#markdown_to_html_node(unoLT_image_check)

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    if os.path.isfile(from_path): #if from_path is a file...
        from_path_file = open(from_path, mode= 'r') #open the file
        markdown = from_path_file.read() #read the file, assign its contents to markdown variable
        from_path_file.close() #closes the file
    #print(markdown)
    if os.path.isfile(template_path):
        template_file = open(template_path)
        template = template_file.read()
        template_file.close()
    #print(template)
    processed_MD = markdown_to_html_node(markdown)
    MD_as_HTML = processed_MD.to_html()
    #print(processed_MD.to_html())
    MD_title = extract_title(markdown) #perhaps edit to grab info from HTML instead?
    #print(MD_title)
    rep_template= template.replace("{{ Title }}", MD_title )
   
    rep_template = rep_template.replace("{{ Content }}", MD_as_HTML)
    #print(rep_template)
    dest_path_sections = dest_path.split("/") #current implementation supports one directory in path
    new_path = ""

    if os.path.exists(dest_path):

        HTML_page = open(dest_path, mode="w")
        HTML_page.write("")
        HTML_page.write(rep_template)
        HTML_page.close()
    #if os.path.exists(dest_path) != True:
    else:
        for i in range(0, len(dest_path_sections)):

            if dest_path_sections[i] != dest_path_sections[-1]:
                new_path = new_path + "/" + dest_path_sections[i]
        new_path = new_path.strip("/")
        os.makedirs(new_path, exist_ok=True)
        HTML_page = open(dest_path, mode="x")
        HTML_page.write(rep_template)
        HTML_page.close()
    return

def generate_pages_recursive(dir_path, template_path, dest_dir_path):
    print (f'Generating page from {dir_path} at {dest_dir_path} with {template_path}')

    if os.path.isfile(template_path): 
        template_file = open(template_path)
        template = template_file.read()
        template_file.close()
        #print(template)
        
    start_paths = os.listdir(dir_path)
    for start_path in start_paths:
        truestart = start_path
        start_path = os.path.join(dir_path, start_path)
        p = pathlib.PurePosixPath(start_path)
        dest_component = p.relative_to(dir_path)
        dest_path = os.path.join(dest_dir_path, dest_component)
        #dinko_path = dest_path.split("/")
        #dinko_path = "/".join(dinko_path[1:])
        #print(dinko_path)
        
        #print("start path:", start_path)
        #print(dest_path)
        if os.path.isfile(start_path):
            
            file_to_open = open(start_path)
            markdown = file_to_open.read()
            file_to_open.close()
            processed_MD = markdown_to_html_node(markdown)
            MD_as_HTML = processed_MD.to_html()
            MD_title = extract_title(markdown)
            replace_template = template.replace("{{ Title }}", MD_title)
            replace_template = replace_template.replace("{{ Content }}", MD_as_HTML)
            replace_template = replace_template.replace('href="/', f'href="{basepath}') #### Added for public page generation
            replace_template = replace_template.replace('src="/', f'src="{basepath}')  #### Added for public page generation
            dest_path_list = dest_path.split("/")
            file_path = dest_path_list[-1][0:-3]   #The end of start_path with .md removed: index
            dest_path_list = dest_path_list[0:-1] #start_path broken down into a list of each dir/sub dir, excluding file information
            dirs_path = "/".join(dest_path_list) #The path to start_path without the file at the end:  public/content
            
            os.makedirs(dirs_path, exist_ok=True)  #Makes the directory for file to be written in
            HTML_page = open(f'{dirs_path}/{file_path}.html', mode= "w") #will not work for any file type other than .md, consider use of Regex
            #HTML_page.write("")
            HTML_page.write(replace_template)
            HTML_page.close()

        if os.path.isdir(start_path):
            dest_path = os.path.join(dest_dir_path, truestart)
            os.makedirs(dest_path, exist_ok=True)
            start_item = start_path
            dest_item = dest_path
            #print (start_item, "-->", dest_item)
            generate_pages_recursive(start_item, 'template.html', dest_item)

    return
        
#generate_page("content/index.md", "template.html", "public/index.html")
#generate_pages_recursive("content", "template.html", "public")