# DomainGetObjectV2ResponseMPayload

Payload for GET /2/object/domain/{pkiDomainID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_domain** | [**DomainResponseCompound**](DomainResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.domain_get_object_v2_response_m_payload import DomainGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetObjectV2ResponseMPayload from a JSON string
domain_get_object_v2_response_m_payload_instance = DomainGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DomainGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
domain_get_object_v2_response_m_payload_dict = domain_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of DomainGetObjectV2ResponseMPayload from a dict
domain_get_object_v2_response_m_payload_from_dict = DomainGetObjectV2ResponseMPayload.from_dict(domain_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


