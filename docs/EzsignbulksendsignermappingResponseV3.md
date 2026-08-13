# EzsignbulksendsignermappingResponseV3

A Ezsignbulksendsignermapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendsignermapping_id** | **int** | The unique ID of the Ezsignbulksendsignermapping | 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**e_ezsignbulksendsignermapping_role** | [**FieldEEzsignbulksendsignermappingRole**](FieldEEzsignbulksendsignermappingRole.md) |  | [optional] 
**s_ezsignbulksendsignermapping_description** | **str** | The description of the Ezsignbulksendsignermapping | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_response_v3 import EzsignbulksendsignermappingResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingResponseV3 from a JSON string
ezsignbulksendsignermapping_response_v3_instance = EzsignbulksendsignermappingResponseV3.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingResponseV3.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_response_v3_dict = ezsignbulksendsignermapping_response_v3_instance.to_dict()
# create an instance of EzsignbulksendsignermappingResponseV3 from a dict
ezsignbulksendsignermapping_response_v3_from_dict = EzsignbulksendsignermappingResponseV3.from_dict(ezsignbulksendsignermapping_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


