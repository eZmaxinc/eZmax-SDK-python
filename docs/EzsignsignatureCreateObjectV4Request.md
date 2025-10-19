# EzsignsignatureCreateObjectV4Request

Request for POST /4/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureRequestCompoundV2]**](EzsignsignatureRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v4_request import EzsignsignatureCreateObjectV4Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV4Request from a JSON string
ezsignsignature_create_object_v4_request_instance = EzsignsignatureCreateObjectV4Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV4Request.to_json())

# convert the object into a dict
ezsignsignature_create_object_v4_request_dict = ezsignsignature_create_object_v4_request_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV4Request from a dict
ezsignsignature_create_object_v4_request_from_dict = EzsignsignatureCreateObjectV4Request.from_dict(ezsignsignature_create_object_v4_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


