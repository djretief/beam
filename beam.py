from typing import Any


class Material:
    name = ""
    ultimate_strength = 0.0  # MPa
    yield_strength = 0.0  # MPa
    modulus_of_elasticity = 0.0  # GPa

    def __init__(self, material_name, material_ultimate_strength, material_yield_strength, material_modulus):
        self.name = material_name
        self.ultimate_strength = material_ultimate_strength
        self.yield_strength = material_yield_strength
        self.modulus_of_elasticity = material_modulus


class Beam:
    """
    The Beam class is used to represent the beam itself.  It contains the properties of the beam and the functions that
    are used to calculate properties of the beam.
    """
    material = None
    listOfBeamElements: list[Any] = []

    def add_beam_cross_section_element(self, element_width, element_height, element_x_offset, element_y_offset):
        """
        Add an element to the beam cross-section definition for this beam.  See the class "Element" for an explanation
        of what an element is.
        :param element_width: Width of the rectangular cross-sectional element
        :param element_height: Length of the rectangular cross-sectional element
        :param element_x_offset: The offset of the left side of the element from the origin on the x-axis
        :param element_y_offset: The offset of the bottom of the element from the origin on the y-axis
        :return: nothing
        """
        beam_element = Element(element_height, element_width, element_x_offset, element_y_offset)
        self.listOfBeamElements.append(beam_element)


class Element:
    """
    The class Element represents a rectangular cross-sectional part of the beam.  A beam cross-section is built up of
    several different parts of these elements to make up the total cross-section.
    """

    def __init__(self, height, width, x_offset, y_offset):
        """

        :param height: Length of the rectangular cross-sectional element
        :param width: Width of the rectangular cross-sectional element
        :param x_offset: The offset of the left side of the element from the origin on the x-axis
        :param y_offset: The offset of the bottom of the element from the origin on the y-axis
        """
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset


"""
Main code starts here:
"""
beam = Beam()
menu = True


def print_menu():
    """
    Function which displays the main menu screen
    :return:
    """
    print("Beam Definition:")
    if beam.material is not None:
        print("Beam Material: " + beam.material.name)
    print("Beam Elements:")
    for element in beam.listOfBeamElements:
        print("Beam Element")
        print("Width: " + element.width +
              " Height: " + element.height +
              " x Offset: " + element.x_offset +
              " y Offset: " + element.y_offset)
    print("n - Define new beam.  Note only beam can be defined at a time.  "
          "Creating a new beam erases any existing beams.")
    print("e - Add element to the beam cross section")

    # Get user menu selection input from the console
    print("Input:")
    user_input = input()

    # Menu selection process
    match user_input:
        case "n":
            print("Material name: ")
            material_name = input()
            print("Material ultimate strength: ")
            material_ultimate_strength = input()
            print("Material yield strength: ")
            material_yield_strength = input()
            print("Material modulus of elasticity: ")
            material_modulus = input()
            beam.material = Material(material_name, material_ultimate_strength, material_yield_strength,
                                     material_modulus)
        case "e":
            print("Adding a beam element:")
        case _:
            print("Invalid selection.")


while menu:
    print_menu()
