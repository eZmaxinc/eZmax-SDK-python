# ApikeyCreateObjectV2Response

Response for POST /2/object/apikey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ApikeyCreateObjectV2ResponseMPayload**](ApikeyCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_create_object_v2_response import ApikeyCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyCreateObjectV2Response from a JSON string
apikey_create_object_v2_response_instance = ApikeyCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(ApikeyCreateObjectV2Response.to_json())

# convert the object into a dict
apikey_create_object_v2_response_dict = apikey_create_object_v2_response_instance.to_dict()
# create an instance of ApikeyCreateObjectV2Response from a dict
apikey_create_object_v2_response_form_dict = apikey_create_object_v2_response.from_dict(apikey_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


