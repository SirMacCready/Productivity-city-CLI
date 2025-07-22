from village.village import Village

def display_village():
    my_village = Village()

    for name, props in my_village.infrastructures.items():
        print(f"{name}: {props["value"]}")
    print(my_village.citizens)
