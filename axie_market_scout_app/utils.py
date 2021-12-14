import base64
from io import BytesIO

## my imports ##
import matplotlib
from .file_handler import *
from datetime import datetime
import matplotlib as mpl
from matplotlib import pyplot as plt

def get_graph():
    buffer = BytesIO()
    #plt.figure(figsize=(8, 5))
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):

    """plt.switch_backend('AGG')
    plt.title('sales of items')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph"""

### Classes ###

beast_eye_parts = ['Calico Zeal', 'Chubby', 'Little Peas', 'Puppy', 'Snowflakes', 'Zeal']
bug_eye_parts = ['Bookworm', 'Broken Bookworm', 'Kotaro?', 'Neo', 'Nerdy']
bird_eye_parts = ['Icy Gaze', 'Little Owl', 'Lucas', 'Mavis', 'Robin', 'Sky Mavis']
plant_eye_parts = ['Blossom', 'Confused', 'Cucumber Slice', 'Dreamy Papi', 'Papi']
aquatic_eye_parts = ['Clear', 'Gero', 'Insomnia', 'Sleepless', 'Telescope', 'Yen']
reptile_eye_parts = ['Crimson Gecko', 'Dokuganryu', 'Gecko', 'Kabuki', 'Scar', 'Topaz', 'Tricky']

beast_ear_parts = ['Belieber', 'Innocent Lamb', 'Merry Lamb', 'Nut Cracker', 'Nyan', 'Point Nyan', 'Puppy', 'Zen']
bug_ear_parts = ['Beetle Spike', 'Ear Breathing', 'Earwing', 'Larva', 'Leaf Bug', 'Mon', 'Tassels', 'Vector']
bird_ear_parts = ['Curly', 'Early Bird', 'Hearth Cheek', 'Karimata', 'Owl', 'Peace Maker', 'Pink Cheek', 'Risly Bird']
plant_ear_parts = ['Clover', 'Hollow', 'Leafy', 'Lotus', 'Maiako', 'Pinecones', 'Rosa', 'Sakura', 'The Last Leaf']
aquatic_ear_parts = ['Bubblemaker', 'Gill', 'Inkling', 'Nimo', 'Red Nimo', 'Seaslug', 'Tiny Fan']
reptile_ear_parts = ['Curved Spine', 'Deadly Pogona', 'Friezard', 'Pogona', 'Sidebarb', 'Small Frill', 'Swirl']

beast_back_parts = ['Furball', 'Hamaya', 'Hasagi', 'Hero', 'Jaguar', 'Risky Beast', 'Ronin', 'Timber']
bug_back_parts = ['Buzz Buzz', 'Candy Canes', 'Garish Worm', 'Sandal', 'Scarab', 'Snail Shell', 'Spiky Wing', 'Starry Shell']
bird_back_parts = ['Balloon', 'Cupid', 'Kingfisher', 'Origami', 'Pigeon Post', 'Raven', 'Starry Ballon', 'Tri Feather']
plant_back_parts = ['Bidens', 'Mint', 'Pink Turnip', 'Pumpkin', 'Shiitake', 'Turnip', 'Watering Can', 'Yakitori']
aquatic_back_parts = ['Anemone', 'Blue Moon', 'Crystal Hermit', 'Goldfish', 'Hermit', 'Perch', 'Sponge']
reptile_back_parts = ['1ND14N-5T4R', 'Bone Sail', 'Croc', 'Frozen Bucket', 'Green Thorns', 'Indian Star', 'Red Ear', 'Rugged Sail', 'Tri Spikes']

beast_mouth_parts = ['Axies Kiss', 'Confident', 'Goda', 'Nut Cracker', 'Skull Cracker']
bug_mouth_parts = ['Cute Bunny', 'Feasting Mosquito', 'Kawaii', 'Mosquito', 'Pincer', 'Square Teeth']
bird_mouth_parts = ['Doubletalk', 'Hungry Bird', 'Little Owl', 'Mr. Doubletalk', 'Peace Maker']
plant_mouth_parts = ['Herbivore', 'Humorless', 'Rudolph', 'Serious', 'Silence Whisper', 'Zigzag']
aquatic_mouth_parts = ['Catfish', 'Geisha', 'Lam', 'Lam Handsome', 'Piranha', 'Risky Fish']
reptile_mouth_parts = ['Dango', 'Kotaro', 'Razor Bite', 'Tiny Carrot', 'Tiny Turtle', 'Toothless Bite', 'Venom Bite']

