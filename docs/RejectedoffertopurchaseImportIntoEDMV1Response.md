# RejectedoffertopurchaseImportIntoEDMV1Response

Response for POST /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload**](RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_import_into_edmv1_response import RejectedoffertopurchaseImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseImportIntoEDMV1Response from a JSON string
rejectedoffertopurchase_import_into_edmv1_response_instance = RejectedoffertopurchaseImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseImportIntoEDMV1Response.to_json())

# convert the object into a dict
rejectedoffertopurchase_import_into_edmv1_response_dict = rejectedoffertopurchase_import_into_edmv1_response_instance.to_dict()
# create an instance of RejectedoffertopurchaseImportIntoEDMV1Response from a dict
rejectedoffertopurchase_import_into_edmv1_response_from_dict = RejectedoffertopurchaseImportIntoEDMV1Response.from_dict(rejectedoffertopurchase_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


