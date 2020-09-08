# this file was programatically generated by scripts/generate-elements.py
# DO NOT EDIT MANUALLY
from atompack.util import AsDict


class Element(AsDict):
    """Container to store metadata about an element."""

    def __init__(self, name: str, symbol: str, number: int, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)
        self._name = name
        self._symbol = symbol
        self._number = number

    @property
    def name(self) -> str:
        """Name of the element."""
        return self._name

    @property
    def symbol(self) -> str:
        """IUPAC chemical symbol."""
        return self._symbol

    @property
    def number(self) -> int:
        """Atomic number."""
        return self._number


class H(Element):
    """Hydrogen."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Hydrogen', 'H', 1, **kwargs)


class He(Element):
    """Helium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Helium', 'He', 2, **kwargs)


class Li(Element):
    """Lithium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Lithium', 'Li', 3, **kwargs)


class Be(Element):
    """Beryllium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Beryllium', 'Be', 4, **kwargs)


class B(Element):
    """Boron."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Boron', 'B', 5, **kwargs)


class C(Element):
    """Carbon."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Carbon', 'C', 6, **kwargs)


class N(Element):
    """Nitrogen."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Nitrogen', 'N', 7, **kwargs)


class O(Element):
    """Oxygen."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Oxygen', 'O', 8, **kwargs)


class F(Element):
    """Fluorine."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Fluorine', 'F', 9, **kwargs)


class Ne(Element):
    """Neon."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Neon', 'Ne', 10, **kwargs)


class Na(Element):
    """Sodium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Sodium', 'Na', 11, **kwargs)


class Mg(Element):
    """Magnesium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Magnesium', 'Mg', 12, **kwargs)


class Al(Element):
    """Aluminum."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Aluminum', 'Al', 13, **kwargs)


class Si(Element):
    """Silicon."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Silicon', 'Si', 14, **kwargs)


class P(Element):
    """Phosphorus."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Phosphorus', 'P', 15, **kwargs)


class S(Element):
    """Sulfur."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Sulfur', 'S', 16, **kwargs)


class Cl(Element):
    """Chlorine."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Chlorine', 'Cl', 17, **kwargs)


class Ar(Element):
    """Argon."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Argon', 'Ar', 18, **kwargs)


class K(Element):
    """Potassium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Potassium', 'K', 19, **kwargs)


class Ca(Element):
    """Calcium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Calcium', 'Ca', 20, **kwargs)


class Sc(Element):
    """Scanadium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Scanadium', 'Sc', 21, **kwargs)


class Ti(Element):
    """Titanium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Titanium', 'Ti', 22, **kwargs)


class V(Element):
    """Vanadium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Vanadium', 'V', 23, **kwargs)


class Cr(Element):
    """Chromium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Chromium', 'Cr', 24, **kwargs)


class Mn(Element):
    """Manganese."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Manganese', 'Mn', 25, **kwargs)


class Fe(Element):
    """Iron."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Iron', 'Fe', 26, **kwargs)


class Co(Element):
    """Cobalt."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Cobalt', 'Co', 27, **kwargs)


class Ni(Element):
    """Nickel."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Nickel', 'Ni', 28, **kwargs)


class Cu(Element):
    """Copper."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Copper', 'Cu', 29, **kwargs)


class Zn(Element):
    """Zinc."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Zinc', 'Zn', 30, **kwargs)


class Ga(Element):
    """Gallium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Gallium', 'Ga', 31, **kwargs)


class Ge(Element):
    """Germanium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Germanium', 'Ge', 32, **kwargs)


class As(Element):
    """Arsenic."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Arsenic', 'As', 33, **kwargs)


class Se(Element):
    """Selenium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Selenium', 'Se', 34, **kwargs)


class Br(Element):
    """Bromine."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Bromine', 'Br', 35, **kwargs)


class Kr(Element):
    """Krypton."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Krypton', 'Kr', 36, **kwargs)


class Rb(Element):
    """Rubidium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Rubidium', 'Rb', 37, **kwargs)


class Sr(Element):
    """Strontium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Strontium', 'Sr', 38, **kwargs)


class Y(Element):
    """Yttrium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Yttrium', 'Y', 39, **kwargs)


class Zr(Element):
    """Zirconium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Zirconium', 'Zr', 40, **kwargs)


class Nb(Element):
    """Niobium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Niobium', 'Nb', 41, **kwargs)


class Mo(Element):
    """Molybdenum."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Molybdenum', 'Mo', 42, **kwargs)


class Tc(Element):
    """Technetium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Technetium', 'Tc', 43, **kwargs)


class Ru(Element):
    """Ruthenium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Ruthenium', 'Ru', 44, **kwargs)


