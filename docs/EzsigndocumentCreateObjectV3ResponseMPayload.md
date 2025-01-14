# EzsigndocumentCreateObjectV3ResponseMPayload

Payload for POST /3/object/ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[EzsigndocumentCreateElementV3Response]**](EzsigndocumentCreateElementV3Response.md) | An array of objets that contain unique IDs representing the object that were requested to be created and possibly matching template IDs.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_object_v3_response_m_payload import EzsigndocumentCreateObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateObjectV3ResponseMPayload from a JSON string
ezsigndocument_create_object_v3_response_m_payload_instance = EzsigndocumentCreateObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_create_object_v3_response_m_payload_dict = ezsigndocument_create_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentCreateObjectV3ResponseMPayload from a dict
ezsigndocument_create_object_v3_response_m_payload_from_dict = EzsigndocumentCreateObjectV3ResponseMPayload.from_dict(ezsigndocument_create_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


