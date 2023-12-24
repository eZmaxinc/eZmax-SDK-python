# EzsigndocumentCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigndocument_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v1_response_m_payload import EzsigndocumentCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV1ResponseMPayload from a JSON string
ezsigndocument_create_object_v1_response_m_payload_instance = EzsigndocumentCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentCreateObjectV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigndocument_create_object_v1_response_m_payload_dict = ezsigndocument_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV1ResponseMPayload from a dict
ezsigndocument_create_object_v1_response_m_payload_form_dict = ezsigndocument_create_object_v1_response_m_payload.from_dict(ezsigndocument_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


