# GlaccountcontainerAutocompleteElementResponse

A Glaccountcontainer AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_glaccountcontainer_id** | **int** | The unique ID of the Glaccountcontainer | 
**s_glaccountcontainer_longcode** | **str** | The Code for the Glaccountcontainer | 
**s_glaccountcontainer_longdescription_x** | **str** | The Description for the Glaccountcontainer in the language of the requester | 
**b_glaccountcontainer_isactive** | **bool** | Whether the glaccountcontainer is active or not | 

## Example

```python
from eZmaxApi.models.glaccountcontainer_autocomplete_element_response import GlaccountcontainerAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlaccountcontainerAutocompleteElementResponse from a JSON string
glaccountcontainer_autocomplete_element_response_instance = GlaccountcontainerAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(GlaccountcontainerAutocompleteElementResponse.to_json())

# convert the object into a dict
glaccountcontainer_autocomplete_element_response_dict = glaccountcontainer_autocomplete_element_response_instance.to_dict()
# create an instance of GlaccountcontainerAutocompleteElementResponse from a dict
glaccountcontainer_autocomplete_element_response_from_dict = GlaccountcontainerAutocompleteElementResponse.from_dict(glaccountcontainer_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


