# EzsignfoldersignerassociationGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfoldersignerassociation** | [**EzsignfoldersignerassociationResponseCompoundV3**](EzsignfoldersignerassociationResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v3_response_m_payload import EzsignfoldersignerassociationGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationGetObjectV3ResponseMPayload from a JSON string
ezsignfoldersignerassociation_get_object_v3_response_m_payload_instance = EzsignfoldersignerassociationGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_get_object_v3_response_m_payload_dict = ezsignfoldersignerassociation_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsignfoldersignerassociationGetObjectV3ResponseMPayload from a dict
ezsignfoldersignerassociation_get_object_v3_response_m_payload_from_dict = EzsignfoldersignerassociationGetObjectV3ResponseMPayload.from_dict(ezsignfoldersignerassociation_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


