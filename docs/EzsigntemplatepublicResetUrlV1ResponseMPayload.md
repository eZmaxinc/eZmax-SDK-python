# EzsigntemplatepublicResetUrlV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}/resetUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsigntemplatepublic_url** | **str** | The url of the Ezsigntemplatepublic  You can add these value as query parameters to prefill the corresponding role  |Parameter|Description| |-|-| |sEzsigntemplatesignerDescription|The role to fill| |sContactFirstname|The contact firstname| |sContactLastname|The contact lastname| |sEmailAddress|The contact email| |sPhoneE164|The contact phone number| |sPhoneE164Cell|The contact cell phone number| | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_reset_url_v1_response_m_payload import EzsigntemplatepublicResetUrlV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicResetUrlV1ResponseMPayload from a JSON string
ezsigntemplatepublic_reset_url_v1_response_m_payload_instance = EzsigntemplatepublicResetUrlV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicResetUrlV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_reset_url_v1_response_m_payload_dict = ezsigntemplatepublic_reset_url_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicResetUrlV1ResponseMPayload from a dict
ezsigntemplatepublic_reset_url_v1_response_m_payload_from_dict = EzsigntemplatepublicResetUrlV1ResponseMPayload.from_dict(ezsigntemplatepublic_reset_url_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


