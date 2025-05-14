import re
shmeebo = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
shmorblo = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\(([^\(\)]*)\)", text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\(([^\(\)]*)\)", text)
    return matches
   
print(extract_markdown_images(shmeebo))

print(extract_markdown_links(shmorblo))

#\!\[(.*?)\]\((http\w+://\w+\.\w+\.\w+\/\w+\W+\w+)       my poorly functioning novice solutions

#\[(.*?)\]\((https://\w+\.\w+\.\w+)    

#provided solutions

#!\[([^\[\]]*)\]\(([^\(\)]*)\)    images

#(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)     links