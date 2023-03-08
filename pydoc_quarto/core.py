# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['get_modules', 'gethelp', 'help2md', 'gen_md']

# %% ../nbs/00_core.ipynb 2
import pkgutil, pydoc, re
from importlib import import_module
from types import ModuleType
from pathlib import Path
from fastcore.script import call_parse
from fastcore.xtras import mk_write

# %% ../nbs/00_core.ipynb 3
def get_modules(lib:ModuleType) -> list[str]:
    "get a list of modules from a python package"
    modules = []
    for _, modname, _ in pkgutil.iter_modules(lib.__path__, lib.__name__ + '.'):
        if not modname.split('.')[-1].startswith('_'): modules.append(modname)
    return modules

# %% ../nbs/00_core.ipynb 8
def gethelp(modname:str)->str:
    "Get the help string for a module, when the module is a string."
    sym = __import__(modname, fromlist=[''])
    return pydoc.render_doc(sym, title='~~~~~~~~~~~~%s', renderer=pydoc.plaintext)

# %% ../nbs/00_core.ipynb 10
def help2md(helpstr):
    "Transform a help string for a module into Markdown."
    md = []
    section = None
    class_prefix = re.compile('^     \|  ')

    for l in helpstr.splitlines():
        if l.strip().startswith('~~~~~~~~~~~~'): continue

        if l and re.search('^\w', l): 
            section = l.strip().lower()
            if section not in ['name', 'data', 'file', 'version']: md.append(f'## {l.title()}')
            continue
        
        if section == 'description' and '[[quarto_pydoc:ignore]]' in l: return ''
        if section in ['file', 'data', 'version']: continue

        if l and re.search('^    \w', l):
            if section == 'name': md.append(f'# {l.strip()}')
            if section == 'functions': md.extend(['', f"### {l.split('(')[0].strip()}", '', f'<strong>{l.strip()}</strong>'])
            if section == 'classes': 
                if l.startswith('    class '): 
                    md.extend(['', f"### {l.replace('    class ', '').split('(')[0].strip()}", '', f'<strong>{l.strip()}</strong>', ''])
                else: md.append(l)
            continue

        else: md.append(l)
    return '\n'.join(md)

# %% ../nbs/00_core.ipynb 13
@call_parse
def gen_md(lib:str, # the name of the python library
           dest_dir:str # the destination directory the markdown files will be rendered into
          ) -> None:
    "Generate Markdown API docs"
    for modname in get_modules(import_module(lib)):  
        helpstr = gethelp(modname)
        md = help2md(helpstr)
        if md == '': continue
        submod = modname.split('.')[-1]
        (Path(dest_dir)/f'{submod}.md').mk_write(md)
