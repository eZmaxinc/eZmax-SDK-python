# ElectronicfundstransfertransactionGetListV1Response

Response for GET /1/object/electronicfundstransfertransaction/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ElectronicfundstransfertransactionGetListV1ResponseMPayload**](ElectronicfundstransfertransactionGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfertransaction_get_list_v1_response import ElectronicfundstransfertransactionGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransfertransactionGetListV1Response from a JSON string
electronicfundstransfertransaction_get_list_v1_response_instance = ElectronicfundstransfertransactionGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransfertransactionGetListV1Response.to_json())

# convert the object into a dict
electronicfundstransfertransaction_get_list_v1_response_dict = electronicfundstransfertransaction_get_list_v1_response_instance.to_dict()
# create an instance of ElectronicfundstransfertransactionGetListV1Response from a dict
electronicfundstransfertransaction_get_list_v1_response_from_dict = ElectronicfundstransfertransactionGetListV1Response.from_dict(electronicfundstransfertransaction_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


