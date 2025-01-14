# EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload

Payload for GET /1/object/ezsignfoldersignerassociation/getInPersonLoginUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_login_url** | **str** | The Url to login to the signing application.    Url will expire after 30 minutes.   | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_get_in_person_login_url_v1_response_m_payload import EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload from a JSON string
ezsignfoldersignerassociation_get_in_person_login_url_v1_response_m_payload_instance = EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_get_in_person_login_url_v1_response_m_payload_dict = ezsignfoldersignerassociation_get_in_person_login_url_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload from a dict
ezsignfoldersignerassociation_get_in_person_login_url_v1_response_m_payload_from_dict = EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload.from_dict(ezsignfoldersignerassociation_get_in_person_login_url_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


