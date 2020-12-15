from TypeAdvantages import *


def dual_type_stats(a, b):
    weak = {}
    strong = {}

    for i in range(len(a.adi_vector)):
        val = a.adi_vector[i] * b.adi_vector[i]
        if val > 1:
            weak[type_names[i]] = val
        elif val < 1:
            strong[type_names[i]] = val
    return weak, strong


def parse_type_input(type_entered):
    if type_entered in type_names:
        return [type_entered]
    elif ' ' in type_entered:
        types = type_entered.split(' ')
        for t in types:
            if t not in type_names:
                s = f"ERROR: invalid type '{t}'"
                print(s)
                return
        return types
    else:
        print(f"ERROR: invalid type '{type_entered}'")
        return


def parse_types(types):
    if types is None:
        return
    elif len(types) == 0:
        print("ERROR: no types given")
        return
    else:
        type_objs = []
        for t in types:
            type_objs.append(Type(t))
        return type_objs


def get_dual_type_string(maps):
    o_string = "  Weak against\n"
    for k, v in maps[0].items():
        o_string += "\t" + k + " x" + str(v) + " damage\n"
    o_string += "  Strong against\n"
    for k, v in maps[1].items():
        o_string += "\t" + k + " x" + str(v) + " damage\n"

    return o_string


def print_type_data(types):
    o_string = ""
    if types is None:
        return
    if len(types) == 2:
        o_string += "dual type detected\n"
        o_string += f"Type {types[0].name.upper()} {types[1].name.upper()}\n"
        maps = dual_type_stats(types[0], types[1])
        o_string += get_dual_type_string(maps)

    else:
        for t in types:
            o_string += t.string_summary()
    return o_string


def run(given_types):
    return print_type_data(parse_types(parse_type_input(given_types.lower())))