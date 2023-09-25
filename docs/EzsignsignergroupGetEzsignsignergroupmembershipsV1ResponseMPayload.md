# EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload

Response for GET /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/getEzsignsignergroupmemberships

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignergroupmembership** | [**List[EzsignsignergroupmembershipResponseCompound]**](EzsignsignergroupmembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload import EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload from a JSON string
ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload_instance = EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload_dict = ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload from a dict
ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload_form_dict = ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload.from_dict(ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


