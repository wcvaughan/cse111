from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name("Yamnianiamh", "Yisayiaweziya") == "Yisayiaweziya; Yamnianiamh"
    assert make_full_name("Ewan", "Rorkoh") == "Rorkoh; Ewan"
    assert make_full_name("Verkan", "Kieran-Bailey") == "Kieran-Bailey; Verkan"

def test_extract_family_name():

    assert extract_family_name("Kafardummur; Eduardagat") == "Kafardummur"
    assert extract_family_name("Zafo; yeva") == "Zafo"
    assert extract_family_name("Demmo-Pufa; Inessa") == "Demmo-Pufa"

def test_extract_given_name():

    assert extract_given_name("Polliwoglittletree; Rivercoppercups") == "Rivercoppercups"
    assert extract_given_name("Prott; Fern") == "Fern"
    assert extract_given_name("Iron-Wood; Rhine") == "Rhine"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])