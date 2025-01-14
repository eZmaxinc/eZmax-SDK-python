# ApikeyGetCorsV1ResponseMPayload

Response for GET /1/object/apikey/{pkiApikeyID}/getCors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_cors** | [**List[CorsResponseCompound]**](CorsResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_get_cors_v1_response_m_payload import ApikeyGetCorsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGetCorsV1ResponseMPayload from a JSON string
apikey_get_cors_v1_response_m_payload_instance = ApikeyGetCorsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ApikeyGetCorsV1ResponseMPayload.to_json())

# convert the object into a dict
apikey_get_cors_v1_response_m_payload_dict = apikey_get_cors_v1_response_m_payload_instance.to_dict()
# create an instance of ApikeyGetCorsV1ResponseMPayload from a dict
apikey_get_cors_v1_response_m_payload_from_dict = ApikeyGetCorsV1ResponseMPayload.from_dict(apikey_get_cors_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


