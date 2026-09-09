# CommissionadvanceImportIntoEDMV1Response

Response for POST /1/object/commissionadvance/{pkiCommissionadvanceID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommissionadvanceImportIntoEDMV1ResponseMPayload**](CommissionadvanceImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_import_into_edmv1_response import CommissionadvanceImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceImportIntoEDMV1Response from a JSON string
commissionadvance_import_into_edmv1_response_instance = CommissionadvanceImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceImportIntoEDMV1Response.to_json())

# convert the object into a dict
commissionadvance_import_into_edmv1_response_dict = commissionadvance_import_into_edmv1_response_instance.to_dict()
# create an instance of CommissionadvanceImportIntoEDMV1Response from a dict
commissionadvance_import_into_edmv1_response_from_dict = CommissionadvanceImportIntoEDMV1Response.from_dict(commissionadvance_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


