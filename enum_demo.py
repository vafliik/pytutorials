from enum import Enum

class MichalDropDown(Enum):
    BILY_VINO = 'bily vino'
    CERVENY_VINO = 'cerveny vino'
    VINO_S_COLOU = 'vino s colou'

class DropdownDemo():

    def testovaci_funkce(self, option):
        print(option.value)


DropdownDemo().testovaci_funkce(MichalDropDown.BILY_VINO)
