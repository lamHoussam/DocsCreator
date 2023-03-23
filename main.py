import ply.lex as lex
from scripts_processor import *

from os import makedirs, path
from glob import glob
import sys

folder_name = "API"

# Tokens
tokens = (
    'BRACKETS',
    'NAMESPACE', 
    'CLASS', 
    'PROPERTY',
    'GETPROPERTY', # public Test Value => value;
    'SERIALIZEDMEMBER',
    'MEMBERS', 
    'METHODS',
)
# r'\s*(public\s+)(\w+)\s+(\w+)\s*;'
# Regex
# t_CHARACTER = r'[a-z]'
def t_SERIALIZEDMEMBER(t):
    r'\[SerializeField\s*(?:,\s*[a-zA-Z0-9_]+\s*=\s*[^\]]+)?\]\s*(private\s+)?(\w+)\s+(\w+)(\s*,\s*\w+)*\s*;'
    return t

def t_MEMBERS(t):
    r'\s*(public\s+)(\w+)\s+(\w+)(\s*,\s*\w+)*\s*;'

    return t

def t_PROPERTY(t):
    r'\s*(public\s+)(static\s+)?(readonly\s+)?(?!class)(\s+\w+\s+)?(\w+)\s+(\w+)\s*{[^}]*}'
    return t

def t_GETPROPERTY(t):
    r'public\s+\w+\s+\w+\s+=>\s+\w+;'
    return t

t_BRACKETS = "[{}]"

def t_NAMESPACE(t):
    r'^namespace\s+([^\s{]+)'
    return t

def t_METHODS(t):
    r'\bpublic\s+\w+\s+\w+\s*\([^)]*\)\s*{'
    return t

def t_CLASS(t):
    r'\s*(public|private|internal|protected)?\s*(sealed|partial|abstract)?\s*class\s+([^\s{}]+)(?:\s*:\s*([^\s{}]+))?'
    # do stuff to extract name base and interfaces
    return t


# Ignore
t_ignore = ' \t\n\r'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



def generate_md_file(file_path, lexer):
    members_dict = {}
    properties_dict = {}
    class_values = []
    namespace = ""
    methods_dict = {}

    filename = path.basename(file_path)

    output_file = path.join(folder_name, str(filename).split(".")[0] + ".md")
    file = open(file_path, "r")
    data = file.read()
    
    lexer.input(data)
    file.close()

        # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input

        if (tok.type == 'SERIALIZEDMEMBER'):
            arr = process_ser_members_input(tok)
            for key, val in arr:
                members_dict[key] = val            
        elif(tok.type == 'MEMBERS'):
            arr = process_public_members_input(tok)
            for key, val in arr:
                members_dict[key] = val
        elif (tok.type == 'PROPERTY'):
            key, val = process_property_input(tok)
            properties_dict[key] = val
        elif tok.type == 'GETPROPERTY':
            key, val = process_get_property(tok)
            properties_dict[key] = val
        elif (tok.type == 'CLASS'):
            class_values = processs_class_input(tok)
        elif (tok.type == 'NAMESPACE'):
            namespace = process_namespace_input(tok)
        elif (tok.type == 'METHODS'):
            key, val = process_methods_input(tok)
            methods_dict[key] = val
        
        
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)
    print("Class values : " + str(class_values))
    print("Namespace : " + namespace)
    print(members_dict)
    print(properties_dict)
    print(methods_dict)

    with open(output_file, "w") as f:
        # Class definition
        class_def_md = f"# {class_values[0]} : {class_values[1]}\n## Namespace : {namespace}\n## DESCRIPTION\n{class_values[2]}\n"
        f.write(class_def_md)
        
        # Members definition
        class_def_md = f'## Members\n'
        for var_name, var in members_dict.items():
            class_def_md += f'`{var_name}` ({var[2]})\n\n{var[0]}\n```csharp\n{var[1]}\n```\n'

        f.write(class_def_md)

        # Properties definition
        class_def_md = f'## Properties\n'
        for var_name, var in properties_dict.items():
            class_def_md += f'`{var_name}` ({var[2]})\n\n{var[0]}\n```csharp\n{var[1]}\n```\n'

        f.write(class_def_md)

        # Methods definition
        class_def_md = f'## Methods\n'
        for meth_name, meth in methods_dict.items():
            class_def_md += f'`{meth_name}`\n\n{meth[0]}\n```csharp\n{meth[1]}\n```\n'

        f.write(class_def_md)

def usage():
    print("Usage : \npython main.py [--options] <project_path>")


def main():
    lexer = lex.lex()

    project_path = "./"
    recursive = False
    
    # print(sys.argv)
    if len(sys.argv) == 2:
        project_path = sys.argv[1]
        if not path.exists(project_path):
            usage()
            exit(1)
    elif len(sys.argv) >= 3:
        if sys.argv[1] == "--recursive":
            recursive = True
        project_path = sys.argv[2]
        if not path.exists(project_path):
            usage()
            exit(1)
    
    directory = folder_name

    if not path.exists(directory):
        makedirs(directory)

    # Get C# files and generate respective md files
    # TODO: Fix rec
    project_path = path.join(project_path, "*.cs")
    cs_files = glob(project_path, recursive=recursive)
    
    print(project_path)
    print(cs_files)
    for file in cs_files:
        print(path.basename(file))
        generate_md_file(file, lexer)



if __name__ == '__main__':
    main()