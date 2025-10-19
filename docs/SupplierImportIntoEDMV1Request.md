# SupplierImportIntoEDMV1Request

Request for POST /1/object/supplier/{pkiSupplierID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_import_into_edmv1_request import SupplierImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierImportIntoEDMV1Request from a JSON string
supplier_import_into_edmv1_request_instance = SupplierImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(SupplierImportIntoEDMV1Request.to_json())

# convert the object into a dict
supplier_import_into_edmv1_request_dict = supplier_import_into_edmv1_request_instance.to_dict()
# create an instance of SupplierImportIntoEDMV1Request from a dict
supplier_import_into_edmv1_request_from_dict = SupplierImportIntoEDMV1Request.from_dict(supplier_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


