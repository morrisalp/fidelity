# -*- coding: utf-8 -*-

from unittest import TestCase

import fidelity

class TestF2A(TestCase):
    def test_is_string(self):
        self.assertTrue(type(fidelity.fidel2ascii(u"ትግርኛ")) is str)

    def test_single_words(self):
        self.assertTrue(fidelity.fidel2ascii(u"ትግርኛ") == "tIgIrINa")
    
    def test_spaces(self):
        self.assertTrue(fidelity.fidel2ascii(u"ትምህርቲ ዘይብሉ ህዝቢ ጨው ዘይብሉ መግቢ") \
            == "tImIhIrIti zeyIbIlu hIzIbi CewI zeyIbIlu megIbi")
        self.assertTrue(fidelity.fidel2ascii(u"ኩሉ ይሓልፍ ፍቕሪ ይተርፍ") \
            == "kulu yIHalIfI fIQIri yIterIfI")

    def test_labialized(self):
        self.assertTrue(fidelity.fidel2ascii(u"ጓል") == "gWalI")
        self.assertTrue(fidelity.fidel2ascii(u"ምዃን") == "mIKWanI")
        self.assertTrue(fidelity.fidel2ascii(u"ኣይኰነን") == "'ayIkWenenI")

class TestA2F(TestCase):
    def test_is_unicode(self):
        self.assertTrue(type(fidelity.ascii2fidel("tIgIrINa")) is unicode)

    def test_single_words(self):
        self.assertTrue(fidelity.ascii2fidel("tIgIrINa") == u"ትግርኛ")
    
    def test_spaces(self):
        self.assertTrue(
            fidelity.ascii2fidel("tImIhIrIti zeyIbIlu hIzIbi CewI zeyIbIlu megIbi") \
            == u"ትምህርቲ ዘይብሉ ህዝቢ ጨው ዘይብሉ መግቢ")
        self.assertTrue(fidelity.ascii2fidel("kulu yIHalIfI fIQIri yIterIfI") \
            == u"ኩሉ ይሓልፍ ፍቕሪ ይተርፍ")

    def test_labialized(self):
        self.assertTrue(fidelity.ascii2fidel("gWalI") == u"ጓል")
        self.assertTrue(fidelity.ascii2fidel("mIKWanI") == u"ምዃን")
        self.assertTrue(fidelity.ascii2fidel("'ayIkWenenI") == u"ኣይኰነን")