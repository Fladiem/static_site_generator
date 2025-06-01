import re
shmeebo = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
shmorblo = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\(([^\(\)]*)\)", text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\(([^\(\)]*)\)", text)
    return matches

#print(extract_markdown_images(shmeebo))
#print(extract_markdown_images(shmorblo))

#print(extract_markdown_links(shmorblo))
#print(extract_markdown_links(shmeebo))
header_ex ="""
# The Last Roaming Glacier

content

## The Tlingit Tribe's Traditional Woodworking
"""
header_ex_two = ""
def extract_title(markdown): #Extracts the first header from a markdown document
    try:
        matches = re.findall(r"(?<!#)#\s((.*?))\n", markdown)
        #print(matches)
        if matches == []:
            raise Exception("No header detected! Example: # header1")
        
        return matches[0][0].strip("# ")

    except Exception as e:
        print(f"{e}")
        return f"{e}"
    

    

#extract_title(header_ex_two)
   


#\!\[(.*?)\]\((http\w+://\w+\.\w+\.\w+\/\w+\W+\w+)       my poorly functioning novice solutions

#\[(.*?)\]\((https://\w+\.\w+\.\w+)    

#provided solutions

#!\[([^\[\]]*)\]\(([^\(\)]*)\)    images

#(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)     links