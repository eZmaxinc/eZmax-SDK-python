# EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response

Response for GET /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocument}/getEzsigntemplatesignatures

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload**](EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response import EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response from a JSON string
ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_instance = EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response.to_json()

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_dict = ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response from a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_form_dict = ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response.from_dict(ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


