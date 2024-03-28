# EzsignbulksendsignermappingResponse

A Ezsignbulksendsignermapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendsignermapping_id** | **int** | The unique ID of the Ezsignbulksendsignermapping | 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**s_ezsignbulksendsignermapping_description** | **str** | The description of the Ezsignbulksendsignermapping | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_response import EzsignbulksendsignermappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingResponse from a JSON string
ezsignbulksendsignermapping_response_instance = EzsignbulksendsignermappingResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingResponse.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_response_dict = ezsignbulksendsignermapping_response_instance.to_dict()
# create an instance of EzsignbulksendsignermappingResponse from a dict
ezsignbulksendsignermapping_response_form_dict = ezsignbulksendsignermapping_response.from_dict(ezsignbulksendsignermapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


