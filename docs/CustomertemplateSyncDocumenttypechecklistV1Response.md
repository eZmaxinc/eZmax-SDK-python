# CustomertemplateSyncDocumenttypechecklistV1Response

Response for POST /1/object/customertemplate/{pkiCustomertemplateID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CustomertemplateSyncDocumenttypechecklistV1ResponseMPayload**](CustomertemplateSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customertemplate_sync_documenttypechecklist_v1_response import CustomertemplateSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomertemplateSyncDocumenttypechecklistV1Response from a JSON string
customertemplate_sync_documenttypechecklist_v1_response_instance = CustomertemplateSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(CustomertemplateSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
customertemplate_sync_documenttypechecklist_v1_response_dict = customertemplate_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of CustomertemplateSyncDocumenttypechecklistV1Response from a dict
customertemplate_sync_documenttypechecklist_v1_response_from_dict = CustomertemplateSyncDocumenttypechecklistV1Response.from_dict(customertemplate_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


