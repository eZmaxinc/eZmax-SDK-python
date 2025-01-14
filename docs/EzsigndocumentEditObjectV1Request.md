# EzsigndocumentEditObjectV1Request

Request for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndocument** | [**EzsigndocumentRequestCompound**](EzsigndocumentRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_object_v1_request import EzsigndocumentEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditObjectV1Request from a JSON string
ezsigndocument_edit_object_v1_request_instance = EzsigndocumentEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditObjectV1Request.to_json())

# convert the object into a dict
ezsigndocument_edit_object_v1_request_dict = ezsigndocument_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigndocumentEditObjectV1Request from a dict
ezsigndocument_edit_object_v1_request_from_dict = EzsigndocumentEditObjectV1Request.from_dict(ezsigndocument_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


