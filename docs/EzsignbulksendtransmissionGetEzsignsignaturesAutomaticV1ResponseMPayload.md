# EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload

Payload for GET /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getEzsignsignaturesAutomatic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_e_ezsignsignature_type** | [**List[FieldEEzsignsignatureType]**](FieldEEzsignsignatureType.md) | All eEzsignsignatureType contained in the response | 
**a_obj_ezsignfolder** | [**List[CustomEzsignfolderEzsignsignaturesAutomaticResponse]**](CustomEzsignfolderEzsignsignaturesAutomaticResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload import EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload from a JSON string
ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload_instance = EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload_dict = ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload from a dict
ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload_form_dict = ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload.from_dict(ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


