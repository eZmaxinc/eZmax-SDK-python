# EzsigndocumentCreateObjectV3Request

Request for POST /3/object/ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[EzsigndocumentRequestCompound]**](EzsigndocumentRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v3_request import EzsigndocumentCreateObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV3Request from a JSON string
ezsigndocument_create_object_v3_request_instance = EzsigndocumentCreateObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateObjectV3Request.to_json())

# convert the object into a dict
ezsigndocument_create_object_v3_request_dict = ezsigndocument_create_object_v3_request_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV3Request from a dict
ezsigndocument_create_object_v3_request_from_dict = EzsigndocumentCreateObjectV3Request.from_dict(ezsigndocument_create_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


