# CommissionadvanceImportIntoEDMV1Request

Request for POST /1/object/commissionadvance/{pkiCommissionadvanceID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_import_into_edmv1_request import CommissionadvanceImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceImportIntoEDMV1Request from a JSON string
commissionadvance_import_into_edmv1_request_instance = CommissionadvanceImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceImportIntoEDMV1Request.to_json())

# convert the object into a dict
commissionadvance_import_into_edmv1_request_dict = commissionadvance_import_into_edmv1_request_instance.to_dict()
# create an instance of CommissionadvanceImportIntoEDMV1Request from a dict
commissionadvance_import_into_edmv1_request_from_dict = CommissionadvanceImportIntoEDMV1Request.from_dict(commissionadvance_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


