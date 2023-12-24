# EzsignsigningreasonCreateObjectV1Request

Request for POST /1/object/ezsignsigningreason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsigningreason** | [**List[EzsignsigningreasonRequestCompound]**](EzsignsigningreasonRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_create_object_v1_request import EzsignsigningreasonCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonCreateObjectV1Request from a JSON string
ezsignsigningreason_create_object_v1_request_instance = EzsignsigningreasonCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignsigningreasonCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignsigningreason_create_object_v1_request_dict = ezsignsigningreason_create_object_v1_request_instance.to_dict()
# create an instance of EzsignsigningreasonCreateObjectV1Request from a dict
ezsignsigningreason_create_object_v1_request_form_dict = ezsignsigningreason_create_object_v1_request.from_dict(ezsignsigningreason_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


