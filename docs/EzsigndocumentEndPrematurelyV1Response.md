# EzsigndocumentEndPrematurelyV1Response

Response for POST /1/object/ezsigndocument/{pkiEzsigndocument}/endPrematurely

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_end_prematurely_v1_response import EzsigndocumentEndPrematurelyV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEndPrematurelyV1Response from a JSON string
ezsigndocument_end_prematurely_v1_response_instance = EzsigndocumentEndPrematurelyV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEndPrematurelyV1Response.to_json())

# convert the object into a dict
ezsigndocument_end_prematurely_v1_response_dict = ezsigndocument_end_prematurely_v1_response_instance.to_dict()
# create an instance of EzsigndocumentEndPrematurelyV1Response from a dict
ezsigndocument_end_prematurely_v1_response_form_dict = ezsigndocument_end_prematurely_v1_response.from_dict(ezsigndocument_end_prematurely_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