beast_horn_parts = ['Arco', 'Dual Blade', 'Imp', 'Kendama', 'Little Branch', 'Merry', 'Pocky', 'Umaibo', 'Winter Branch']
bug_horn_parts = ['Antenna', 'Caterpillars', 'Lagging', 'Laggingggggg', 'Leaf Bug', 'P4R451T3', 'Parasite', 'Pliers']
bird_horn_parts = ['Cuckoo', 'Eggshell', 'Feather Spear', 'Golden Shell', 'Kestrel', 'Spruce Spear', 'Trump', 'Wing Horn']
plant_horn_parts = ['Bamboo Shoot', 'Breech', 'Cactus', 'Golden Bamboo Shoot', 'Rose Bud', "Santa's Gift", 'Strawberry Shortcake', 'Watermelon', 'Yorishiro']
aquatic_horn_parts = ['5H04L-5T4R', 'Anemone', 'Babylonia', 'Candy Babylonia', 'Clamshell', 'Oranda', 'Shoal Star', 'Teal Shell']
reptile_horn_parts = ['Bumpy', 'Cerastes', 'Incisor', 'Pinku Unko', 'Scaly Spear', 'Scaly Spoon', 'Unko']

beast_tail_parts = ['Cottontail', 'Gerbil', 'Hare', 'Nut Cracker', 'Rice', 'Sakura Cottontail', 'Shiba']
bug_tail_parts = ['Ant', 'Fire Ant', 'Fish Snack', 'Gravel Ant', 'Maki', 'Pupae', 'Thorny Caterpillar', 'Twin Tail']
bird_tail_parts = ['Cloud', 'Feather Fan', "Granma's Fan", 'Omatsuri', 'Post Fight', 'Snowy Swallow', 'Swallow', 'The Last One']
plant_tail_parts = ['Carrot', 'Cattail', 'Hatsune', 'Hot Butt', 'Namek Carrot', 'Potato Leaf', 'Yam']
aquatic_tail_parts = ['Koi', 'Koinobori', 'Kuro Koi', 'Navaga', 'Nimo', 'Ranchu', 'Shrimp', 'Tadpole']
reptile_tail_parts = ['December Surprise', 'Escaped Gecko', 'Fir Trunk', 'Gila', 'Grass Snake', 'Iguana', 'Snake Jar', 'Tiny Dino', 'Wall Gecko']

beast_parts = beast_eye_parts + beast_ear_parts + beast_back_parts + beast_mouth_parts + beast_horn_parts + beast_tail_parts
bug_parts = bug_eye_parts + bug_ear_parts + bug_back_parts + bug_mouth_parts + bug_horn_parts + bug_tail_parts
bird_parts = bird_eye_parts + bird_ear_parts + bird_back_parts + bird_mouth_parts + bird_horn_parts + bird_tail_parts
plant_parts = plant_eye_parts + plant_ear_parts + plant_back_parts + plant_mouth_parts + plant_horn_parts + plant_tail_parts
aquatic_parts = aquatic_eye_parts + aquatic_ear_parts + aquatic_back_parts + aquatic_mouth_parts + aquatic_horn_parts + aquatic_tail_parts
reptile_parts = reptile_eye_parts + reptile_ear_parts + reptile_back_parts + reptile_mouth_parts + reptile_horn_parts + reptile_tail_parts

all_class_types = ['Beast', 'Aquatic', 'Plant', 'Bird', 'Bug', 'Reptile', 'Mech', 'Dawn', 'Dusk']
all_eyes_parts = beast_eye_parts + bug_eye_parts + bird_eye_parts + plant_eye_parts + aquatic_eye_parts + reptile_eye_parts
all_ear_parts = beast_ear_parts + bug_ear_parts + bird_ear_parts + plant_ear_parts + aquatic_ear_parts + reptile_ear_parts
all_back_parts = beast_back_parts + bug_back_parts + bird_back_parts + plant_back_parts + aquatic_back_parts + reptile_back_parts
all_mouth_parts = beast_mouth_parts + bug_mouth_parts + bird_mouth_parts + plant_mouth_parts + aquatic_mouth_parts + reptile_mouth_parts
all_horn_parts = beast_horn_parts + bug_horn_parts + bird_horn_parts + plant_horn_parts + aquatic_horn_parts + reptile_horn_parts
all_tail_parts = beast_tail_parts + bug_tail_parts + bird_tail_parts + plant_tail_parts + aquatic_tail_parts + reptile_tail_parts

