# FranchisereferalincomeCreateObjectV1Response

Response for POST /1/object/franchisereferalincome

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FranchisereferalincomeCreateObjectV1ResponseMPayload**](FranchisereferalincomeCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.franchisereferalincome_create_object_v1_response import FranchisereferalincomeCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisereferalincomeCreateObjectV1Response from a JSON string
franchisereferalincome_create_object_v1_response_instance = FranchisereferalincomeCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print FranchisereferalincomeCreateObjectV1Response.to_json()

# convert the object into a dict
franchisereferalincome_create_object_v1_response_dict = franchisereferalincome_create_object_v1_response_instance.to_dict()
# create an instance of FranchisereferalincomeCreateObjectV1Response from a dict
franchisereferalincome_create_object_v1_response_form_dict = franchisereferalincome_create_object_v1_response.from_dict(franchisereferalincome_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


