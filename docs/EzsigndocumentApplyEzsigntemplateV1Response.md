# EzsigndocumentApplyEzsigntemplateV1Response

Response for POST /1/object/ezsigndocument/{pkiEzsigndocument}/applyEzsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v1_response import EzsigndocumentApplyEzsigntemplateV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateV1Response from a JSON string
ezsigndocument_apply_ezsigntemplate_v1_response_instance = EzsigndocumentApplyEzsigntemplateV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentApplyEzsigntemplateV1Response.to_json()

# convert the object into a dict
ezsigndocument_apply_ezsigntemplate_v1_response_dict = ezsigndocument_apply_ezsigntemplate_v1_response_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateV1Response from a dict
ezsigndocument_apply_ezsigntemplate_v1_response_form_dict = ezsigndocument_apply_ezsigntemplate_v1_response.from_dict(ezsigndocument_apply_ezsigntemplate_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


