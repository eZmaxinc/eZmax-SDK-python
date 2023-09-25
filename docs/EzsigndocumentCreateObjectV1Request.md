# EzsigndocumentCreateObjectV1Request

Request for POST /1/object/ezsigndocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndocument** | [**EzsigndocumentRequest**](EzsigndocumentRequest.md) |  | [optional] 
**obj_ezsigndocument_compound** | [**EzsigndocumentRequestCompound**](EzsigndocumentRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v1_request import EzsigndocumentCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV1Request from a JSON string
ezsigndocument_create_object_v1_request_instance = EzsigndocumentCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentCreateObjectV1Request.to_json()

# convert the object into a dict
ezsigndocument_create_object_v1_request_dict = ezsigndocument_create_object_v1_request_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV1Request from a dict
ezsigndocument_create_object_v1_request_form_dict = ezsigndocument_create_object_v1_request.from_dict(ezsigndocument_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


