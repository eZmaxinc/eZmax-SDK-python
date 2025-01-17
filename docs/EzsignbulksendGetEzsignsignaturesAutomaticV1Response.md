# EzsignbulksendGetEzsignsignaturesAutomaticV1Response

Response for GET /1/object/ezsignbulksend/{pkiEzsignbulksendID}/getEzsignsignaturesAutomatic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendGetEzsignsignaturesAutomaticV1ResponseMPayload**](EzsignbulksendGetEzsignsignaturesAutomaticV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_ezsignsignatures_automatic_v1_response import EzsignbulksendGetEzsignsignaturesAutomaticV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetEzsignsignaturesAutomaticV1Response from a JSON string
ezsignbulksend_get_ezsignsignatures_automatic_v1_response_instance = EzsignbulksendGetEzsignsignaturesAutomaticV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetEzsignsignaturesAutomaticV1Response.to_json())

# convert the object into a dict
ezsignbulksend_get_ezsignsignatures_automatic_v1_response_dict = ezsignbulksend_get_ezsignsignatures_automatic_v1_response_instance.to_dict()
# create an instance of EzsignbulksendGetEzsignsignaturesAutomaticV1Response from a dict
ezsignbulksend_get_ezsignsignatures_automatic_v1_response_from_dict = EzsignbulksendGetEzsignsignaturesAutomaticV1Response.from_dict(ezsignbulksend_get_ezsignsignatures_automatic_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


