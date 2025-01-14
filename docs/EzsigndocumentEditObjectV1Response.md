# EzsigndocumentEditObjectV1Response

Response for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**a_obj_warning** | [**List[CommonResponseWarning]**](CommonResponseWarning.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_object_v1_response import EzsigndocumentEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditObjectV1Response from a JSON string
ezsigndocument_edit_object_v1_response_instance = EzsigndocumentEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditObjectV1Response.to_json())

# convert the object into a dict
ezsigndocument_edit_object_v1_response_dict = ezsigndocument_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigndocumentEditObjectV1Response from a dict
ezsigndocument_edit_object_v1_response_from_dict = EzsigndocumentEditObjectV1Response.from_dict(ezsigndocument_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


