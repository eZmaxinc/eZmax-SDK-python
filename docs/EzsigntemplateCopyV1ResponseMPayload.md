# EzsigntemplateCopyV1ResponseMPayload

Payload for POST /1/object/ezsigntemplate/{pkiEzsigntemplateID}/copy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplate_id** | **List[int]** | An array of unique IDs representing the object that were requested to be copied.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_copy_v1_response_m_payload import EzsigntemplateCopyV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCopyV1ResponseMPayload from a JSON string
ezsigntemplate_copy_v1_response_m_payload_instance = EzsigntemplateCopyV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateCopyV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplate_copy_v1_response_m_payload_dict = ezsigntemplate_copy_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateCopyV1ResponseMPayload from a dict
ezsigntemplate_copy_v1_response_m_payload_form_dict = ezsigntemplate_copy_v1_response_m_payload.from_dict(ezsigntemplate_copy_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


