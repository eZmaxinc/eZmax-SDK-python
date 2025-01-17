# ApikeyGetObjectV2Response

Response for GET /2/object/apikey/{pkiApikeyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ApikeyGetObjectV2ResponseMPayload**](ApikeyGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_get_object_v2_response import ApikeyGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGetObjectV2Response from a JSON string
apikey_get_object_v2_response_instance = ApikeyGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(ApikeyGetObjectV2Response.to_json())

# convert the object into a dict
apikey_get_object_v2_response_dict = apikey_get_object_v2_response_instance.to_dict()
# create an instance of ApikeyGetObjectV2Response from a dict
apikey_get_object_v2_response_from_dict = ApikeyGetObjectV2Response.from_dict(apikey_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


