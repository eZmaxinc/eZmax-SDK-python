# EzsigntemplatesignerCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplatesigner_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_create_object_v1_response_m_payload import EzsigntemplatesignerCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerCreateObjectV1ResponseMPayload from a JSON string
ezsigntemplatesigner_create_object_v1_response_m_payload_instance = EzsigntemplatesignerCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignerCreateObjectV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplatesigner_create_object_v1_response_m_payload_dict = ezsigntemplatesigner_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignerCreateObjectV1ResponseMPayload from a dict
ezsigntemplatesigner_create_object_v1_response_m_payload_form_dict = ezsigntemplatesigner_create_object_v1_response_m_payload.from_dict(ezsigntemplatesigner_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


