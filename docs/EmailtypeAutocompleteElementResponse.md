# EmailtypeAutocompleteElementResponse

A Emailtype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_emailtype_id** | **int** | The unique ID of the Emailtype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| | 
**s_emailtype_name_x** | **str** | The name of the Emailtype in the language of the requester | 
**b_emailtype_isactive** | **bool** | Whether the Emailtype is active or not | 

## Example

```python
from eZmaxApi.models.emailtype_autocomplete_element_response import EmailtypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailtypeAutocompleteElementResponse from a JSON string
emailtype_autocomplete_element_response_instance = EmailtypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EmailtypeAutocompleteElementResponse.to_json())

# convert the object into a dict
emailtype_autocomplete_element_response_dict = emailtype_autocomplete_element_response_instance.to_dict()
# create an instance of EmailtypeAutocompleteElementResponse from a dict
emailtype_autocomplete_element_response_form_dict = emailtype_autocomplete_element_response.from_dict(emailtype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


