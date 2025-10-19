# BrokerImportIntoEDMV1Response

Response for POST /1/object/broker/{pkiBrokerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrokerImportIntoEDMV1ResponseMPayload**](BrokerImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.broker_import_into_edmv1_response import BrokerImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerImportIntoEDMV1Response from a JSON string
broker_import_into_edmv1_response_instance = BrokerImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(BrokerImportIntoEDMV1Response.to_json())

# convert the object into a dict
broker_import_into_edmv1_response_dict = broker_import_into_edmv1_response_instance.to_dict()
# create an instance of BrokerImportIntoEDMV1Response from a dict
broker_import_into_edmv1_response_from_dict = BrokerImportIntoEDMV1Response.from_dict(broker_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


