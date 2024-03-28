# EzsignsignergroupCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsignsignergroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignsignergroup_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_create_object_v1_response_m_payload import EzsignsignergroupCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupCreateObjectV1ResponseMPayload from a JSON string
ezsignsignergroup_create_object_v1_response_m_payload_instance = EzsignsignergroupCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignsignergroup_create_object_v1_response_m_payload_dict = ezsignsignergroup_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignsignergroupCreateObjectV1ResponseMPayload from a dict
ezsignsignergroup_create_object_v1_response_m_payload_form_dict = ezsignsignergroup_create_object_v1_response_m_payload.from_dict(ezsignsignergroup_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


