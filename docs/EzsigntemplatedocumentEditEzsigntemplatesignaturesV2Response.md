# EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response

Response for PUT /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatesignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentEditEzsigntemplatesignaturesV2ResponseMPayload**](EzsigntemplatedocumentEditEzsigntemplatesignaturesV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_response import EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response from a JSON string
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_response_instance = EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_response_dict = ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response from a dict
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_response_from_dict = EzsigntemplatedocumentEditEzsigntemplatesignaturesV2Response.from_dict(ezsigntemplatedocument_edit_ezsigntemplatesignatures_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


