# MkDocs Bootstrap Elements Plugin

This plugin enhances your MkDocs site with Bootstrap elements, allowing you to easily add accordions, modals, and cards using simple Markdown syntax.

## Features

- Accordion support
- Modal support
- Card support
- Easy-to-use Markdown syntax
- Customizable styles

## Installation

Install the plugin using pip:

```bash
pip install mkdocs-bootstrap-elements-plugin
```

## Usage

1. Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - bootstrap_elements
```

2. Use the custom syntax in your Markdown files:

### Accordion

```markdown
:::accordion Accordion Title
Accordion content goes here.
:::
```

### Modal

```markdown
:::modal Modal Title
Modal content goes here.
:::
```

### Card

```markdown
:::card Card Title
Card content goes here.
:::
```

## Customization

You can customize the appearance of the Bootstrap elements by overriding the default CSS. Create a custom CSS file and add it to your `mkdocs.yml`:

```yaml
extra_css:
  - css/custom.css
```
