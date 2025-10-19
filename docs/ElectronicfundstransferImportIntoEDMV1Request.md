# ElectronicfundstransferImportIntoEDMV1Request

Request for POST /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_import_into_edmv1_request import ElectronicfundstransferImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferImportIntoEDMV1Request from a JSON string
electronicfundstransfer_import_into_edmv1_request_instance = ElectronicfundstransferImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferImportIntoEDMV1Request.to_json())

# convert the object into a dict
electronicfundstransfer_import_into_edmv1_request_dict = electronicfundstransfer_import_into_edmv1_request_instance.to_dict()
# create an instance of ElectronicfundstransferImportIntoEDMV1Request from a dict
electronicfundstransfer_import_into_edmv1_request_from_dict = ElectronicfundstransferImportIntoEDMV1Request.from_dict(electronicfundstransfer_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


