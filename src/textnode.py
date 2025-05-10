from enum import Enum

class TextType(Enum):      #This seems... not right?
    NORMAL_TEXT = "Normal text"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"
    

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

        
        
