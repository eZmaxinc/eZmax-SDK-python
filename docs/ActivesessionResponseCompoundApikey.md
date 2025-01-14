# ActivesessionResponseCompoundApikey

An Activesession->Apikey object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_apikey_id** | **int** | The unique ID of the Apikey | 
**s_apikey_description_x** | **str** | The description of the Apikey in the language of the requester | 

## Example

```python
from eZmaxApi.models.activesession_response_compound_apikey import ActivesessionResponseCompoundApikey

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionResponseCompoundApikey from a JSON string
activesession_response_compound_apikey_instance = ActivesessionResponseCompoundApikey.from_json(json)
# print the JSON string representation of the object
print(ActivesessionResponseCompoundApikey.to_json())

# convert the object into a dict
activesession_response_compound_apikey_dict = activesession_response_compound_apikey_instance.to_dict()
# create an instance of ActivesessionResponseCompoundApikey from a dict
activesession_response_compound_apikey_from_dict = ActivesessionResponseCompoundApikey.from_dict(activesession_response_compound_apikey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


