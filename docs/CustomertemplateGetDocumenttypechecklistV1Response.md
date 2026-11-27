# CustomertemplateGetDocumenttypechecklistV1Response

Response for GET /1/object/customertemplate/{pkiCustomertemplateID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CustomertemplateGetDocumenttypechecklistV1ResponseMPayload**](CustomertemplateGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customertemplate_get_documenttypechecklist_v1_response import CustomertemplateGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomertemplateGetDocumenttypechecklistV1Response from a JSON string
customertemplate_get_documenttypechecklist_v1_response_instance = CustomertemplateGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(CustomertemplateGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
customertemplate_get_documenttypechecklist_v1_response_dict = customertemplate_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of CustomertemplateGetDocumenttypechecklistV1Response from a dict
customertemplate_get_documenttypechecklist_v1_response_from_dict = CustomertemplateGetDocumenttypechecklistV1Response.from_dict(customertemplate_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