class Rh(Element):
    """Rhodium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Rhodium', 'Rh', 45, **kwargs)


class Pd(Element):
    """Palladium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Palladium', 'Pd', 46, **kwargs)


class Ag(Element):
    """Silver."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Silver', 'Ag', 47, **kwargs)


class Cd(Element):
    """Cadmium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Cadmium', 'Cd', 48, **kwargs)


class In(Element):
    """Indium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Indium', 'In', 49, **kwargs)


class Sn(Element):
    """Tin."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Tin', 'Sn', 50, **kwargs)


class Sb(Element):
    """Antimony."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Antimony', 'Sb', 51, **kwargs)


class Te(Element):
    """Tellurium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Tellurium', 'Te', 52, **kwargs)


class I(Element):
    """Iodine."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Iodine', 'I', 53, **kwargs)


class Xe(Element):
    """Xenon."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Xenon', 'Xe', 54, **kwargs)


class Cs(Element):
    """Caesium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Caesium', 'Cs', 55, **kwargs)


class Ba(Element):
    """Barium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Barium', 'Ba', 56, **kwargs)


class La(Element):
    """Lanthanum."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Lanthanum', 'La', 57, **kwargs)


class Ce(Element):
    """Cerium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Cerium', 'Ce', 58, **kwargs)


class Pr(Element):
    """Praseodymium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Praseodymium', 'Pr', 59, **kwargs)


class Nd(Element):
    """Neodymium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Neodymium', 'Nd', 60, **kwargs)


class Pm(Element):
    """Promethium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Promethium', 'Pm', 61, **kwargs)


class Sm(Element):
    """Samarium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Samarium', 'Sm', 62, **kwargs)


class Eu(Element):
    """Europium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Europium', 'Eu', 63, **kwargs)


class Gd(Element):
    """Gadolinium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Gadolinium', 'Gd', 64, **kwargs)


class Tb(Element):
    """Terbium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Terbium', 'Tb', 65, **kwargs)


class Dy(Element):
    """Dysprosium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Dysprosium', 'Dy', 66, **kwargs)


class Ho(Element):
    """Holmium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Holmium', 'Ho', 67, **kwargs)


class Er(Element):
    """Erbium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Erbium', 'Er', 68, **kwargs)


class Tm(Element):
    """Thulium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Thulium', 'Tm', 69, **kwargs)


class Yb(Element):
    """Ytterbium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Ytterbium', 'Yb', 70, **kwargs)


class Lu(Element):
    """Lutetium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Lutetium', 'Lu', 71, **kwargs)


class Hf(Element):
    """Hafnium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Hafnium', 'Hf', 72, **kwargs)


class Ta(Element):
    """Tantalum."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Tantalum', 'Ta', 73, **kwargs)


class W(Element):
    """Tungsten."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Tungsten', 'W', 74, **kwargs)


class Re(Element):
    """Rhenium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Rhenium', 'Re', 75, **kwargs)


class Os(Element):
    """Osmium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Osmium', 'Os', 76, **kwargs)


class Ir(Element):
    """Iridium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Iridium', 'Ir', 77, **kwargs)


class Pt(Element):
    """Platinum."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Platinum', 'Pt', 78, **kwargs)


class Au(Element):
    """Gold."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Gold', 'Au', 79, **kwargs)


class Hg(Element):
    """Mercury."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Mercury', 'Hg', 80, **kwargs)


class Tl(Element):
    """Thallium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Thallium', 'Tl', 81, **kwargs)


class Pb(Element):
    """Lead."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Lead', 'Pb', 82, **kwargs)


class Bi(Element):
    """Bismuth."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Bismuth', 'Bi', 83, **kwargs)


class Po(Element):
    """Polonium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Polonium', 'Po', 84, **kwargs)


class At(Element):
    """Astatine."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Astatine', 'At', 85, **kwargs)


class Rn(Element):
    """Radon."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Radon', 'Rn', 86, **kwargs)


class Fr(Element):
    """Francium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Francium', 'Fr', 87, **kwargs)


class Ra(Element):
    """Radium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Radium', 'Ra', 88, **kwargs)


class Ac(Element):
    """Actinium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Actinium', 'Ac', 89, **kwargs)


class Th(Element):
    """Thorium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Thorium', 'Th', 90, **kwargs)


class Pa(Element):
    """Protactinium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Protactinium', 'Pa', 91, **kwargs)


class U(Element):
    """Uranium."""

    def __init__(self, **kwargs) -> None:
        super().__init__('Uranium', 'U', 92, **kwargs)
