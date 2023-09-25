# EzsignbulksendsignermappingRequest

A Ezsignbulksendsignermapping Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendsignermapping_id** | **int** | The unique ID of the Ezsignbulksendsignermapping | [optional] 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**s_ezsignbulksendsignermapping_description** | **str** | The description of the Ezsignbulksendsignermapping | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_request import EzsignbulksendsignermappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingRequest from a JSON string
ezsignbulksendsignermapping_request_instance = EzsignbulksendsignermappingRequest.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendsignermappingRequest.to_json()

# convert the object into a dict
ezsignbulksendsignermapping_request_dict = ezsignbulksendsignermapping_request_instance.to_dict()
# create an instance of EzsignbulksendsignermappingRequest from a dict
ezsignbulksendsignermapping_request_form_dict = ezsignbulksendsignermapping_request.from_dict(ezsignbulksendsignermapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


