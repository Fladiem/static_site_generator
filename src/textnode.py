from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):      #This seems... not right?  Wrong, it's not wrong because it isn't wrong.
    TEXT = "TextType.TEXT"  
    BOLD = "TextType.BOLD"  #**
    ITALIC = "TextType.ITALIC"  #_
    CODE = "`TextType.CODE`" # `
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"
    

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TextType(TEXT_TYPE)
        self.url = URL

    
    def __eq__(textnode1, textnode2):
        if textnode1.text == textnode2.text and textnode1.text_type == textnode2.text_type and textnode1.url == textnode2.url:
            return True
        else:
            return False
    def __repr__(textnode):
        return f'TextNode({textnode.text}, {textnode.text_type.value}, {textnode.url})'

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.TEXT):
            return LeafNode(None, text_node.text)
        case(TextType.BOLD):
            return LeafNode("b", text_node.text)
        case(TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case(TextType.CODE):
            return LeafNode("code", text_node.text)
        case(TextType.LINK):
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case(TextType.IMAGE):
            return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})
            
normal_case = TextNode("text here", TextType.IMAGE, "https://gameinformer.com")
#print(text_node_to_html_node(normal_case))        
        
