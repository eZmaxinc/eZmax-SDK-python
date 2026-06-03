# EzsigndocumentApplyEzsigntemplateV3Response

Response for POST /3/object/ezsigndocument/{pkiEzsigndocument}/applyEzsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**a_obj_warning** | [**List[CommonResponseWarning]**](CommonResponseWarning.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v3_response import EzsigndocumentApplyEzsigntemplateV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateV3Response from a JSON string
ezsigndocument_apply_ezsigntemplate_v3_response_instance = EzsigndocumentApplyEzsigntemplateV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentApplyEzsigntemplateV3Response.to_json())

# convert the object into a dict
ezsigndocument_apply_ezsigntemplate_v3_response_dict = ezsigndocument_apply_ezsigntemplate_v3_response_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateV3Response from a dict
ezsigndocument_apply_ezsigntemplate_v3_response_from_dict = EzsigndocumentApplyEzsigntemplateV3Response.from_dict(ezsigndocument_apply_ezsigntemplate_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


