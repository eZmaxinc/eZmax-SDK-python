# EzsigndocumentGetEzsigndiscussionsV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocument}/getEzsigndiscussions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndiscussion** | [**List[EzsigndiscussionResponse]**](EzsigndiscussionResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_ezsigndiscussions_v1_response_m_payload import EzsigndocumentGetEzsigndiscussionsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetEzsigndiscussionsV1ResponseMPayload from a JSON string
ezsigndocument_get_ezsigndiscussions_v1_response_m_payload_instance = EzsigndocumentGetEzsigndiscussionsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetEzsigndiscussionsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_ezsigndiscussions_v1_response_m_payload_dict = ezsigndocument_get_ezsigndiscussions_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetEzsigndiscussionsV1ResponseMPayload from a dict
ezsigndocument_get_ezsigndiscussions_v1_response_m_payload_form_dict = ezsigndocument_get_ezsigndiscussions_v1_response_m_payload.from_dict(ezsigndocument_get_ezsigndiscussions_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


