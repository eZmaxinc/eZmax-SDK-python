# ApikeyEditPermissionsV1ResponseMPayload

Payload for PUT /1/object/apikey/{pkiApikeyID}/editPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_permission_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.apikey_edit_permissions_v1_response_m_payload import ApikeyEditPermissionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyEditPermissionsV1ResponseMPayload from a JSON string
apikey_edit_permissions_v1_response_m_payload_instance = ApikeyEditPermissionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ApikeyEditPermissionsV1ResponseMPayload.to_json())

# convert the object into a dict
apikey_edit_permissions_v1_response_m_payload_dict = apikey_edit_permissions_v1_response_m_payload_instance.to_dict()
# create an instance of ApikeyEditPermissionsV1ResponseMPayload from a dict
apikey_edit_permissions_v1_response_m_payload_form_dict = apikey_edit_permissions_v1_response_m_payload.from_dict(apikey_edit_permissions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


