# OtherincometypeAutocompleteElementResponse

A Otherincometype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_otherincometype_id** | **int** | The unique ID of the Otherincometype | 
**s_otherincometype_description_x** | **str** | The description of the Otherincometype in the language of the requester | 
**b_otherincometype_isactive** | **bool** | Whether the Otherincometype is active or not | 

## Example

```python
from eZmaxApi.models.otherincometype_autocomplete_element_response import OtherincometypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincometypeAutocompleteElementResponse from a JSON string
otherincometype_autocomplete_element_response_instance = OtherincometypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(OtherincometypeAutocompleteElementResponse.to_json())

# convert the object into a dict
otherincometype_autocomplete_element_response_dict = otherincometype_autocomplete_element_response_instance.to_dict()
# create an instance of OtherincometypeAutocompleteElementResponse from a dict
otherincometype_autocomplete_element_response_from_dict = OtherincometypeAutocompleteElementResponse.from_dict(otherincometype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


