# BrokerGetListV1Response

Response for GET /1/object/broker/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrokerGetListV1ResponseMPayload**](BrokerGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.broker_get_list_v1_response import BrokerGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerGetListV1Response from a JSON string
broker_get_list_v1_response_instance = BrokerGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(BrokerGetListV1Response.to_json())

# convert the object into a dict
broker_get_list_v1_response_dict = broker_get_list_v1_response_instance.to_dict()
# create an instance of BrokerGetListV1Response from a dict
broker_get_list_v1_response_from_dict = BrokerGetListV1Response.from_dict(broker_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


