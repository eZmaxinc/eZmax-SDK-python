# FranchisereferalincomeCreateObjectV2Response

Response for POST /2/object/franchisereferalincome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FranchisereferalincomeCreateObjectV2ResponseMPayload**](FranchisereferalincomeCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.franchisereferalincome_create_object_v2_response import FranchisereferalincomeCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisereferalincomeCreateObjectV2Response from a JSON string
franchisereferalincome_create_object_v2_response_instance = FranchisereferalincomeCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(FranchisereferalincomeCreateObjectV2Response.to_json())

# convert the object into a dict
franchisereferalincome_create_object_v2_response_dict = franchisereferalincome_create_object_v2_response_instance.to_dict()
# create an instance of FranchisereferalincomeCreateObjectV2Response from a dict
franchisereferalincome_create_object_v2_response_from_dict = FranchisereferalincomeCreateObjectV2Response.from_dict(franchisereferalincome_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