class Complex_Axie_Data:

    def __init__(self, class_type, purity, genes_dominant, genes_r1, genes_r2, value, id, breeds, date):
        self.genes_dominant = genes_dominant
        self.genes_r1 = genes_r1
        self.genes_r2 = genes_r2
        self.id = id
        self.purity = purity
        self.value = value
        self.breeds = breeds
        self.date = date
        self.objective_date = objective_date(self.date)
        self.class_type = class_type
        self.attributes = calc_attributes(self.genes_dominant, self.class_type)

    def __str__(self):
        #return str([self.class_type, self.purity, self.genes_dominant, self.genes_r1, self.genes_r2, self.attributes, self.value, self.breeds, self.id, self.date])
        return "Class Type: " + str(self.class_type) + " Id: " + str(self.id) + " Value: " + str(self.value) + " Date: " + str(self.objective_date) + '\n' + "D: " + str(self.genes_dominant) + '\n' + "R1:" + str(self.genes_r1) + '\n' + "R2:" + str(self.genes_r2) + '\n' + "Attributes: " + str(self.attributes) + " Breeds: " + str(self.breeds) + " Purity: " + str(self.purity) + '\n'

class Point_graph:
    def __init__(self, signature, x_axis_value, y_axis_value, amount):
        self.signature = signature
        self.x_axis_value = x_axis_value
        self.y_axis_value = y_axis_value
        self.amount = amount

    def __str__(self):
        #return self.signature + " " + str(self.x_axis_value) + " " + str(self.y_axis_value) + " " + str(self.amount)
        return self.signature + " " + str(self.amount)

def objective_date(element):
    #print(element)
    clean_element = element.replace('  ', ' ').split(' ')
    #print(clean_element)
    if int(clean_element[2]) >= 10:
        organized_element = clean_element[2]
    else:
        organized_element = '0' + clean_element[2]

    organized_element += " " + clean_element[1]
    organized_element += " " + clean_element[4]
    #print(organized_element)
    return organized_element


def calc_attributes(parts, type):
    if type == 'Aquatic':
        health = 39
        speed = 39
        skill = 35
        morale = 27

    elif type == 'Beast':
        health = 31
        speed = 35
        skill = 31
        morale = 43

    elif type == 'Bird':
        health = 27
        speed = 43
        skill = 35
        morale = 35

    elif type == 'Bug':
        health = 35
        speed = 31
        skill = 35
        morale = 39

    elif type == 'Plant':
        health = 43
        speed = 31
        skill = 31
        morale = 35

    elif type == 'Reptile':
        health = 39
        speed = 35
        skill = 31
        morale = 35

    elif type == 'Dawn':
        health = 35
        speed = 35
        skill = 39
        morale = 31

    elif type == 'Dusk':
        health = 43
        speed = 39
        skill = 27
        morale = 31

    elif type == 'Mech':
        health = 31
        speed = 39
        skill = 43
        morale = 27

    else:
        health = 0
        speed = 0
        skill = 0
        morale = 0

    for part in parts:
        if part in aquatic_parts:
            health += 1
            speed += 3
        if part in beast_parts:
            speed += 1
            morale += 3
        if part in bird_parts:
            speed += 3
            morale += 1
        if part in bug_parts:
            health += 1
            morale += 3
        if part in plant_parts:
            health += 3
            morale += 1
        if part in reptile_parts:
            health += 3
            speed += 1

    return [health, speed, skill, morale]

### Start-Up Database ###

def routine_pre_load(file_name):
    global raw_data
    #raw_data = read_data(file_name)
    raw_data = read_data(file_name)
    create_data()

