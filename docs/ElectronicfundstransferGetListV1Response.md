# ElectronicfundstransferGetListV1Response

Response for GET /1/object/electronicfundstransfer/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ElectronicfundstransferGetListV1ResponseMPayload**](ElectronicfundstransferGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_list_v1_response import ElectronicfundstransferGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetListV1Response from a JSON string
electronicfundstransfer_get_list_v1_response_instance = ElectronicfundstransferGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetListV1Response.to_json())

# convert the object into a dict
electronicfundstransfer_get_list_v1_response_dict = electronicfundstransfer_get_list_v1_response_instance.to_dict()
# create an instance of ElectronicfundstransferGetListV1Response from a dict
electronicfundstransfer_get_list_v1_response_from_dict = ElectronicfundstransferGetListV1Response.from_dict(electronicfundstransfer_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


