import ply.lex as lex
from scripts_processor import *

# Tokens
tokens = (
    'SERIALIZEDMEMBER',
    'BRACKETS',
    'NAMESPACE', 
    'CLASS', 

    # 'MEMBERS', 
    # 'PROPERTIES', 
    # 'METHODS',
)

# Regex
# t_CHARACTER = r'[a-z]'
def t_SERIALIZEDMEMBER(t):
    r'\[SerializeField\s*(?:,\s*[a-zA-Z0-9_]+\s*=\s*[^\]]+)?\]\s*(private\s+)?(\w+)\s+(\w+)\s*;'
    return t

t_BRACKETS = "[{}]"

def t_NAMESPACE(t):
    r'^namespace\s+([^\s{]+)'
    return t


def t_CLASS(t):
    r'\s*(public|private|internal|protected)?\s*(sealed|partial)?\s*class\s+([^\s{{}}]+)(?:\s*:\s*([^\s{{}}]+))?'
    # do stuff to extract name base and interfaces
    return t


# Ignore
t_ignore = ' \t\n\r'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



def generate_md_file(filename, lexer):

    ser_members_dict = {}
    class_values = []
    namespace = ""


    output_file = str(filename).split(".")[0] + ".md"
    file = open(filename, "r")
    data = file.read()
    
    lexer.input(data)
    file.close()

        # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input

        if (tok.type == 'SERIALIZEDMEMBER'):
            key, val = process_ser_members_input(tok)
            ser_members_dict[key] = val
        elif (tok.type == 'CLASS'):
            class_values = processs_class_input(tok)
        elif (tok.type == 'NAMESPACE'):
            namespace = process_namespace_input(tok)
        
        
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)
    print("Class values : " + str(class_values))
    print("Namespace : " + namespace)
    print(ser_members_dict)

    with open(output_file, "w") as f:
        class_def_md = f"## {class_values[0]} : {class_values[1]}\n### Namespace : {namespace}\n### DESCRIPTION\n{class_values[2]}\n"
        f.write(class_def_md)
        class_def_md = f'### Properties\n'
        for var_name, var in ser_members_dict.items():
            class_def_md += f'`{var_name}` ({var[2]})\n\n{var[0]}\n```csharp\n{var[1]}\n```\n'

        f.write(class_def_md)


def main():
    lexer = lex.lex()
    # Get C# files and generate respective mds
    generate_md_file("Test.cs", lexer)

if __name__ == '__main__':
    main()