# EzsignbulksendsignermappingRequestV2

A Ezsignbulksendsignermapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendsignermapping_id** | **int** | The unique ID of the Ezsignbulksendsignermapping | [optional] 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**e_ezsignbulksendsignermapping_role** | [**FieldEEzsignbulksendsignermappingRole**](FieldEEzsignbulksendsignermappingRole.md) |  | [optional] 
**s_ezsignbulksendsignermapping_description** | **str** | The description of the Ezsignbulksendsignermapping | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_request_v2 import EzsignbulksendsignermappingRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingRequestV2 from a JSON string
ezsignbulksendsignermapping_request_v2_instance = EzsignbulksendsignermappingRequestV2.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingRequestV2.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_request_v2_dict = ezsignbulksendsignermapping_request_v2_instance.to_dict()
# create an instance of EzsignbulksendsignermappingRequestV2 from a dict
ezsignbulksendsignermapping_request_v2_from_dict = EzsignbulksendsignermappingRequestV2.from_dict(ezsignbulksendsignermapping_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


