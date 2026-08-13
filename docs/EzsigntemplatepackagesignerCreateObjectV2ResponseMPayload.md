# EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload

Payload for POST /2/object/ezsigntemplatepackagesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplatepackagesigner_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v2_response_m_payload import EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload from a JSON string
ezsigntemplatepackagesigner_create_object_v2_response_m_payload_instance = EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_create_object_v2_response_m_payload_dict = ezsigntemplatepackagesigner_create_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload from a dict
ezsigntemplatepackagesigner_create_object_v2_response_m_payload_from_dict = EzsigntemplatepackagesignerCreateObjectV2ResponseMPayload.from_dict(ezsigntemplatepackagesigner_create_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


