# EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatepublic/createEzsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsigntemplatepublic_signingurl** | **str** | The url to sign the Ezsignfolder created by the Ezsigntemplatepublic. Only used when fkiUserLogintypeID is **No validation** or **Sms only** | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_create_ezsignfolder_v1_response_m_payload import EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload from a JSON string
ezsigntemplatepublic_create_ezsignfolder_v1_response_m_payload_instance = EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_create_ezsignfolder_v1_response_m_payload_dict = ezsigntemplatepublic_create_ezsignfolder_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload from a dict
ezsigntemplatepublic_create_ezsignfolder_v1_response_m_payload_from_dict = EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload.from_dict(ezsigntemplatepublic_create_ezsignfolder_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


