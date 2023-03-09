# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['get_modules', 'MarkdownDoc', 'render_quarto_md', 'gethelp', 'write_md', 'gen_md']

# %% ../nbs/00_core.ipynb 2
import pkgutil, re, inspect
from importlib import import_module
from pydoc import TextDoc, resolve, describe
from types import ModuleType
from pathlib import Path
from fastcore.script import call_parse
from fastcore.xtras import mk_write

# %% ../nbs/00_core.ipynb 3
def get_modules(lib:ModuleType):
    "get a list of modules from a python package"
    modules = []
    for _, modname, _ in pkgutil.iter_modules(lib.__path__, lib.__name__ + '.'):
        if not modname.split('.')[-1].startswith('_'): modules.append(modname)
    return modules

# %% ../nbs/00_core.ipynb 8
class MarkdownDoc(TextDoc):
    _skip_titles = ['file', 'data', 'version', 'author', 'credits', 'name']
    def _get_class_nm(text): return 

    def _bold_first_line(self, text):
        lines = text.splitlines()
        html_escape = "\n```{=html}\n"
        if lines: lines[0] = f'<br>{html_escape}<blockquote><strong><code>{lines[0].strip()}</code></strong></blockquote>\n```\n<br>\n'
        return '\n'.join(lines)
    
    def title_format(self, text): return f'## {text.title()}\n'
    
    def bold(self, text): return text

    def indent(self, text, prefix='    '):
        """Indent text by prepending a given prefix to each line."""
        if not text: return ''
    
        lines = []
        for line in text.split('\n'):
            sline = line.strip()

            if  sline == '<br>': lines.append('\n')
            elif sline.startswith('###') or sline.startswith('<blockquote>') or sline.startswith("```"):
                lines.append(sline)
            else: 
                lines.append(prefix + line)
                
        if lines: lines[-1] = lines[-1].rstrip()
        return '\n'.join(lines)

    
    def document(self, object, name=None, *args):
        """
        Generate documentation for an object.
        
        This method overrides pydoc.Doc.document in the standard library
        """
        args = (object, name) + args
        try:
            if inspect.ismodule(object): return self.docmodule(*args)
            elif inspect.isclass(object): return f'\n### {name.strip()}\n\n' + self._bold_first_line(self.docclass(*args))
            elif inspect.ismethod(object) or '.' in object.__qualname__: return  f'\n#### `{object.__qualname__}`\n\n' + self.docroutine(*args)
            elif inspect.isroutine(object) and '.' not in object.__qualname__: return f'\n### `{name.strip()}`\n\n' + self._bold_first_line(self.docroutine(*args))
        except AttributeError:
            pass
        if inspect.isdatadescriptor(object): return self.docdata(*args)
        return self.docother(*args)

        
    def section(self, title, contents):
        if title.lower() in self._skip_titles: return ''
        clean_contents = self.indent(contents).rstrip()
        return self.title_format(title) + '\n' + clean_contents + '\n\n'

# %% ../nbs/00_core.ipynb 9
def render_quarto_md(thing, title=None, forceload=0):
    """Render text documentation, given an object or a path to an object."""
    renderer = MarkdownDoc()
    object, name = resolve(thing, forceload)
    desc = describe(object)
    module = inspect.getmodule(object)
    if name and '.' in name:
        desc += ' in ' + name[:name.rfind('.')]
    elif module and module is not object:
        desc += ' in module ' + module.__name__

    if not (inspect.ismodule(object) or
              inpsect.isclass(object) or
              inspect.isroutine(object) or
              inspect.isdatadescriptor(object) or
              _getdoc(object)):
        # If the passed object is a piece of data or an instance,
        # document its available methods instead of its value.
        if hasattr(object, '__origin__'):
            object = object.__origin__
        else:
            object = type(object)
            desc += ' object'
    
    doc_title = title if title else name
    desc_top = ' '.join(desc.splitlines()[:2])
    frontmatter=f'---\ntitle: "{doc_title}"\ndescription: "{desc_top}"\n---\n\n'
    return frontmatter + renderer.document(object, name)

# %% ../nbs/00_core.ipynb 10
def gethelp(modname:str, title:str=None)->str:
    "Get the help string for a module in a markdown format."
    sym = __import__(modname, fromlist=[''])
    return render_quarto_md(sym, title=title)

# %% ../nbs/00_core.ipynb 15
def write_md(modname, dest_dir):
    "Write markdown to file"
    submod = modname.split('.')[-1]
    md = gethelp(modname=modname, title=submod)
    (Path(dest_dir)/f'{submod}.qmd').mk_write(md)

@call_parse
def gen_md(lib:str, # the name or module of the python library, if module should be in the form `library.module`
           dest_dir:str # the destination directory the markdown files will be rendered into
          ) -> None:
    "Generate Quarto Markdown API docs"
    if '.' in lib: write_md(modname=lib, dest_dir=dest_dir)
    else:
        for modname in get_modules(import_module(lib)): write_md(modname=modname, dest_dir=dest_dir)
