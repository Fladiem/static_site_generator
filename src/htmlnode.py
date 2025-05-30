
class HTMLNode:   #Primary purpose is to output HTML
    def __init__(self, tag=None, value=None, children=None, props=None):
        #tag: string representing HTML tag name
        #value: string representing the value of the HTML tag, the text inside a paragraph
        #children: A list of HTMLNode objects representing children of this node
        #props: A dictionary of key-value pairs representing attributes of the HTML tag.
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):   #Child classes should override this method to render themselves as HTML
        raise NotImplementedError  
    def props_to_html(self):
        if isinstance(self.props, dict):
                

            output = ''
            for content in self.props:
                output = output + f' {content}="{self.props[content]}"'
            return output
        if self.props == None:
            return
        else:
            raise ValueError('props must be dict or None')
            

            #output = output + ", " + amendment
            #count + 1
            #if count == 1:
                #return output
            #else:
                #amendment = f'{content}= {self.props[content]}'
        #return self.props_to_html()

    def __eq__(self, other):
        if not isinstance(other,HTMLNode):
            return False
        return (
        self.tag == other.tag and
        self.value == other.value and
        self.children == other.children and
        self.props == other.props
    )
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):   #Represents single HTML tag with no children
    def __init__(self, tag, value, props=None):    #Should not allow for children
        super().__init__(tag, value, None, props )  
                                                       
    def to_html(self):   #Return LeafNode as usable HTML   #Ch2 Section 4
        selfkey = ""
        output=""
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return f'{self.value}'
        #alteration made in ch 4-3 for markdown_to_html, deviates from course suggestion? START
        ####if self.props == None and (self.tag == "ul" or self.tag == "ol"):
            ####return f'<{self.tag}>{self.value}</{self.tag}>'
        if self.props == None and self.tag == "li":
            return f'  <{self.tag}>{self.value}</{self.tag}>\n'
        #alteration made in ch 4-3 for markdown_to_html, deviates from course suggestion? END
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        if self.props != None and self.tag == "img":  #another alteration Ch 4-3
            key_list = []
            for key in self.props:
                key_list.append(key)
            output = f'<{self.tag} {key_list[0]}="{self.props[key_list[0]]}" {key_list[1]}="{self.props[key_list[1]]}" />'
            return output

        else:
            for key in self.props:  #May need alterations to account for multiple dict entries !See logic for img tag above.
                selfkey = key    #see above solution for output in HTMLNode
                output = output + f'<{self.tag} {selfkey}="{self.props[selfkey]}">{self.value}</{self.tag}>'   #Ch2 Section 4

            return output#f'<{self.tag} {selfkey}="{self.props[selfkey]}">{self.value}</{self.tag}>' #old code returns last dict entry
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children , props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have tag argument")
        if self.children == None:
            raise ValueError("Parent node must have children argument")
        #alteration made in ch 4-3 for markdown_to_html, deviates from course suggestion START
        if self.tag == "ul" or self.tag == "ol":
            output = ''
            for child in self.children:   #lists represents (tag, value) of LeafNodes
                output += child.to_html() #f'<{lists.tag}>{lists.value}</{lists.tag}>' 
            
            
            return f'<{self.tag}>\n{output}</{self.tag}>'

        #alteration made in ch 4-3 for markdown_to_html, deviates from course suggestion END
        else:
            
            output = ''
            for child in self.children:   #lists represents (tag, value) of LeafNodes
                output += child.to_html() #f'<{lists.tag}>{lists.value}</{lists.tag}>' 
            
            
            return f'<{self.tag}>{output}</{self.tag}>'
            
                


