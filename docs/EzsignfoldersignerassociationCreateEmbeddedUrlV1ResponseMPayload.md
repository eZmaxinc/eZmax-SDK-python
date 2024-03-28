# EzsignfoldersignerassociationCreateEmbeddedUrlV1ResponseMPayload

Payload for POST /1/object/ezsignfoldersignerassociation/createEmbeddedUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_embedded_url** | **str** | The embedded Url to the signing application.    Url will expire after 5 minutes.   | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload import EzsignfoldersignerassociationCreateEmbeddedUrlV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateEmbeddedUrlV1ResponseMPayload from a JSON string
ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload_instance = EzsignfoldersignerassociationCreateEmbeddedUrlV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateEmbeddedUrlV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload_dict = ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateEmbeddedUrlV1ResponseMPayload from a dict
ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload_form_dict = ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload.from_dict(ezsignfoldersignerassociation_create_embedded_url_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


