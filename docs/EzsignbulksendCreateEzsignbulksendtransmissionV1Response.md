# EzsignbulksendCreateEzsignbulksendtransmissionV1Response

Response for POST /1/object/ezsignbulksend/{pkiEzsignbulksendID}/createEzsignbulksendtransmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload**](EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v1_response import EzsignbulksendCreateEzsignbulksendtransmissionV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV1Response from a JSON string
ezsignbulksend_create_ezsignbulksendtransmission_v1_response_instance = EzsignbulksendCreateEzsignbulksendtransmissionV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendCreateEzsignbulksendtransmissionV1Response.to_json()

# convert the object into a dict
ezsignbulksend_create_ezsignbulksendtransmission_v1_response_dict = ezsignbulksend_create_ezsignbulksendtransmission_v1_response_instance.to_dict()
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV1Response from a dict
ezsignbulksend_create_ezsignbulksendtransmission_v1_response_form_dict = ezsignbulksend_create_ezsignbulksendtransmission_v1_response.from_dict(ezsignbulksend_create_ezsignbulksendtransmission_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


