# ApikeyGetPermissionsV1ResponseMPayload

Response for GET /1/object/apikey/{pkiApikeyID}/getPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_modulegroup** | [**List[ModulegroupResponseCompound]**](ModulegroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_get_permissions_v1_response_m_payload import ApikeyGetPermissionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGetPermissionsV1ResponseMPayload from a JSON string
apikey_get_permissions_v1_response_m_payload_instance = ApikeyGetPermissionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ApikeyGetPermissionsV1ResponseMPayload.to_json())

# convert the object into a dict
apikey_get_permissions_v1_response_m_payload_dict = apikey_get_permissions_v1_response_m_payload_instance.to_dict()
# create an instance of ApikeyGetPermissionsV1ResponseMPayload from a dict
apikey_get_permissions_v1_response_m_payload_from_dict = ApikeyGetPermissionsV1ResponseMPayload.from_dict(apikey_get_permissions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


