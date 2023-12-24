# VariableexpenseCreateObjectV1ResponseMPayload

Payload for POST /1/object/variableexpense

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_variableexpense_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.variableexpense_create_object_v1_response_m_payload import VariableexpenseCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseCreateObjectV1ResponseMPayload from a JSON string
variableexpense_create_object_v1_response_m_payload_instance = VariableexpenseCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print VariableexpenseCreateObjectV1ResponseMPayload.to_json()

# convert the object into a dict
variableexpense_create_object_v1_response_m_payload_dict = variableexpense_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of VariableexpenseCreateObjectV1ResponseMPayload from a dict
variableexpense_create_object_v1_response_m_payload_form_dict = variableexpense_create_object_v1_response_m_payload.from_dict(variableexpense_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


