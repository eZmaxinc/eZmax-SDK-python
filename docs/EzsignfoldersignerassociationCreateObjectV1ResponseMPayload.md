# EzsignfoldersignerassociationCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsignfoldersignerassociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignfoldersignerassociation_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v1_response_m_payload import EzsignfoldersignerassociationCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateObjectV1ResponseMPayload from a JSON string
ezsignfoldersignerassociation_create_object_v1_response_m_payload_instance = EzsignfoldersignerassociationCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_object_v1_response_m_payload_dict = ezsignfoldersignerassociation_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateObjectV1ResponseMPayload from a dict
ezsignfoldersignerassociation_create_object_v1_response_m_payload_from_dict = EzsignfoldersignerassociationCreateObjectV1ResponseMPayload.from_dict(ezsignfoldersignerassociation_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


