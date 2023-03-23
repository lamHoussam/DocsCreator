def processs_class_input(t):
    el_arr = str(t.value).split(" ")
    ind = el_arr.index("class") + 1

    is_abstract = "abstract" in el_arr
    
    class_name = el_arr[ind]

    base_class = ""
    try:
        ind = el_arr.index(":") + 1
        base_class = el_arr[ind]
    except ValueError:
        pass
    
    class_description = "My Abstract class" if is_abstract else "My Class"
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

    return method_name, [method_description, method_snip+";"] 

def process_ser_members_input(t):
    var_code_snip = str(t.value)
    # el_arr = var_code_snip.split(" ")

    # return (var_name, [var_description, var_code_snip, var_type])

    el_sides = var_code_snip.split(",")
    el_arr = el_sides[0].split(" ")
    var_type = el_arr[-2]
    var_description = "Ser Member"
    var_name = el_arr[-1].replace(";", "")

    var_code_snip = "[SerializeField] private " + var_type

    vars = [(var_name, [var_description, var_code_snip + " " + var_name + ";", var_type])]
    for i in range(1, len(el_sides)):
        el = el_sides[i].replace(" ", "").replace(";", "")
        vars.append((el, [var_description, var_code_snip + " " + el + ";", var_type]))

    return vars


def process_public_members_input(t):
    var_code_snip = str(t.value)

    el_sides = var_code_snip.split(",")
    el_arr = el_sides[0].split(" ")
    var_type = el_arr[-2]
    var_description = "Public Member"
    var_name = el_arr[-1].replace(";", "")

    var_code_snip = "public " + var_type

    vars = [(var_name, [var_description, var_code_snip + " " + var_name + ";", var_type])]
    for i in range(1, len(el_sides)):
        el = el_sides[i].replace(" ", "").replace(";", "")
        vars.append((el, [var_description, var_code_snip + " " + el + ";", var_type]))

    return vars


def process_property_input(t):
    prop_snip = str(t.value)
    el_sides = prop_snip.split("{")
    el_arr = el_sides[0].split(" ")
    prop_accessors = " {" + el_sides[1]


    prop_name = el_arr[0]

    prop_description = "My Property"
    prop_type_ind = 0
    for i in range(len(el_arr)):
        el = el_arr[i]
        if el != "" and el != " ":
            prop_name = el
            prop_type_ind = i-1
    
    prop_type = el_arr[prop_type_ind]

    final_prop_snip = "public " + str(prop_type) + " " + prop_name + prop_accessors

    return prop_name, [prop_description, final_prop_snip, prop_type]

def process_get_property(t):
    prop_snip = str(t.value)
    el_sides = prop_snip.split("=>")
    el_arr = el_sides[0].split(" ")
    prop_name = el_arr[0]

    prop_description = "My Get Property"
    prop_type_ind = 0
    for i in range(len(el_arr)):
        el = el_arr[i]
        if el != "" and el != " ":
            prop_name = el
            prop_type_ind = i-1
    
    prop_type = el_arr[prop_type_ind]

    final_prop_snip = "public " + str(prop_type) + " " + prop_name + " { get; }"

    return prop_name, [prop_description, final_prop_snip, prop_type]