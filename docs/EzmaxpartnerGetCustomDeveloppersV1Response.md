# EzmaxpartnerGetCustomDeveloppersV1Response

Response for GET /1/object/ezmaxpartner/getCustomDeveloppers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload**](EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartner_get_custom_developpers_v1_response import EzmaxpartnerGetCustomDeveloppersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerGetCustomDeveloppersV1Response from a JSON string
ezmaxpartner_get_custom_developpers_v1_response_instance = EzmaxpartnerGetCustomDeveloppersV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerGetCustomDeveloppersV1Response.to_json())

# convert the object into a dict
ezmaxpartner_get_custom_developpers_v1_response_dict = ezmaxpartner_get_custom_developpers_v1_response_instance.to_dict()
# create an instance of EzmaxpartnerGetCustomDeveloppersV1Response from a dict
ezmaxpartner_get_custom_developpers_v1_response_from_dict = EzmaxpartnerGetCustomDeveloppersV1Response.from_dict(ezmaxpartner_get_custom_developpers_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


