
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree import ElementTree as etree

class MarkdownImageDecorator (Extension):

  def __init__ (self, *, figuresrcs=[]):

    """
    this is a constructor.
    parameter of `figuresrcs` is iterable object that contain URL.
    this class, it will reformed structure with `decorate_as_linked_figured_image` what is contained in `figuresrcs`.
    """

    super().__init__()
    self.figuresrcs = set(figuresrcs)

  def extendMarkdown (self, md):
    md.treeprocessors["image_decorator"] = ImageDecorator(
      figuresrcs=self.figuresrcs
    )

class ImageDecorator (Treeprocessor):

  """
  this treeprocessor decorate <img> tag with <a> and <figure> tag if necessary.
  """

  def __init__ (self, *, figuresrcs=[]):

    """
    this is a constructor.
    parameter of `figuresrcs` is iterable object that contain URL.
    this class, it will reformed structure with `decorate_as_linked_figured_image` what is contained in `figuresrcs`.
    """

    super().__init__()
    self.figuresrcs = set(figuresrcs)

  def search_parent (self, element, root):

    """
    find parent node of element.
    this function return position of element in parent node, and parent node.
    """

    dictionary = dict()
    for p in root.iter():
      for index, ele in enumerate(p.findall("./*")):
        dictionary[ele] = index, p 
    return dictionary[element]

  def iter_exclude_element (self, root):

    """
    list child nodes that are in <a> and <figure> tag.
    """

    for link in root.findall(".//a"):
      yield from link.iter()
    for figure in root.findall(".//figure"):
      yield from figure.iter()

  def search_single_image (self, root):

    """
    search <img> tags that are not contained by <a> and <figure> tag.
    """

    excludes = set(self.iter_exclude_element(root))
    for img in root.findall(".//img"):
      if img not in excludes:
        yield img 

  def decorate_as_linked_image (self, image, root):

    """
    convert <img> tag to <a href=""><img title="" alt="" src=""></a> like structure.
    """

    index, parent = self.search_parent(image, root)
    parent.remove(image)
    link = etree.Element("a")
    link.set("href", image.get("src", ""))
    link.set("target", "_blank")
    link.insert(-1, image)
    parent.insert(index, link)

  def decorate_as_linked_figured_image (self, image, root):

    """
    convert <img> tag to <a href=""><figure><img alt="" src=""><figcaption></figcaption></figure></a> like structure.
    """

    index, parent = self.search_parent(image, root)
    parent.remove(image)
    link = etree.Element("a")
    link.set("href", image.get("src", ""))
    link.set("target", "_blank")
    figure = etree.Element("figure")
    figcaption = None 
    if "title" in image.attrib:
      figcaption = etree.Element("figcaption")
      figcaption.text = image.attrib["title"]
      del image.attrib["title"]
    link.insert(0, figure)
    if figcaption is not None:
      figure.insert(0, figcaption)
    figure.insert(0, image)
    parent.insert(index, link)

  def decorate_image (self, image, root):

    """
    convert <img> tag to proper structure.
    """

    if image.get("src", "") in self.figuresrcs:
      self.decorate_as_linked_figured_image(image, root)
    else:
      self.decorate_as_linked_image(image, root)

  def run (self, root):
    for image in self.search_single_image(root):
      self.decorate_image(image, root)