def read_data(filename):
    file = codecs.open(filename, "r", "utf-8")
    line = file.read()
    #print(line)
    raw_data = line.replace('\r', '').split('\n')
    return raw_data

complex_axies = []
def create_data():
    #print(raw_data)
    #complex_axies = []
    line_count = 0
    for line in raw_data:
        try:
            line = line.split('-')
            if len(line) != 7:
                pass
            #print(line)
            ########################################################################################type
            class_type = line[0].replace('class_type: ', '').strip()
            purity = line[1].replace('purity: ', '').strip()
            ######################################################################################## genes
            genes_dominant = line[2].replace(" genes_dominant: [", '').replace("'", '').replace('] ', '').split(",")
            genes_dominant_clean_parts = []
            for part in genes_dominant:
                part_clean = part.strip()
                #print(part_clean)
                genes_dominant_clean_parts.append(part_clean)


            genes_r1 = line[3].replace(" genes_r1: [", '').replace("'", '').replace('] ', '').split(",")
            genes_r1_clean_parts = []
            for part in genes_r1:
                part_clean = part.strip()
                #print(part_clean)
                genes_r1_clean_parts.append(part_clean)

            genes_r2 = line[4].replace(" genes_r2: [", '').replace("'", '').replace('] ', '').split(",")
            genes_r2_clean_parts = []
            for part in genes_r2:
                part_clean = part.strip()
                #print(part_clean)
                genes_r2_clean_parts.append(part_clean)

            ##################################################################################### value
            value = float(line[5].replace(' value: ', '').replace(' ', '').replace(',', '.'))
            #print(value)
            ##################################################################################### id
            id = line[7].replace(' id: ', '').replace(' ', '')
            #print(id)
            ##################################################################################### breeds
            breeds = int(line[6].replace(' breeds: ', '').replace(' ', ''))
            #print(breeds)
            ##################################################################################### date
            date = line[8].replace('date: ', '').strip()
            #print(date)

            complex_axie = Complex_Axie_Data(class_type, purity, genes_dominant_clean_parts, genes_r1_clean_parts, genes_r2_clean_parts, value, id, breeds, date)
            #print(complex_axie)
            complex_axies.append(complex_axie)
            line_count += 1
        except:
            #print("error at line: " + str(line_count))
            pass

    print("total ok_axies: " + str(line_count))
    return complex_axies

### Search Engine ###

