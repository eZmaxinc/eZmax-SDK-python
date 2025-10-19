# EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response

Response for GET /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatesignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload**](EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response import EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response from a JSON string
ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_instance = EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_dict = ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response from a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_from_dict = EzsigntemplatedocumentGetEzsigntemplatesignaturesV2Response.from_dict(ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


