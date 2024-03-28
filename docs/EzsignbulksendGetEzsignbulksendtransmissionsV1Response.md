# EzsignbulksendGetEzsignbulksendtransmissionsV1Response

Response for GET /1/object/ezsignbulksend/{pkiEzsignbulksend}/getEzsignbulksendtransmissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload**](EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_ezsignbulksendtransmissions_v1_response import EzsignbulksendGetEzsignbulksendtransmissionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetEzsignbulksendtransmissionsV1Response from a JSON string
ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_instance = EzsignbulksendGetEzsignbulksendtransmissionsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetEzsignbulksendtransmissionsV1Response.to_json())

# convert the object into a dict
ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_dict = ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_instance.to_dict()
# create an instance of EzsignbulksendGetEzsignbulksendtransmissionsV1Response from a dict
ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_form_dict = ezsignbulksend_get_ezsignbulksendtransmissions_v1_response.from_dict(ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


