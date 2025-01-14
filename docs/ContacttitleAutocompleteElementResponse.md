# ContacttitleAutocompleteElementResponse

A Contacttitle AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_contacttitle_id** | **int** | The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)| | 
**s_contacttitle_name_x** | **str** | The name of the Contacttitle in the language of the requester | 

## Example

```python
from eZmaxApi.models.contacttitle_autocomplete_element_response import ContacttitleAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContacttitleAutocompleteElementResponse from a JSON string
contacttitle_autocomplete_element_response_instance = ContacttitleAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(ContacttitleAutocompleteElementResponse.to_json())

# convert the object into a dict
contacttitle_autocomplete_element_response_dict = contacttitle_autocomplete_element_response_instance.to_dict()
# create an instance of ContacttitleAutocompleteElementResponse from a dict
contacttitle_autocomplete_element_response_from_dict = ContacttitleAutocompleteElementResponse.from_dict(contacttitle_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


