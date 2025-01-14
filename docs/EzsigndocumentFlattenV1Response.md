# EzsigndocumentFlattenV1Response

Response for POST /1/object/ezsigndocument/{pkiEzsigndocument}/flatten

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_flatten_v1_response import EzsigndocumentFlattenV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentFlattenV1Response from a JSON string
ezsigndocument_flatten_v1_response_instance = EzsigndocumentFlattenV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentFlattenV1Response.to_json())

# convert the object into a dict
ezsigndocument_flatten_v1_response_dict = ezsigndocument_flatten_v1_response_instance.to_dict()
# create an instance of EzsigndocumentFlattenV1Response from a dict
ezsigndocument_flatten_v1_response_from_dict = EzsigndocumentFlattenV1Response.from_dict(ezsigndocument_flatten_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


