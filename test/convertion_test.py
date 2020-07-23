
import textwrap
from bs4 import BeautifulSoup as Bs
from unittest import TestCase 
from markdown import Markdown
from markdown_image_decorator import MarkdownImageDecorator

class ConvertionTest (TestCase):

  def test_link_only1 (self):
    md = Markdown(extensions=[MarkdownImageDecorator()])
    source = """
    ![](example.png)
    """
    mustbe = """
    <p>
    <a href="example.png" target="_blank">
    <img alt="" src="example.png">
    </a>
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )

  def test_link_only2 (self):
    md = Markdown(extensions=[MarkdownImageDecorator()])
    source = """
    ![alt](example.png)
    """
    mustbe = """
    <p>
    <a href="example.png" target="_blank">
    <img alt="alt" src="example.png">
    </a>
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )

  def test_link_only3 (self):
    md = Markdown(extensions=[MarkdownImageDecorator()])
    source = """
    ![alt](example.png "title")
    """
    mustbe = """
    <p>
    <a href="example.png" target="_blank">
    <img alt="alt" title="title" src="example.png">
    </a>
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )

  def test_figure1 (self):
    md = Markdown(extensions=[MarkdownImageDecorator(figuresrcs=("example.png",))])
    source = """
    ![](example.png)
    """
    mustbe = """
    <p>
    <a href="example.png" target="_blank">
    <figure>
    <img alt="" src="example.png">
    </figure>
    </a>
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )

  def test_figure2 (self):
    md = Markdown(extensions=[MarkdownImageDecorator(figuresrcs=("example.png",))])
    source = """
    ![alt](example.png)
    """
    mustbe = """
    <p>
    <a href="example.png" target="_blank">
    <figure>
    <img alt="alt" src="example.png">
    </figure>
    </a>
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )

  def test_figure3 (self):
    md = Markdown(extensions=[MarkdownImageDecorator(figuresrcs=("example.png",))])
    source = """
    ![alt](example.png "title")
    """
    mustbe = """
    <p>
    <a href="example.png" target="_blank">
    <figure>
    <img alt="alt" src="example.png">
    <figcaption>title</figcaption>
    </figure>
    </a>
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )
