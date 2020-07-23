
# Markdown Image Decorator

![](https://img.shields.io/badge/Python-3.7-blue?style=flat)
![](https://img.shields.io/badge/License-MIT-green?style=flat)

このパッケージははマークダウンのライブラリである [markdown](https://python-markdown.github.io/) に拡張機能を提供します。

この拡張機能は画像表示のマークダウンを `<a>` `<figure>` `<figcaption>` `<img>` を用いた HTML 構造に変換します。
この拡張機能を使用することで、よりユーザや SEO に配慮した画像表示を行うことができます。
また引数を指定することにより、画像ごとに `<figure>` タグの使用の有無も設定することができます。

## Usage

```python
import markdown
from markdown_image_decorator import MarkdownImageDecorator

md1 = markdown.Markdown(extensions=[MarkdownImageDecorator()])
md2 = markdown.Markdown(extensions=[MarkdownImageDecorator(figuresrcs=["use-figure.jpg"])])
```

```markdown
![](picture.jpg)
![alt text](picture.jpg)
![alt text](picture.jpg "title text")
![alt text](use-figure.jpg "title text")
```

```html
<p>
  <a href="picture.jpg">
    <img src="picture.jpg">
  </a>
  <a href="picture.jpg">
    <img src="picture.jpg" alt="alt text">
  </a>
  <a href="picture.jpg">
    <img src="picture.jpg" alt="alt text" title="title text">
  </a>
  <a href="use-figure.jpg">
    <figure>
      <img src="use-figure.jpg" alt="alt text">
      <figcaption>title text</figcaption>
    </figure>
  </a>
</p>
```

## Installation

```shell
python setup.py install
```

```shell
python setup.py test
```

```shell
python -m pip uninstall markdown_image_decorator
```

## License

&copy; tikubonn 2020<br>
Markdown Image Expander released under [MIT License](LICENSE).<br>
[markdown](https://python-markdown.github.io/) released under [BSD License](LICENSE).
