# UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload

Response for GET /1/object/usergroupexternal/{pkiUsergroupexternalID}/getUsergroupexternalmemberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupexternalmembership** | [**List[UsergroupexternalmembershipResponseCompound]**](UsergroupexternalmembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload import UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload from a JSON string
usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload_instance = UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload.to_json())

# convert the object into a dict
usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload_dict = usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload from a dict
usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload_form_dict = usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload.from_dict(usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


