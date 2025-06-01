from enum import Enum
import re
#START variables for test purposes
#paragraph = "This is just a normal paragraph.\nMost humble."
#heading = "# This is a heading\n## This is a second heading\n### third\n#### fourth\n##### fifth\n###### sixth\n#######seventh"
#code = "```\nThis is code\n```"
quote = "> This is a quote\n> From the **famous** philosopher Shrek"
trouble = ">"
#unordered_list = "- This is the first list entry\n- This is the second list entry"
uno_list_trouble = '- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)\n- [Why Tom Bombadil Was a Mistake](/blog/tom)\n- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)'
#ordered_list = "1. This is the first ordered entry\n2. This is the second ordered entry"  #END variables for test purposes

class BlockType(Enum): # Types of markdown blocks
    PARA = "BlockType.PARA" #Paragraph
    HEAD = "BlockType.HEAD" #Heading
    CODE = "BlockType.CODE" #Code
    QUOTE = "BlockType.QUOTE" # Quote
    UNORDERED = "BlockType.UNORDERED" # Unordered list
    ORDERED = "BlockType.ORDERED" # Ordered list


def block_to_block_type(block): #Takes a single block of markdown text and returns block type
    to_analyze = block.split("\n")
    #print(to_analyze)
    block_type = ''
    heading_matches = re.findall(r"\#{1,10}\s", block)
    heading_false = re.findall(r"\#{7,}", block)
    #print(heading_matches)
    #print(heading_false)
    code_matches_begin = re.findall(r"```[^`]", block[0:4])
    code_matches_end = re.findall(r"[^`]```", block[(len(block)-4):(len(block))])
    #print("start:", block[0:4], "end:", block[(len(block)-4):(len(block))])
    #print("code matches:", code_matches)
    quote_matches = []  #for identifying quote conditions
    uno_list_matches = [] #for identifying unordered list conditions
    count = 0
    ord_list_matches = [] #for identifying ordered list conditions

    for line in to_analyze:
        count += 1#starts count at 1, increments 1 for every line in to_analyze
        #count used to identify ordered lists
        #print(line)
        if line[0:2] == "> " or line == ">":
            quote_matches.append("T")
        if line[0:2] == "- ":
            uno_list_matches.append("T")
        if line[0:3] == f"{count}. ":
            ord_list_matches.append("T")
    
    if len(heading_matches) < 7 and heading_matches != [] and len(to_analyze) < 7 and heading_false == []:
        block_type = BlockType.HEAD
    elif code_matches_begin != [] and code_matches_end != []:
        block_type = BlockType.CODE
    elif len(quote_matches) == len(to_analyze):
        block_type = BlockType.QUOTE
    elif len(uno_list_matches) == len(to_analyze):
        block_type = BlockType.UNORDERED
    elif len(ord_list_matches) == len(to_analyze):
        block_type = BlockType.ORDERED
    else:
        block_type = BlockType.PARA
    
    #print(len(ord_list_matches), len(to_analyze))
    #print(block_type)
    return block_type
#block_to_block_type(uno_list_trouble)

#heading works, code works, quote works, need unordered