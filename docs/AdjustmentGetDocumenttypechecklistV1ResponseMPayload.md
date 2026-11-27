# AdjustmentGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/adjustment/{pkiAdjustmentID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_get_documenttypechecklist_v1_response_m_payload import AdjustmentGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentGetDocumenttypechecklistV1ResponseMPayload from a JSON string
adjustment_get_documenttypechecklist_v1_response_m_payload_instance = AdjustmentGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AdjustmentGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
adjustment_get_documenttypechecklist_v1_response_m_payload_dict = adjustment_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of AdjustmentGetDocumenttypechecklistV1ResponseMPayload from a dict
adjustment_get_documenttypechecklist_v1_response_m_payload_from_dict = AdjustmentGetDocumenttypechecklistV1ResponseMPayload.from_dict(adjustment_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


