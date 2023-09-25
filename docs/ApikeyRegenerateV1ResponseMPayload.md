# ApikeyRegenerateV1ResponseMPayload

Response for GET /1/object/apikey/{pkiApikeyID}/regenerate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_apikey** | [**ApikeyResponseCompound**](ApikeyResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_regenerate_v1_response_m_payload import ApikeyRegenerateV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyRegenerateV1ResponseMPayload from a JSON string
apikey_regenerate_v1_response_m_payload_instance = ApikeyRegenerateV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print ApikeyRegenerateV1ResponseMPayload.to_json()

# convert the object into a dict
apikey_regenerate_v1_response_m_payload_dict = apikey_regenerate_v1_response_m_payload_instance.to_dict()
# create an instance of ApikeyRegenerateV1ResponseMPayload from a dict
apikey_regenerate_v1_response_m_payload_form_dict = apikey_regenerate_v1_response_m_payload.from_dict(apikey_regenerate_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


