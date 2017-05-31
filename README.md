# Fidelity: The Tigrinya orthography wizard

Fidelity converts between Tigrinya script (Fidel) and a machine-readable ASCII transcription, *Fidelascii*. Fidelascii is a convenient representation of Tigrinya for programs that parse Tigrinya. See below for details on how Fidelascii maps to Tigrinya Fidel.

## Requirements

* Python 2.7

## Usage

Package is [available on PyPI](https://pypi.python.org/pypi/fidelity/0.1) and can be installed with
~~~~
pip install fidelity
~~~~
or installed locally with
~~~~
pip install .
~~~~
Then this package may be used in a Python script as follows:
~~~~
import fidelity

print fidelity.fidel2ascii(u"ትምህርቲ ዘይብሉ ህዝቢ ጨው ዘይብሉ መግቢ")
print fidelity.ascii2fidel("kulu yIHalIfI fIQIri yIterIfI")
~~~~

This outputs:

~~~~
tImIhIrIti zeyIbIlu hIzIbi CewI zeyIbIlu megIbi
ኩሉ ይሓልፍ ፍቕሪ ይተርፍ
~~~~

## Fidelascii

*Fidelascii* is a Tigrinya transcription scheme based on the following principles:

* ASCII-based
* Every Fidel character maps to a unique Fidelascii code string, and Fidelascii strings are uniquely representable in Fidel
* Every consonant and vowel is represented with one character, with the exception of labialized consonants which are two characters long

### Vowels:
 * አ = 'e
 * ኡ = 'u
 * ኢ = 'i
 * ኣ = 'a
 * ኤ = 'E
 * እ = 'I
 * ኦ = 'o

 Note: the vowel in እ is always written even when it is normally elided in speech, e.g. ትግርኛ in Fidelascii is *tIgIrINa*.

 ### Consonants
* ሀ = he
* ለ = le
* ሐ = He
* መ = me
* ረ = re
* ሰ = se
* ሸ = Se
* ቀ = qe
* ቐ = Qe
* በ = be
* ቨ = ve
* ተ = te
* ቸ = ce
* ነ = ne
* ኘ = Ne
* አ = 'e
* ከ = ke
* ኸ = Ke
* ወ = we
* ዐ = "e
* ዘ = ze
* ዠ = Ze
* የ = ye
* ደ = de
* ጀ = je
* ገ = ge
* ጠ = Te
* ጨ = Ce
* ጰ = Pe
* ጸ = xe
* ፈ = fe
* ፐ = pe

Labialized consonants are indicated by *W* before the vowel, e.g. ጓ = *gWa*.

### Punctuation:
Right now only spaces are supported.
