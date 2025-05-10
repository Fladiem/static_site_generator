import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
nodule = HTMLNode(("oat", "oat","boat", {'goose: beef'}))
noduledos = HTMLNode(("oat", "oat","boat", {'goose: beef'}))

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = HTMLNode("bart", "liscense", "plate", "bort")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_var_eq(self):
        node = ("bart", "liscense", "plate", {"bort": "cowabummer"})
        node2 = ("bart", "liscense", "plate", {"bort": "cowabummer"})
        self.assertEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self): #Tests if leaf_to_html works properly
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self): #Tests if leaf_to_html works properly with props != None
        node = LeafNode('a', 'Click here', {'href': 'https://www.gameinformer.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.gameinformer.com">Click here</a>')

    def test_LeafNode_noteq_(self):  #Tests if LeafNodes are not equal
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, wherld!", None)
        self.assertNotEqual(node, node2)

class TestParentNode(unittest.TestCase):
    def test_eq_ParentNode(self):
        node = ParentNode("p", [LeafNode("p", "Chazz it up!", {"The": "Chazz", "Oat": "Meal"})])
        node2 = ParentNode("p", [LeafNode("p", "Chazz it up!", {"The": "Chazz", "Oat": "Meal"})])
        self.assertEqual(node, node2)
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_great_grandchildren(self):
        greatchild_node = LeafNode("b", "greatchild")
        grandchild_node = ParentNode("p", [greatchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><p><b>greatchild</b></p></span></div>",
        )
    def test_to_html_errors(self):
        node = ParentNode(None, "spinach")
        node2 = ParentNode("p", None)
        self.assertNotEqual(node.to_html, node2.to_html)
    def test_ParentNode_without_child(self):
        #self.assertEqual does not work here because Errors do not return the error as a value.
        node = ParentNode("p", None)
        
        with self.assertRaises(ValueError) as context:  #asserts that an error is being raised, context becomes ValueError string
            node.to_html()  #specifies the function an Error is expected from
        
        self.assertTrue("Parent node must have children argument" in str(context.exception))
        #checks node.to_html() against "Parent node must have child argument"

if __name__ == "__main__":
    unittest.main()