# CustomerImportIntoEDMV1Request

Request for POST /1/object/customer/{pkiCustomerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.customer_import_into_edmv1_request import CustomerImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerImportIntoEDMV1Request from a JSON string
customer_import_into_edmv1_request_instance = CustomerImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(CustomerImportIntoEDMV1Request.to_json())

# convert the object into a dict
customer_import_into_edmv1_request_dict = customer_import_into_edmv1_request_instance.to_dict()
# create an instance of CustomerImportIntoEDMV1Request from a dict
customer_import_into_edmv1_request_from_dict = CustomerImportIntoEDMV1Request.from_dict(customer_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


