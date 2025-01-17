# EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response

Response for GET /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getEzsignsignaturesAutomatic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload**](EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response import EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response from a JSON string
ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_instance = EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response.to_json())

# convert the object into a dict
ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_dict = ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_instance.to_dict()
# create an instance of EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response from a dict
ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_from_dict = EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response.from_dict(ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


