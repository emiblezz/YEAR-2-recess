# gravitational force
planets = ["moon", "earth", "sun", "jupiter", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
           "Neptune"]


def gravity(g: float, mm: float):
    G = g
    M = mm
    G = (6.67 * (10 ** (-11)))
    M = (6.0 * (10 ** 24))
    m = (7.34 * (10 ** 22))
    r = (3.84 * (10 ** 8))

    if planet1 and planet2 == "moon" or "earth":
        grav_force = ((G * M * m) / r ** 2)
        print(grav_force)
    else:
        G = (6.67 * (10 ** (-11)))
        mm = input("Enter the mass of first planet\n")
        m = input("Enter the mass of second planet\n")
        r = input("Enter the radius between two  planet\n")
        G = (6.67 * (10 ** (-11)))
        grav_force = ((G * M * m) / r ** 2)
        print(grav_force(g, mm))

print("hello there :), lets compute the gravitational force between two planets planet")
planet1 = input("enter name of first planet: \n")
planet2 = input("enter name of  second planet: \n")

Gravity = gravity()
print(Gravity)