def custom_search(class_type, eyes, mouth, back, ears, horns, tail, breeds_min, breeds_max, min_value, max_value, min_health, min_speed, min_skill, min_morale, eye_gene, eye_gene_chance_min, ear_gene, ear_gene_chance_min, mouth_gene, mouth_gene_chance_min, horn_gene, horn_gene_chace_min, back_gene, back_gene_chance_min, tail_gene, tail_gene_chance_min, date_start, date_end):
    global custom_search_axies
    custom_search_axies = []

    if date_start == "None":
        date_found = True

    else:
        date_found = False

    for axie in complex_axies:
        #print(axie)

        eye_gene_chance = 0
        if eye_gene != 'None':

            if axie.genes_dominant[0] == eye_gene:
                eye_gene_chance += 37.5

            if axie.genes_r1[0] == eye_gene:
                eye_gene_chance += 9.375

            if axie.genes_r2[0] == eye_gene:
                eye_gene_chance += 3.125

        #######################################
        ear_gene_chance = 0
        if ear_gene != 'None':

            if axie.genes_dominant[1] == ear_gene:
                ear_gene_chance += 37.5

            if axie.genes_r1[1] == ear_gene:
                ear_gene_chance += 9.375

            if axie.genes_r2[1] == ear_gene:
                ear_gene_chance += 3.125

        #######################################
        mouth_gene_chance = 0
        if mouth_gene != 'None':

            if axie.genes_dominant[2] == mouth_gene:
                mouth_gene_chance += 37.5

            if axie.genes_r1[2] == mouth_gene:
                mouth_gene_chance += 9.375

            if axie.genes_r2[2] == mouth_gene:
                mouth_gene_chance += 3.125

        #######################################
        horn_gene_chance = 0
        if horn_gene != 'None':

            if axie.genes_dominant[3] == horn_gene:
                horn_gene_chance += 37.5

            if axie.genes_r1[3] == horn_gene:
                horn_gene_chance += 9.375

            if axie.genes_r2[3] == horn_gene:
                horn_gene_chance += 3.125

        #######################################
        back_gene_chance = 0
        if back_gene != 'None':

            if axie.genes_dominant[4] == back_gene:
                back_gene_chance += 37.5

            if axie.genes_r1[4] == back_gene:
                back_gene_chance += 9.375

            if axie.genes_r2[4] == back_gene:
                back_gene_chance += 3.125

        #######################################
        tail_gene_chance = 0
        if eye_gene != 'None':

            if axie.genes_dominant[5] == tail_gene:
                tail_gene_chance += 37.5

            if axie.genes_r1[5] == tail_gene:
                tail_gene_chance += 9.375

            if axie.genes_r2[5] == tail_gene:
                tail_gene_chance += 3.125

        #######################################

        if date_start != "None":
            if datetime.strptime(axie.objective_date, '%d %b %Y') >= datetime.strptime(date_start, '%d %b %Y') :
                date_found = True

        if date_end != "None":
            if datetime.strptime(axie.objective_date, '%d %b %Y') >= datetime.strptime(date_end, '%d %b %Y'):
                date_found = False

        #print(axie)
        if date_found:
            if eye_gene_chance >= eye_gene_chance_min and ear_gene_chance >= ear_gene_chance_min and mouth_gene_chance >= mouth_gene_chance_min and horn_gene_chance >= horn_gene_chace_min and back_gene_chance >= back_gene_chance_min and tail_gene_chance >= tail_gene_chance_min:
                if axie.attributes[0] >= min_health and axie.attributes[1] >= min_speed and axie.attributes[2] >= min_skill and axie.attributes[3] >= min_morale:
                    if (breeds_min <= axie.breeds <= breeds_max) and (axie.value <= max_value or max_value == 0) and (axie.value >= min_value or min_value == 0):
                        if (class_type == axie.class_type or class_type == 'None') and (eyes == axie.genes_dominant[0] or eyes == 'None') and (mouth == axie.genes_dominant[2] or mouth == 'None') and (back == axie.genes_dominant[4] or back == 'None') and (ears == axie.genes_dominant[1] or ears == 'None') and (horns == axie.genes_dominant[3] or horns == 'None') and (tail == axie.genes_dominant[5] or tail == 'None'):
                            custom_search_axies.append(axie)
                            #print(ear_gene_chance)
                            #print(axie.objective_date)
                            print(axie)

    global title_search
    title_search = "Class: " + str(class_type) + " Eyes: " + str(eyes) + " Mouth: " + str(mouth) + " Back: " + str(back) + " Ears: " + str(ears) + " Horns: " + str(horns) + " Tail: " + str(tail) + '\n' + " Breeds_min: " + str(breeds_min) + " Breeds_max: " + str(breeds_max) + " Max_value: " + str(max_value) + " Min_health: " + str(min_health) + " Min_speed: " + str(min_speed) + " Min_skill: " + str(min_skill) + " Min_morale: " + str(min_morale)

def create_axes():
    for axie in custom_search_axies:
        #print(axie)
        x.append(axie.objective_date)
        #x.append(axie.date)
        y.append(axie.value)

def create_point_heat():

    for pos in range(0, len(x)):
        signature = str(y[pos]) + " : " + x[pos]
        if signature not in known_signatures:
            point = Point_graph(signature, x[pos], y[pos], 1)
            known_signatures.append(signature)
            point_array.append(point)
        else:
            for point in point_array:
                if point.signature == signature:
                    point.amount += 1

    #sorting for most hot to overlap least hot
    point_array.sort(key=lambda object: object.amount)

