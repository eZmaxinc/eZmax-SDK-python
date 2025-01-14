# EzsignbulksendsignermappingCreateObjectV1Request

Request for POST /1/object/ezsignbulksendsignermapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksendsignermapping** | [**List[EzsignbulksendsignermappingRequestCompound]**](EzsignbulksendsignermappingRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_request import EzsignbulksendsignermappingCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingCreateObjectV1Request from a JSON string
ezsignbulksendsignermapping_create_object_v1_request_instance = EzsignbulksendsignermappingCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingCreateObjectV1Request.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_create_object_v1_request_dict = ezsignbulksendsignermapping_create_object_v1_request_instance.to_dict()
# create an instance of EzsignbulksendsignermappingCreateObjectV1Request from a dict
ezsignbulksendsignermapping_create_object_v1_request_from_dict = EzsignbulksendsignermappingCreateObjectV1Request.from_dict(ezsignbulksendsignermapping_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


