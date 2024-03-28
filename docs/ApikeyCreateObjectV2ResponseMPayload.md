# ApikeyCreateObjectV2ResponseMPayload

Payload for POST /2/object/apikey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_apikey** | [**List[ApikeyResponseCompound]**](ApikeyResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_create_object_v2_response_m_payload import ApikeyCreateObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyCreateObjectV2ResponseMPayload from a JSON string
apikey_create_object_v2_response_m_payload_instance = ApikeyCreateObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ApikeyCreateObjectV2ResponseMPayload.to_json())

# convert the object into a dict
apikey_create_object_v2_response_m_payload_dict = apikey_create_object_v2_response_m_payload_instance.to_dict()
# create an instance of ApikeyCreateObjectV2ResponseMPayload from a dict
apikey_create_object_v2_response_m_payload_form_dict = apikey_create_object_v2_response_m_payload.from_dict(apikey_create_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


