# EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatepackagemembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplatepackagemembership_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_response_m_payload import EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload from a JSON string
ezsigntemplatepackagemembership_create_object_v1_response_m_payload_instance = EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_create_object_v1_response_m_payload_dict = ezsigntemplatepackagemembership_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload from a dict
ezsigntemplatepackagemembership_create_object_v1_response_m_payload_from_dict = EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload.from_dict(ezsigntemplatepackagemembership_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


