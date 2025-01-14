# EzsignsignatureGetEzsignsignaturesAutomaticV1Response

Response for GET /1/object/ezsignsignature/getEzsignsignaturesAutomatic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload**](EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_ezsignsignatures_automatic_v1_response import EzsignsignatureGetEzsignsignaturesAutomaticV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetEzsignsignaturesAutomaticV1Response from a JSON string
ezsignsignature_get_ezsignsignatures_automatic_v1_response_instance = EzsignsignatureGetEzsignsignaturesAutomaticV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureGetEzsignsignaturesAutomaticV1Response.to_json())

# convert the object into a dict
ezsignsignature_get_ezsignsignatures_automatic_v1_response_dict = ezsignsignature_get_ezsignsignatures_automatic_v1_response_instance.to_dict()
# create an instance of EzsignsignatureGetEzsignsignaturesAutomaticV1Response from a dict
ezsignsignature_get_ezsignsignatures_automatic_v1_response_from_dict = EzsignsignatureGetEzsignsignaturesAutomaticV1Response.from_dict(ezsignsignature_get_ezsignsignatures_automatic_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


