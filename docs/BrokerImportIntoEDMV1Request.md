# BrokerImportIntoEDMV1Request

Request for POST /1/object/broker/{pkiBrokerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.broker_import_into_edmv1_request import BrokerImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerImportIntoEDMV1Request from a JSON string
broker_import_into_edmv1_request_instance = BrokerImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(BrokerImportIntoEDMV1Request.to_json())

# convert the object into a dict
broker_import_into_edmv1_request_dict = broker_import_into_edmv1_request_instance.to_dict()
# create an instance of BrokerImportIntoEDMV1Request from a dict
broker_import_into_edmv1_request_from_dict = BrokerImportIntoEDMV1Request.from_dict(broker_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


