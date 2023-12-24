# EzsignfolderCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignfolder_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v1_response_m_payload import EzsignfolderCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV1ResponseMPayload from a JSON string
ezsignfolder_create_object_v1_response_m_payload_instance = EzsignfolderCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignfolderCreateObjectV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignfolder_create_object_v1_response_m_payload_dict = ezsignfolder_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV1ResponseMPayload from a dict
ezsignfolder_create_object_v1_response_m_payload_form_dict = ezsignfolder_create_object_v1_response_m_payload.from_dict(ezsignfolder_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


