# EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response

Response for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatesignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload**](EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response import EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response from a JSON string
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response_instance = EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response_dict = ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response from a dict
ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response_from_dict = EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response.from_dict(ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


