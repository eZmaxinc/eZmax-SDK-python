# EzsignfolderDuplicateV1ResponseMPayload

Payload for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/duplicate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 

## Example

```python
from eZmaxApi.models.ezsignfolder_duplicate_v1_response_m_payload import EzsignfolderDuplicateV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderDuplicateV1ResponseMPayload from a JSON string
ezsignfolder_duplicate_v1_response_m_payload_instance = EzsignfolderDuplicateV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderDuplicateV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_duplicate_v1_response_m_payload_dict = ezsignfolder_duplicate_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderDuplicateV1ResponseMPayload from a dict
ezsignfolder_duplicate_v1_response_m_payload_from_dict = EzsignfolderDuplicateV1ResponseMPayload.from_dict(ezsignfolder_duplicate_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


