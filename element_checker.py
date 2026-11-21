# Periodic Table Information Finder
from pyscript import document


def countries_capital(e):
    document.getElementById("output").innerHTML = " "
    user_input = document.getElementById("input1").value


    periodic_table = {
        "H": "Symbol: H<br>Name: Hydrogen<br>Atomic Number: 1<br>Atomic Mass: 1.008",
        "He": "Symbol: He<br>Name: Helium<br>Atomic Number: 2<br>Atomic Mass: 4.0026",
        "C": "Symbol: C<br>Name: Carbon<br>Atomic Number: 6<br>Atomic Mass: 12.011",
        "N": "Symbol: N<br>Name: Nitrogen<br>Atomic Number: 7<br>Atomic Mass: 14.007",
        "O": "Symbol: O<br>Name: Oxygen<br>Atomic Number: 8<br>Atomic Mass: 15.999",
        "F": "Symbol: F<br>Name: Fluorine<br>Atomic Number: 9<br>Atomic Mass: 18.998",
        "Ne": "Symbol: Ne<br>Name: Neon<br>Atomic Number: 10<br>Atomic Mass: 20.180",
        "P": "Symbol: P<br>Name: Phosphorus<br>Atomic Number: 15<br>Atomic Mass: 30.974",
        "S": "Symbol: S<br>Name: Sulfur<br>Atomic Number: 16<br>Atomic Mass: 32.06",
        "Cl": "Symbol: Cl<br>Name: Chlorine<br>Atomic Number: 17<br>Atomic Mass: 35.45",
        "Ar": "Symbol: Ar<br>Name: Argon<br>Atomic Number: 18<br>Atomic Mass: 39.948",
        "Se": "Symbol: Se<br>Name: Selenium<br>Atomic Number: 34<br>Atomic Mass: 78.971",
        "Br": "Symbol: Br<br>Name: Bromine<br>Atomic Number: 35<br>Atomic Mass: 79.904",
        "Kr": "Symbol: Kr<br>Name: Krypton<br>Atomic Number: 36<br>Atomic Mass: 83.798",
        "I": "Symbol: I<br>Name: Iodine<br>Atomic Number: 53<br>Atomic Mass: 126.90",
        "Xe": "Symbol: Xe<br>Name: Xenon<br>Atomic Number: 54<br>Atomic Mass: 131.29",
        "Rn": "Symbol: Rn<br>Name: Radon<br>Atomic Number: 86<br>Atomic Mass: 222",
    }

    periodic_checker = user_input in periodic_table

    display_message = (f"Sorry, {user_input} is not a classified non-metal YO!", periodic_table.get(user_input))
    
    document.getElementById("output").innerHTML = display_message[periodic_checker]