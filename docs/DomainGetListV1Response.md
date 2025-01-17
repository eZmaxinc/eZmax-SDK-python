# DomainGetListV1Response

Response for GET /1/object/domain/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DomainGetListV1ResponseMPayload**](DomainGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.domain_get_list_v1_response import DomainGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetListV1Response from a JSON string
domain_get_list_v1_response_instance = DomainGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(DomainGetListV1Response.to_json())

# convert the object into a dict
domain_get_list_v1_response_dict = domain_get_list_v1_response_instance.to_dict()
# create an instance of DomainGetListV1Response from a dict
domain_get_list_v1_response_from_dict = DomainGetListV1Response.from_dict(domain_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


