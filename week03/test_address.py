from address import extract_city, \
    extract_state, extract_zipcode

import pytest

def test_extract_city():

    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("301 Railway Ave, Seward, AK 99664") == "Seward"

    return

def test_extract_state():

    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("301 Railway Ave, Seward, AK 99664") == "AK"

    return

def test_extract_zipcode():

    assert extract_zipcode("301 Railway Ave, Seward, AK 99664") == "99664"
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"

    return

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])