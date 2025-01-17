# EzsigntemplatepublicResetUrlV1Response

Response for POST /1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}/resetUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatepublicResetUrlV1ResponseMPayload**](EzsigntemplatepublicResetUrlV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_reset_url_v1_response import EzsigntemplatepublicResetUrlV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicResetUrlV1Response from a JSON string
ezsigntemplatepublic_reset_url_v1_response_instance = EzsigntemplatepublicResetUrlV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicResetUrlV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_reset_url_v1_response_dict = ezsigntemplatepublic_reset_url_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicResetUrlV1Response from a dict
ezsigntemplatepublic_reset_url_v1_response_from_dict = EzsigntemplatepublicResetUrlV1Response.from_dict(ezsigntemplatepublic_reset_url_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


