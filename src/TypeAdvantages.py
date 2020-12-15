type_names = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying",
              "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

advantage_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 1],
    [1, .5, .5, 1, 2, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1],
    [1, 2, .5, 1, .5, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1],
    [1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1],
    [1, .5, 2, 1, .5, 1, 1, .5, 2, .5, 1, .5, 2, 1, .5, 1, .5, 1],
    [1, .5, .5, 1, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, .5, 1],
    [2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, .5],
    [1, 1, 1, 1, 2, 1, 1, .5, .5, 1, 1, 1, .5, .5, 1, 1, 0, 2],
    [1, 2, 1, 2, .5, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, .5, 2, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1],
    [1, .5, 1, 1, 2, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, .5],
    [1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0],
    [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, .5],
    [1, .5, .5, .5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2],
    [1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1]
]


def set_adi_vector(type_class):
    vector = []
    for i in range(len(advantage_matrix)):
        vector.append(advantage_matrix[i][type_names.index(type_class.name)])
    type_class.adi_vector = vector


def set_disadvantages(type_class):
    i = type_names.index(type_class.name)
    for j in range(len(advantage_matrix[i])):
        if advantage_matrix[i][j] == .5:
            type_class.disadvantages[type_names[j]] = (advantage_matrix[i][j], advantage_matrix[j][i])
        if advantage_matrix[j][i] == 2:
            type_class.disadvantages[type_names[j]] = (advantage_matrix[i][j], advantage_matrix[j][i])
        if advantage_matrix[i][j] == 2:
            type_class.advantages[type_names[j]] = (advantage_matrix[i][j], advantage_matrix[j][i])
        # immune to attack type
        if advantage_matrix[j][i] == 0:
            type_class.immunities[type_names[j]] = (advantage_matrix[j][i], advantage_matrix[i][j])
        if advantage_matrix[i][j] == 0:
            type_class.disadvantages[type_names[j]] = (advantage_matrix[i][j], advantage_matrix[j][i])


def check_type_name(name):
    return name in type_names


class Type:
    def __init__(self, name):
        self.adi_vector = []
        self.advantages = {}
        self.disadvantages = {}
        self.immunities = {}
        name = name.lower()
        if check_type_name(name):
            self.name = name
            set_adi_vector(self)
            set_disadvantages(self)
        else:
            self.name = "no Name"

    def print_summary(self):
        print("Type", self.name)
        print("\tImmunities: ")
        for k in self.immunities.keys():
            print('\t  ', k)
        print("\tAdvantages: ")
        for k, v in self.advantages.items():
            print('\t  ', k, 'SE: ' + str(v[0]) + 'x RCV: ' + str(v[1]) + 'x')
        print("\tDisadvantages: ")
        for k, v in self.disadvantages.items():
            print('\t  ', k, 'GVN: ' + str(v[0]) + 'x RCV: ' + str(v[1]) + 'x')

    def string_summary(self):
        o_string = f"Type {self.name.upper()}\n"
        o_string += "\tImmunities: \n"
        for k in self.immunities.keys():
            o_string += f'\t  {k}\n'
        o_string += "\tAdvantages: \n"
        for k, v in self.advantages.items():
            o_string += '\t  ' + k + ' SE: ' + str(v[0]) + 'x RCV: ' + str(v[1]) + 'x\n'
        o_string += "\tDisadvantages: \n"
        for k, v in self.disadvantages.items():
            o_string += '\t  ' + k + ' GVN: ' + str(v[0]) + 'x RCV: ' + str(v[1]) + 'x\n'
        o_string += '\n'

        return o_string
