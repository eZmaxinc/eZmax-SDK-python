# EzsignsigningreasonResponse

A Ezsignsigningreason Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsigningreason_id** | **int** | The unique ID of the Ezsignsigningreason | 
**obj_ezsignsigningreason_description** | [**MultilingualEzsignsigningreasonDescription**](MultilingualEzsignsigningreasonDescription.md) |  | 
**b_ezsignsigningreason_isactive** | **bool** | Whether the ezsignsigningreason is active or not | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_response import EzsignsigningreasonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonResponse from a JSON string
ezsignsigningreason_response_instance = EzsignsigningreasonResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonResponse.to_json())

# convert the object into a dict
ezsignsigningreason_response_dict = ezsignsigningreason_response_instance.to_dict()
# create an instance of EzsignsigningreasonResponse from a dict
ezsignsigningreason_response_form_dict = ezsignsigningreason_response.from_dict(ezsignsigningreason_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


