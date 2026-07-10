# InscriptionGetObjectV2ResponseMPayload

Payload for GET /2/object/inscription/{pkiInscriptionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_inscription** | [**InscriptionResponseCompound**](InscriptionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_object_v2_response_m_payload import InscriptionGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetObjectV2ResponseMPayload from a JSON string
inscription_get_object_v2_response_m_payload_instance = InscriptionGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
inscription_get_object_v2_response_m_payload_dict = inscription_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of InscriptionGetObjectV2ResponseMPayload from a dict
inscription_get_object_v2_response_m_payload_from_dict = InscriptionGetObjectV2ResponseMPayload.from_dict(inscription_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


