# -*- coding: utf-8 -*-

vowels = "euiaEIo"
consonants = {
    "h": u"ሀሁሂሃሄህሆ",
    "l": u"ለሉሊላሌልሎ",
    "H": u"ሐሑሒሓሔሕሖ",
    "m": u"መሙሚማሜምሞ",
    "r": u"ረሩሪራሬርሮ",
    "s": u"ሰሱሲሳሴስሶ",
    "S": u"ሸሹሺሻሼሽሾ",
    "q": u"ቀቁቂቃቄቅቆ",
    "Q": u"ቐቑቒቓቔቕ",
    "b": u"በቡቢባቤብቦ",
    "v": u"ቨቩቪቫቬቭቮ",
    "t": u"ተቱቲታቴትቶ",
    "c": u"ቸቹቺቻቼችቾ",
    "n": u"ነኑኒናኔንኖ",
    "N": u"ኘኙኚኛኜኝኞ",
    "'": u"አኡኢኣኤእኦ",
    "k": u"ከኩኪካኬክኮ",
    "K": u"ኸኹኺኻኼኽኾ",
    "w": u"ወዉዊዋዌውዎ",
    "\"": u"ዐዑዒዓዔዕዖ",
    "z": u"ዘዙዚዛዜዝዞ",
    "Z": u"ዠዡዢዣዤዥዦ",
    "y": u"የዩዪያዬይዮ",
    "d": u"ደዱዲዳዴድዶ",
    "j": u"ጀጁጂጃጄጅጆ",
    "g": u"ገጉጊጋጌግጎ",
    "T": u"ጠጡጢጣጤጥጦ",
    "C": u"ጨጩጪጫጬጭጮ",
    "P": u"ጰጱጲጳጴጵጶ",
    "x": u"ጸጹጺጻጼጽጾ",
    "f": u"ፈፉፊፋፌፍፎ",
    "p": u"ፐፑፒፓፔፕፖ"
}
labialized_vowels = "eiaEI"
labialization_mark = "W"
labialized_consonants = {
    "q": u"ቈቊቋቌቍ",
    "Q": u"ቘቚቛቜቝ",
    "k": u"ኰኲኳኴኵ",
    "K": u"ዀዂዃዄዅ",
    "g": u"ጐጒጓጔጕ"
}
labialized_fidel = u"".join(labialized_consonants.values())

def fidelchar2ascii(fidel):
    assert type(fidel) is unicode
    if fidel == u" ":
        return " "
    if fidel in labialized_fidel:
        matching_consonant_codes = [
            code for code in labialized_consonants
            if fidel in labialized_consonants[code]
        ]
        assert len(matching_consonant_codes) == 1, "Unrecognized Fidel: %s" % fidel
        consonant_code = matching_consonant_codes[0]
        row = labialized_consonants[consonant_code]
        vowel_code = labialized_vowels[row.index(fidel)]
        return consonant_code + "W" + vowel_code
    else:
        matching_consonant_codes = [
            code for code in consonants
            if fidel in consonants[code]
        ]
        assert len(matching_consonant_codes) == 1, "Unrecognized Fidel: %s" % fidel
        consonant_code = matching_consonant_codes[0]
        row = consonants[consonant_code]
        vowel_code = vowels[row.index(fidel)]
        return consonant_code + vowel_code

def fidel2ascii(fidel_string):
    return "".join([
        fidelchar2ascii(fidel) for fidel in fidel_string
    ])

def ascii_unit2fidel(ascii_unit): # unit -- maps to one character
    if(ascii_unit == " "):
        return u" "
    if "W" in ascii_unit:
        # labialized three-character unit, e.g. gWa
        assert len(ascii_unit) == 3
        consonant_code = ascii_unit[0]
        vowel_code = ascii_unit[-1]
        return labialized_consonants[consonant_code][labialized_vowels.index(vowel_code)]
    else:
        assert len(ascii_unit) == 2
        consonant_code = ascii_unit[0]
        vowel_code = ascii_unit[1]
        assert consonant_code in consonants, "Unrecognized consonant code: %s" % consonant_code
        assert vowel_code in vowels, "Unrecognized vowel code: %s" % vowel_code
        return consonants[consonant_code][vowels.index(vowel_code)]

def ascii2units(ascii_string):
    if ascii_string == "":
        return []
    if ascii_string[0] == " ":
        return [" "] + ascii2units(ascii_string[1:])
    if ascii_string[1] == "W":
        # labialized, so unit is 3 characters long (e.g. gWa)
        assert len(ascii_string) >= 3
        return [ascii_string[0:3]] + ascii2units(ascii_string[3:])
    # normal two-character unit
    assert len(ascii_string) >= 2
    return [ascii_string[0:2]] + ascii2units(ascii_string[2:])

def ascii2fidel(ascii_string):
    return "".join([
        ascii_unit2fidel(ascii_unit)
        for ascii_unit in ascii2units(ascii_string)
    ])