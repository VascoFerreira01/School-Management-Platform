import pytest

from src.school_management.models.assessment import Assessment

# test_assessment_is_created_successfully
def test_assessment_is_created_successfully():
    assessment = Assessment('Teste 1', 'oral', 35)

    assert assessment.name == 'Teste 1'
    assert assessment.assessment_type == 'oral'
    assert assessment.weight == 35

#test_assessment_cannot_have_empty_name
def test_assessment_cannot_have_empty_name():
    with pytest.raises(ValueError):
        Assessment('', 'oral', 35)


#test_assessment_cannot_have_empty_assessment_type
def test_assessment_cannot_have_empty_assessment_type():
    with pytest.raises(ValueError):
        Assessment('Teste 1', '', 35)

#test_assessment_weight_must_be_positive
def test_assessment_weight_must_be_positive():
    with pytest.raises(ValueError):
        Assessment('Teste 1', '', 0)

#test_assessment_weight_cannot_be_greater_than_100
def test_assessment_weight_cannot_be_greater_than_100():
    with pytest.raises(ValueError):
        Assessment('Teste 1', '', 120)