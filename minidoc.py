from xml.dom import minidom


def _elem_inplace_addition(self,other):
    self.appendChild(other)
    return self

def _elem_textnode(self,text):
    textnode = self.ownerDocument.createTextNode(text)
    self.appendChild(textnode)
    return self

def _elem_set_attributes_from_tuple(self,*args):
    for k,v in args:
        self.setAttribute(k,str(v))
    return self

def _elem_set_attributes_from_kwargs(self,**kwargs):
    for k,v in kwargs.items():
        self.setAttribute(k,str(v))
    return self

def _elem_cdata_section(self,data):
    cdatanode = self.ownerDocument.createCDATASection(data)
    self.appendChild(cdatanode)
    return self

minidom.Element.__iadd__ = _elem_inplace_addition
minidom.Element.txt = _elem_textnode
minidom.Element.attrs = _elem_set_attributes_from_kwargs
minidom.Element.attrt = _elem_set_attributes_from_tuple
minidom.Element.cdata = _elem_cdata_section
minidom.Element.__str__ = lambda s:s.toprettyxml().strip()

doc = minidom.Document()

elem = doc.createElement
