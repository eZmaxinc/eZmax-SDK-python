# AdjustmentImportIntoEDMV1Response

Response for POST /1/object/adjustment/{pkiAdjustmentID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AdjustmentImportIntoEDMV1ResponseMPayload**](AdjustmentImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_import_into_edmv1_response import AdjustmentImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentImportIntoEDMV1Response from a JSON string
adjustment_import_into_edmv1_response_instance = AdjustmentImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(AdjustmentImportIntoEDMV1Response.to_json())

# convert the object into a dict
adjustment_import_into_edmv1_response_dict = adjustment_import_into_edmv1_response_instance.to_dict()
# create an instance of AdjustmentImportIntoEDMV1Response from a dict
adjustment_import_into_edmv1_response_from_dict = AdjustmentImportIntoEDMV1Response.from_dict(adjustment_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


