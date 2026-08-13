# EzsignbulksendsignermappingCreateObjectV2Request

Request for POST /2/object/ezsignbulksendsignermapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksendsignermapping** | [**List[EzsignbulksendsignermappingRequestCompoundV2]**](EzsignbulksendsignermappingRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v2_request import EzsignbulksendsignermappingCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingCreateObjectV2Request from a JSON string
ezsignbulksendsignermapping_create_object_v2_request_instance = EzsignbulksendsignermappingCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingCreateObjectV2Request.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_create_object_v2_request_dict = ezsignbulksendsignermapping_create_object_v2_request_instance.to_dict()
# create an instance of EzsignbulksendsignermappingCreateObjectV2Request from a dict
ezsignbulksendsignermapping_create_object_v2_request_from_dict = EzsignbulksendsignermappingCreateObjectV2Request.from_dict(ezsignbulksendsignermapping_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


