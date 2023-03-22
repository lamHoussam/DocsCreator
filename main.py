import ply.lex as lex

filename = "TestFile.cs"
output_file = filename.split(".")[0] + ".md"


ser_members_dict = {}


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
    t.value = str(t.value).split(" ")[1]
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
        # print(tok.type, tok.value, tok.lineno, tok.lexpos)

    print(ser_members_dict)



if __name__ == '__main__':
    main()