import ply.lex as lex

filename = "Test.cs"
output_file = filename.split(".")[0] + ".md"

class_def_md = "## $CLASS$ : $BASE$\n### Namespace : $NAMESPACE$\n### DESCRIPTION\n$DESCRIPTION$\n"


ser_members_dict = {}
namespace = ""
class_values = []

def processs_class_input(t):
    el_arr = str(t.value).split(" ")
    ind = el_arr.index("class") + 1
    class_name = el_arr[ind]

    base_class = ""
    try:
        ind = el_arr.index(":") + 1
        base_class = el_arr[ind]
    except ValueError:
        pass
    
    class_description = "My Class"    
    return [class_name, base_class, class_description]

def process_namespace_input(t):
    return str(t.value).split(" ")[1]

def process_ser_members_input(t):
    var_code_snip = str(t.value)
    el_arr = var_code_snip.split(" ")
    var_name = el_arr[-1][0:-1]
    var_type = el_arr[-2]
    var_description = "Ser Member"

    ser_members_dict[var_name] = [var_description, var_code_snip, var_type]

def write_mdfile():
    pass

# Tokens
tokens = (
    'SERIALIZEDMEMBER',
    'BRACKETS',
    'NAMESPACE', 
    'CLASS', 

    # 'INHERITANCE',
    # 'MEMBERS', 
    # 'PROPERTIES', 
    # 'METHODS',
    # 'CHARACTERS'
    # 'CHARACTER'
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


def main():
    lexer = lex.lex()
    # open file
    
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
            process_ser_members_input(tok)
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


if __name__ == '__main__':
    main()