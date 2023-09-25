# EzsignfolderGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getCommunicationCount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_communication_count_v1_response_m_payload import EzsignfolderGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetCommunicationCountV1ResponseMPayload from a JSON string
ezsignfolder_get_communication_count_v1_response_m_payload_instance = EzsignfolderGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignfolderGetCommunicationCountV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignfolder_get_communication_count_v1_response_m_payload_dict = ezsignfolder_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetCommunicationCountV1ResponseMPayload from a dict
ezsignfolder_get_communication_count_v1_response_m_payload_form_dict = ezsignfolder_get_communication_count_v1_response_m_payload.from_dict(ezsignfolder_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


