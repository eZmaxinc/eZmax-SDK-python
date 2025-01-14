# EzsignsignergroupGetEzsignsignergroupmembershipsV1Response

Response for GET /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/getEzsignsignergroupmemberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload**](EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response import EzsignsignergroupGetEzsignsignergroupmembershipsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupGetEzsignsignergroupmembershipsV1Response from a JSON string
ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_instance = EzsignsignergroupGetEzsignsignergroupmembershipsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupGetEzsignsignergroupmembershipsV1Response.to_json())

# convert the object into a dict
ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_dict = ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_instance.to_dict()
# create an instance of EzsignsignergroupGetEzsignsignergroupmembershipsV1Response from a dict
ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_from_dict = EzsignsignergroupGetEzsignsignergroupmembershipsV1Response.from_dict(ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


