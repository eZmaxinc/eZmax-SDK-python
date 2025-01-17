# ApikeyEditPermissionsV1Response

Response for PUT /1/object/apikey/{pkiApikeyID}/editPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ApikeyEditPermissionsV1ResponseMPayload**](ApikeyEditPermissionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_edit_permissions_v1_response import ApikeyEditPermissionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyEditPermissionsV1Response from a JSON string
apikey_edit_permissions_v1_response_instance = ApikeyEditPermissionsV1Response.from_json(json)
# print the JSON string representation of the object
print(ApikeyEditPermissionsV1Response.to_json())

# convert the object into a dict
apikey_edit_permissions_v1_response_dict = apikey_edit_permissions_v1_response_instance.to_dict()
# create an instance of ApikeyEditPermissionsV1Response from a dict
apikey_edit_permissions_v1_response_from_dict = ApikeyEditPermissionsV1Response.from_dict(apikey_edit_permissions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


