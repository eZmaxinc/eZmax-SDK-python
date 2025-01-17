# EzsignsignergroupEditEzsignsignergroupmembershipsV1Response

Response for PUT /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/editEzsignsignergroupmemberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignsignergroupEditEzsignsignergroupmembershipsV1ResponseMPayload**](EzsignsignergroupEditEzsignsignergroupmembershipsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response import EzsignsignergroupEditEzsignsignergroupmembershipsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupEditEzsignsignergroupmembershipsV1Response from a JSON string
ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response_instance = EzsignsignergroupEditEzsignsignergroupmembershipsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupEditEzsignsignergroupmembershipsV1Response.to_json())

# convert the object into a dict
ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response_dict = ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response_instance.to_dict()
# create an instance of EzsignsignergroupEditEzsignsignergroupmembershipsV1Response from a dict
ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response_from_dict = EzsignsignergroupEditEzsignsignergroupmembershipsV1Response.from_dict(ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


