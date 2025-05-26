from textnode import *
from htmlnode import *
from static_to_public import *

def main():
    #root_dir = "."
    #print(os.listdir(root_dir))

    static_to_public("static", "public")
    
      
    return

main()


"""
    #print (TextNode("1", "Normal text", "3"))
    one = HTMLNode("Any", "value", "children", {
    "href": "https://www.google.com",
    "target": "_blank",
} )
    two = HTMLNode("two","value", "children")
    three = LeafNode("p", "Chazz it up!", {"The": "Chazz", "Oat": "Meal"})
    four = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
"""

#err = ParentNode(None, None)
    #noerr = ParentNode("p", [LeafNode("p", "Chazz it up!", {"The": "Chazz", "Oat": "Meal"})])
    #print(one.props_to_html())
    #print(two.props_to_html())
    #print(three.to_html())
    #print(four.to_html())
    #print (err.to_html())
    #print(noerr.to_html())