def create_graph():
    dic = {}
    max_amount = point_array[-1].amount
    point_array.sort(key=lambda x: datetime.strptime(x.x_axis_value, '%d %b %Y'))

    for point in point_array:
        #print(point)
        if 0 < point.amount < max_amount * 0.70:
            plt.scatter(point.x_axis_value, point.y_axis_value, 200, color=matplotlib.colors.hsv_to_rgb([0.12, 1.0, (point.amount + (point.amount * 0.3)) / max_amount]), marker=".")
        else:
            plt.scatter(point.x_axis_value, point.y_axis_value, 200, color=(0.0, 0.0, 1.0), marker="X")
            plt.annotate("   " + str(point.y_axis_value), (point.x_axis_value, point.y_axis_value))


        if point.x_axis_value not in dic.keys():
            dic[point.x_axis_value] = {"value": 1}
        else:
            dic[point.x_axis_value]["value"] += 1

    values = []
    for key in dic.keys():
        label = key + '\n' +"results: " + str(dic[key]["value"])
        values.append(label)

    cmap = mpl.colors.ListedColormap(matplotlib.colors.hsv_to_rgb([[0.12, 1.0, 0.0], [0.12, 1.0, 0.1], [0.12, 1.0, 0.2], [0.12, 1.0, 0.3], [0.12, 1.0, 0.4], [0.12, 1.0, 0.5], [0.12, 1.0, 0.6], [0.12, 1.0, 0.7], [0.6, 1.00, 1.00], [0.6, 1.00, 1.00], [0.6, 1.00, 1.00]]))
    bounds = [0, max_amount * 0.10, max_amount * 0.20, max_amount * 0.30, max_amount * 0.40, max_amount * 0.50, max_amount * 0.60, max_amount * 0.70, max_amount * 0.80, max_amount * 0.90, max_amount * 1.0]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    clb = plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), location='left', pad=0.15)
    clb.set_label('Axies with same attributes and value' + '\n' + 'Heat Bar', rotation=90)

    locs, labels_text = plt.xticks()

    plt.xticks(ticks=locs, labels=values)
    #print(labels_text)
    plt.xticks(rotation=90)

    plt.title("DrWild Axie_Infinity_Market_Scout" + '\n' + "Results:" + str(len(custom_search_axies)) + '\n' + title_search)
    #plt.xlabel("Dates")
    plt.ylabel("Value")
    plt.box(True)

    #plt.tight_layout(True)
    #plt.figure(figsize=(8, 5))
    plt.savefig(fname='img.png')
    #plt.show()

    graph = get_graph()
    return graph

def routine_graph():
    global f, x, y, point_array, known_signatures
    f = plt.figure()
    f.set_figwidth(19)
    f.set_figheight(11)

    x = []
    y = []
    create_axes()

    #->point heat
    point_array = []
    known_signatures = []
    create_point_heat()
    return create_graph()

