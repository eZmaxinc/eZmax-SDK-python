# EzsigntemplateCreateObjectV3ResponseMPayload

Payload for POST /3/object/ezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplate_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_create_object_v3_response_m_payload import EzsigntemplateCreateObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCreateObjectV3ResponseMPayload from a JSON string
ezsigntemplate_create_object_v3_response_m_payload_instance = EzsigntemplateCreateObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCreateObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplate_create_object_v3_response_m_payload_dict = ezsigntemplate_create_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateCreateObjectV3ResponseMPayload from a dict
ezsigntemplate_create_object_v3_response_m_payload_from_dict = EzsigntemplateCreateObjectV3ResponseMPayload.from_dict(ezsigntemplate_create_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


