# EzsignsignatureCreateObjectV1Request

Request for POST /1/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignature** | [**EzsignsignatureRequest**](EzsignsignatureRequest.md) |  | [optional] 
**obj_ezsignsignature_compound** | [**EzsignsignatureRequestCompound**](EzsignsignatureRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v1_request import EzsignsignatureCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV1Request from a JSON string
ezsignsignature_create_object_v1_request_instance = EzsignsignatureCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV1Request.to_json())

# convert the object into a dict
ezsignsignature_create_object_v1_request_dict = ezsignsignature_create_object_v1_request_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV1Request from a dict
ezsignsignature_create_object_v1_request_form_dict = ezsignsignature_create_object_v1_request.from_dict(ezsignsignature_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


