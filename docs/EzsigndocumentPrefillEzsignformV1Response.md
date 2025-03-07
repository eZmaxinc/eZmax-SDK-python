# EzsigndocumentPrefillEzsignformV1Response

Response for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/prefillEzsignform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_prefill_ezsignform_v1_response import EzsigndocumentPrefillEzsignformV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentPrefillEzsignformV1Response from a JSON string
ezsigndocument_prefill_ezsignform_v1_response_instance = EzsigndocumentPrefillEzsignformV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentPrefillEzsignformV1Response.to_json())

# convert the object into a dict
ezsigndocument_prefill_ezsignform_v1_response_dict = ezsigndocument_prefill_ezsignform_v1_response_instance.to_dict()
# create an instance of EzsigndocumentPrefillEzsignformV1Response from a dict
ezsigndocument_prefill_ezsignform_v1_response_from_dict = EzsigndocumentPrefillEzsignformV1Response.from_dict(ezsigndocument_prefill_ezsignform_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


