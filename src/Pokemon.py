class Pokemon:
    QUESTION_LINK = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Question_mark_alternate.svg/1200px-Question_mark_alternate.svg.png"

    def __init__(self, name="Unassigned Name", dex_id=0, typing=None, bs_total=0, hp=0, attack=0, defense=0,
                 sp_attack=0,
                 sp_defense=0, speed=0,
                 sprite_full=QUESTION_LINK,
                 sprite_shiny=QUESTION_LINK,
                 sprite_icon=QUESTION_LINK,
                 is_alternate_form=False, evolution_tree=None):
        if typing is None:
            typing = []
        self.typing = typing
        self.name = name
        self.dex_id = dex_id
        self.bs_total = bs_total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.sprite_icon = sprite_icon
        self.sprite_full = sprite_full
        self.sprite_shiny = sprite_shiny
        self.is_alternate_form = is_alternate_form
        self.evolution_tree = evolution_tree

    def print_summary(self):
        print("Name: ", self.name)
        print("Typing: ", self.typing)
        print("Dex ID: ", self.dex_id)
        print("HP: ", self.hp)
        print("ATK: ", self.attack)
        print("DEF: ", self.defense)
        print("SP ATK: ", self.sp_attack)
        print("SP DEF: ", self.sp_defense)
        print("Speed: ", self.speed)
        print("Total: ", self.bs_total)

    def string_summary(self):
        return self.sprite_full + " " + self.sprite_shiny + "\nName: " + self.name + "\nTyping: " + str(
            self.typing) + "\nDex ID: " + str(
            self.dex_id) + "\nHP: " + str(self.hp) + "\nATK: " + str(self.attack) + "\nDEF: " + str(
            self.defense) + "\nSP ATK: " + str(self.sp_attack) + "\nSP DEF: " + str(
            self.sp_defense) + "\nSpeed: " + str(self.speed) + "\nTotal: " + str(self.bs_total)


def get_type(self):
    return self.typing


def get_name(self):
    return self.name


def get_dex_id(self):
    return self.dex_id


def get_bs_total(self):
    return self.bs_total


def get_hp(self):
    return self.hp


def get_attack(self):
    return self.attack


def get_defense(self):
    return self.defense


def get_sp_attack(self):
    return self.sp_attack


def get_sp_defense(self):
    return self.sp_defense


def get_speed(self):
    return self.speed


def get_icon(self):
    return self.sprite_icon


def get_sprite(self):
    return self.sprite_full


def get_shiny(self):
    return self.sprite_shiny


def is_alternate_form(self):
    return self.is_alternate_form


def get_evolution_tree(self):
    return self.evolution_tree