def search_helper_custom(class_type, eyes, mouth, back, ears, horns, tail, breeds_min, breeds_max, min_value, max_value, min_health, min_speed, min_skill, min_morale, eye_gene, eye_gene_chance_min, ear_gene, ear_gene_chance_min, mouth_gene, mouth_gene_chance_min, horn_gene, horn_gene_chace_min, back_gene, back_gene_chance_min, tail_gene, tail_gene_chance_min, date_start, date_end):
    search_helper_array = []
    if class_type not in all_class_types:
        print(str(class_type) + " isn't a known Class_Type")
        search_helper_array.append(str(class_type) + " isn't a known Class_Type")

    if eyes not in all_eyes_parts and eyes != 'None':
        print(str(eyes) + " isn't a known Eye")
        search_helper_array.append(str(eyes) + " isn't a known Eye")

    if mouth not in all_mouth_parts and mouth != 'None':
        print(str(mouth) + " isn't a known Mouth")
        search_helper_array.append(str(mouth) + " isn't a known Mouth")

    if back not in all_back_parts and back != 'None':
        print(str(back) + " isn't a known Back")
        search_helper_array.append(str(back) + " isn't a known Back")

    if ears not in all_ear_parts and ears != 'None':
        print(str(ears) + " isn't a known Ear")
        search_helper_array.append(str(ears) + " isn't a known Ear")

    if horns not in all_horn_parts and horns != 'None':
        print(str(horns) + " isn't a known Horn")
        search_helper_array.append(str(horns) + " isn't a known Horn")

    if tail not in all_tail_parts and tail != 'None':
        print(str(tail) + " isn't a known Tail")
        search_helper_array.append(str(tail) + " isn't a known Tail")

    try:
        if 0 > int(breeds_min) or int(breeds_min) > 7:
            print("Lowest Minimum Breeds is: 0 Highest Minimum Breeds is: 7 Current: " + str(breeds_min))
            search_helper_array.append("Lowest Minimum Breeds is: 0 Highest Minimum Breeds is: 7 Current: " + str(breeds_min))
    except:
        print("Minimum Breeds is not a number")
        search_helper_array.append("Minimum Breeds is not a number")

    try:
        if 0 > int(breeds_max) or int(breeds_max) > 7:
            print("Lowest Max Breeds is: 0 Highest Max Breeds is: 7 Current: " + str(breeds_max))
            search_helper_array.append("Lowest Max Breeds is: 0 Highest Max Breeds is: 7 Current: " + str(breeds_max))
    except :
        print("Max Breeds is not a number")
        search_helper_array.append("Max Breeds is not a number")

    try:
        if 0 > float(min_value):
            print("Min Value is bellow 0 Current: " + str(min_value))
            search_helper_array.append("Min Value is bellow 0 Current: " + str(min_value))
    except :
        print("Min Value is not a number")
        search_helper_array.append("Min Value is not a number")

    try:
        if 0 > float(max_value):
            print("Max Value is bellow 0 Current: " + str(max_value))
            search_helper_array.append("Max Value is bellow 0 Current: " + str(max_value))
    except :
        print("Max Value is not a number")
        search_helper_array.append("Max Value is not a number")


    try:
        if int(min_health) > 61:
            print("Max Health is: 61 Current: " + str(min_health))
            search_helper_array.append("Max Health is: 61 Current: " + str(min_health))
    except :
        print("Health is not a number")
        search_helper_array.append("Health is not a number")

    try:
        if int(min_speed) > 61:
            print("Max Speed is: 61 Current: " + str(min_speed))
            search_helper_array.append("Max Speed is: 61 Current: " + str(min_speed))
    except :
        print("Speed is not a number")
        search_helper_array.append("Speed is not a number")

    try:
        if int(min_skill) > 35:
            print("Max Skill is: 35 Current: " + str(min_skill))
            search_helper_array.append("Max Skill is: 35 Current: " + str(min_skill))
    except :
        print("Skill is not a number")
        search_helper_array.append("Skill is not a number")

    try:
        if int(min_morale) > 61:
            print("Max Morale is: 61 Current: " + str(min_morale))
            search_helper_array.append("Max Morale is: 61 Current: " + str(min_morale))
    except :
        print("Morale is not a number")
        search_helper_array.append("Morale is not a number")

    ##################################################################### genes

    if eye_gene not in all_eyes_parts and eye_gene != 'None':
        print(str(eye_gene) + " isn't a known Eye_gene")
        search_helper_array.append(str(eye_gene) + " isn't a known Eye_gene")

    try:
        if int(eye_gene_chance_min) > 50:
            print("Max eye_gene_chance_min is: 50 Current: " + str(eye_gene_chance_min))
            search_helper_array.append("Max eye_gene_chance_min is: 50 Current: " + str(eye_gene_chance_min))
    except :
        print("eye_gene_chance_min is not a number")
        search_helper_array.append("eye_gene_chance_min is not a number")
    #####################################################################################

    if ear_gene not in all_ear_parts and ear_gene != 'None':
        print(str(ear_gene) + " isn't a known Ear_gene")
        search_helper_array.append(str(ear_gene) + " isn't a known Ear_gene")

    try:
        if int(ear_gene_chance_min) > 50:
            print("Max ear_gene_chance_min is: 50 Current: " + str(ear_gene_chance_min))
            search_helper_array.append("Max ear_gene_chance_min is: 50 Current: " + str(ear_gene_chance_min))
    except :
        print("ear_gene_chance_min is not a number")
        search_helper_array.append("ear_gene_chance_min is not a number")
    #####################################################################################

    if mouth_gene not in all_mouth_parts and mouth_gene != 'None':
        print(str(mouth_gene) + " isn't a known Mouth_gene")
        search_helper_array.append(str(mouth_gene) + " isn't a known Mouth_gene")

    try:
        if int(mouth_gene_chance_min) > 50:
            print("Max mouth_gene_chance_min is: 50 Current: " + str(mouth_gene_chance_min))
            search_helper_array.append("Max mouth_gene_chance_min is: 50 Current: " + str(mouth_gene_chance_min))
    except :
        print("mouth_gene_chance_min is not a number")
        search_helper_array.append("mouth_gene_chance_min is not a number")
    #####################################################################################

    if horn_gene not in all_horn_parts and horn_gene != 'None':
        print(str(horn_gene) + " isn't a known Horn_gene")
        search_helper_array.append(str(horn_gene) + " isn't a known Horn_gene")

    try:
        if int(horn_gene_chace_min) > 50:
            print("Max horn_gene_chance_min is: 50 Current: " + str(horn_gene_chace_min))
            search_helper_array.append("Max horn_gene_chance_min is: 50 Current: " + str(horn_gene_chace_min))
    except :
        print("horn_gene_chance_min is not a number")
        search_helper_array.append("horn_gene_chance_min is not a number")
    #####################################################################################

    if back_gene not in all_back_parts and back_gene != 'None':
        print(str(back_gene) + " isn't a known Back_gene")
        search_helper_array.append(str(back_gene) + " isn't a known Back_gene")

    try:
        if int(back_gene_chance_min) > 50:
            print("Max back_gene_chance_min is: 50 Current: " + str(back_gene_chance_min))
            search_helper_array.append("Max back_gene_chance_min is: 50 Current: " + str(back_gene_chance_min))
    except :
        print("back_gene_chance_min is not a number")
        search_helper_array.append("back_gene_chance_min is not a number")
    #####################################################################################

    if tail_gene not in all_tail_parts and tail_gene != 'None':
        print(str(tail_gene) + " isn't a known Tail_gene")
        search_helper_array.append(str(tail_gene) + " isn't a known Tail_gene")

    try:
        if int(tail_gene_chance_min) > 50:
            print("Max tail_gene_chance_min is: 50 Current: " + str(tail_gene_chance_min))
            search_helper_array.append("Max tail_gene_chance_min is: 50 Current: " + str(tail_gene_chance_min))
    except :
        print("tail_gene_chance_min is not a number")
        search_helper_array.append("tail_gene_chance_min is not a number")
    #####################################################################################

    if date_start != "None":
        try:
            datetime.strptime(date_start, '%d %b %Y')

        except:
            print("date_start not valid")
            search_helper_array.append("date_start not valid")

    if date_end != "None":
        try:
            datetime.strptime(date_end, '%d %b %Y')
        except:
            print("date_end not valid")
            search_helper_array.append("date_end not valid")

    #return search_helper_array

    error_msg = ""
    for error in search_helper_array:
        error_msg += str(error) + '\n'
    return error_msg.strip()

