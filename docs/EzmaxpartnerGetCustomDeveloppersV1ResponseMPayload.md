# EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload

Payload for GET /1/object/ezmaxpartner/getCustomDeveloppers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezmaxpartner** | [**List[CustomEzmaxpartnerListElement]**](CustomEzmaxpartnerListElement.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartner_get_custom_developpers_v1_response_m_payload import EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload from a JSON string
ezmaxpartner_get_custom_developpers_v1_response_m_payload_instance = EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload.to_json())

# convert the object into a dict
ezmaxpartner_get_custom_developpers_v1_response_m_payload_dict = ezmaxpartner_get_custom_developpers_v1_response_m_payload_instance.to_dict()
# create an instance of EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload from a dict
ezmaxpartner_get_custom_developpers_v1_response_m_payload_from_dict = EzmaxpartnerGetCustomDeveloppersV1ResponseMPayload.from_dict(ezmaxpartner_get_custom_developpers_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


