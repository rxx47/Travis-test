import pytest

@pytest.mark.parametrize("a,b, expected",[
                            (2, 3, 5),
                            (3, 7, 10),
                            (-2, 5, 3),
                            (0.1,0.2,0.3)
                            ])
                            
def test_add(a, b, expected):
    from calculate import add
    result = add(2,3)
    expected = 5
    assert result == pytest.approx(expected)