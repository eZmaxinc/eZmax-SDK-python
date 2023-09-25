# ApikeyGetCorsV1Response

Response for GET /1/object/apikey/{pkiApikeyID}/getCors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ApikeyGetCorsV1ResponseMPayload**](ApikeyGetCorsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_get_cors_v1_response import ApikeyGetCorsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGetCorsV1Response from a JSON string
apikey_get_cors_v1_response_instance = ApikeyGetCorsV1Response.from_json(json)
# print the JSON string representation of the object
print ApikeyGetCorsV1Response.to_json()

# convert the object into a dict
apikey_get_cors_v1_response_dict = apikey_get_cors_v1_response_instance.to_dict()
# create an instance of ApikeyGetCorsV1Response from a dict
apikey_get_cors_v1_response_form_dict = apikey_get_cors_v1_response.from_dict(apikey_get_cors_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


