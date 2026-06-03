# EzsigndocumentApplyEzsigntemplateglobalV2Response

Response for POST /2/object/ezsigndocument/{pkiEzsigndocument}/applyEzsigntemplateglobal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**a_obj_warning** | [**List[CommonResponseWarning]**](CommonResponseWarning.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplateglobal_v2_response import EzsigndocumentApplyEzsigntemplateglobalV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateglobalV2Response from a JSON string
ezsigndocument_apply_ezsigntemplateglobal_v2_response_instance = EzsigndocumentApplyEzsigntemplateglobalV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentApplyEzsigntemplateglobalV2Response.to_json())

# convert the object into a dict
ezsigndocument_apply_ezsigntemplateglobal_v2_response_dict = ezsigndocument_apply_ezsigntemplateglobal_v2_response_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateglobalV2Response from a dict
ezsigndocument_apply_ezsigntemplateglobal_v2_response_from_dict = EzsigndocumentApplyEzsigntemplateglobalV2Response.from_dict(ezsigndocument_apply_ezsigntemplateglobal_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


