# ModulegroupGetAllV1ResponseMPayload

Response for GET /1/object/modulegroup/getAll

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_modulegroup** | [**List[ModulegroupResponseCompound]**](ModulegroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.modulegroup_get_all_v1_response_m_payload import ModulegroupGetAllV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ModulegroupGetAllV1ResponseMPayload from a JSON string
modulegroup_get_all_v1_response_m_payload_instance = ModulegroupGetAllV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print ModulegroupGetAllV1ResponseMPayload.to_json()

# convert the object into a dict
modulegroup_get_all_v1_response_m_payload_dict = modulegroup_get_all_v1_response_m_payload_instance.to_dict()
# create an instance of ModulegroupGetAllV1ResponseMPayload from a dict
modulegroup_get_all_v1_response_m_payload_form_dict = modulegroup_get_all_v1_response_m_payload.from_dict(modulegroup_get_all_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


