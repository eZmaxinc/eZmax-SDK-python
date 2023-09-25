# ApikeyGetObjectV2ResponseMPayload

Payload for GET /2/object/apikey/{pkiApikeyID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_apikey** | [**ApikeyResponseCompound**](ApikeyResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_get_object_v2_response_m_payload import ApikeyGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGetObjectV2ResponseMPayload from a JSON string
apikey_get_object_v2_response_m_payload_instance = ApikeyGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print ApikeyGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
apikey_get_object_v2_response_m_payload_dict = apikey_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of ApikeyGetObjectV2ResponseMPayload from a dict
apikey_get_object_v2_response_m_payload_form_dict = apikey_get_object_v2_response_m_payload.from_dict(apikey_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