def create_receipt():
    custom_search_axies.sort(key=lambda x: x.value)
    custom_search_axies.sort(key=lambda x: datetime.strptime(x.objective_date, '%d %b %Y'), reverse=True)

    axies_in_graph = ""
    total_axies = 0
    total_value = 0
    for axie in custom_search_axies:
        axies_in_graph += str(axie) + '\n'
        total_axies += 1
        total_value += axie.value

    return [axies_in_graph.strip(), str(total_value/total_axies)[:4]]
    #return axies_in_graph.strip()


def routine_graph_scatter_heat_plot(class_type, eyes, mouth, back, ears, horns, tail, breeds_min, breeds_max, min_value, max_value, min_health, min_speed, min_skill, min_morale, eye_gene, eye_gene_chance_min, ear_gene, ear_gene_chance_min, mouth_gene, mouth_gene_chance_min, horn_gene, horn_gene_chace_min, back_gene, back_gene_chance_min, tail_gene, tail_gene_chance_min, date_start, date_end):
    custom_search(class_type, eyes, mouth, back, ears, horns, tail, breeds_min, breeds_max, min_value, max_value, min_health, min_speed, min_skill, min_morale, eye_gene, eye_gene_chance_min, ear_gene, ear_gene_chance_min, mouth_gene, mouth_gene_chance_min, horn_gene, horn_gene_chace_min, back_gene, back_gene_chance_min, tail_gene, tail_gene_chance_min, date_start, date_end)
    return routine_graph()


### Start-Up Database ###
print("Load Started")
routine_pre_load('axie_all_sales.txt')
print("Load completed")
### Start-Up Database ###