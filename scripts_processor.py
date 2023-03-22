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


def process_methods_input(t):
    method_snip = str(t.value)[0:-1]
    el_arr = method_snip.split(" ")
    
    method_description = "My method"
    method_name = el_arr[2]

    method_name.replace(" ", "")

    try:
        ind = method_name.index("(")
        method_name = method_name[0:ind]
    except ValueError:
        pass

    return method_name, [method_description, method_snip] 

def process_ser_members_input(t):
    var_code_snip = str(t.value)
    el_arr = var_code_snip.split(" ")
    var_name = el_arr[-1][0:-1]
    var_type = el_arr[-2]
    var_description = "Ser Member"

    return (var_name, [var_description, var_code_snip, var_type])




