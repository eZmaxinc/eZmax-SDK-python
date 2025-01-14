# EzsignannotationCreateObjectV1Request

Request for POST /1/object/ezsignannotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignannotation** | [**List[EzsignannotationRequestCompound]**](EzsignannotationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignannotation_create_object_v1_request import EzsignannotationCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationCreateObjectV1Request from a JSON string
ezsignannotation_create_object_v1_request_instance = EzsignannotationCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationCreateObjectV1Request.to_json())

# convert the object into a dict
ezsignannotation_create_object_v1_request_dict = ezsignannotation_create_object_v1_request_instance.to_dict()
# create an instance of EzsignannotationCreateObjectV1Request from a dict
ezsignannotation_create_object_v1_request_from_dict = EzsignannotationCreateObjectV1Request.from_dict(ezsignannotation_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


