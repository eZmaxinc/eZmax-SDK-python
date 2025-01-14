# EzsignsignatureCreateObjectV2Request

Request for POST /2/object/ezsignsignature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureRequestCompound]**](EzsignsignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_create_object_v2_request import EzsignsignatureCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureCreateObjectV2Request from a JSON string
ezsignsignature_create_object_v2_request_instance = EzsignsignatureCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureCreateObjectV2Request.to_json())

# convert the object into a dict
ezsignsignature_create_object_v2_request_dict = ezsignsignature_create_object_v2_request_instance.to_dict()
# create an instance of EzsignsignatureCreateObjectV2Request from a dict
ezsignsignature_create_object_v2_request_from_dict = EzsignsignatureCreateObjectV2Request.from_dict(ezsignsignature_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


