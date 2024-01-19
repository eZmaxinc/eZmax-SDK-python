# CustomCreateEzsignelementsPositionedByWordRequest

A CreateEzsignelementsPositionedByWord object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_createezsignelementspositionedbyword_pattern** | **str** | The word to search | 
**i_createezsignelementspositionedbyword_offsetx** | **int** | The X offset | 
**i_createezsignelementspositionedbyword_offsety** | **int** | The Y offset | 
**e_createezsignelementspositionedbyword_occurance** | **str** | The occurance in the search to add the ezsign element | 

## Example

```python
from eZmaxApi.models.custom_create_ezsignelements_positioned_by_word_request import CustomCreateEzsignelementsPositionedByWordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCreateEzsignelementsPositionedByWordRequest from a JSON string
custom_create_ezsignelements_positioned_by_word_request_instance = CustomCreateEzsignelementsPositionedByWordRequest.from_json(json)
# print the JSON string representation of the object
print CustomCreateEzsignelementsPositionedByWordRequest.to_json()

# convert the object into a dict
custom_create_ezsignelements_positioned_by_word_request_dict = custom_create_ezsignelements_positioned_by_word_request_instance.to_dict()
# create an instance of CustomCreateEzsignelementsPositionedByWordRequest from a dict
custom_create_ezsignelements_positioned_by_word_request_form_dict = custom_create_ezsignelements_positioned_by_word_request.from_dict(custom_create_ezsignelements_positioned_by_word_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


