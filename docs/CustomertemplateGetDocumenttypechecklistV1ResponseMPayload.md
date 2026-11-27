# CustomertemplateGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/customertemplate/{pkiCustomertemplateID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.customertemplate_get_documenttypechecklist_v1_response_m_payload import CustomertemplateGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomertemplateGetDocumenttypechecklistV1ResponseMPayload from a JSON string
customertemplate_get_documenttypechecklist_v1_response_m_payload_instance = CustomertemplateGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomertemplateGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
customertemplate_get_documenttypechecklist_v1_response_m_payload_dict = customertemplate_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of CustomertemplateGetDocumenttypechecklistV1ResponseMPayload from a dict
customertemplate_get_documenttypechecklist_v1_response_m_payload_from_dict = CustomertemplateGetDocumenttypechecklistV1ResponseMPayload.from_dict(customertemplate_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


