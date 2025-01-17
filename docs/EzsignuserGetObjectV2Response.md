# EzsignuserGetObjectV2Response

Response for GET /2/object/ezsignuser/{pkiEzsignuserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignuserGetObjectV2ResponseMPayload**](EzsignuserGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignuser_get_object_v2_response import EzsignuserGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserGetObjectV2Response from a JSON string
ezsignuser_get_object_v2_response_instance = EzsignuserGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignuserGetObjectV2Response.to_json())

# convert the object into a dict
ezsignuser_get_object_v2_response_dict = ezsignuser_get_object_v2_response_instance.to_dict()
# create an instance of EzsignuserGetObjectV2Response from a dict
ezsignuser_get_object_v2_response_from_dict = EzsignuserGetObjectV2Response.from_dict(ezsignuser_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


