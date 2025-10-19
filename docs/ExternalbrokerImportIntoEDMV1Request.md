# ExternalbrokerImportIntoEDMV1Request

Request for POST /1/object/externalbroker/{pkiExternalbrokerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_import_into_edmv1_request import ExternalbrokerImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerImportIntoEDMV1Request from a JSON string
externalbroker_import_into_edmv1_request_instance = ExternalbrokerImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerImportIntoEDMV1Request.to_json())

# convert the object into a dict
externalbroker_import_into_edmv1_request_dict = externalbroker_import_into_edmv1_request_instance.to_dict()
# create an instance of ExternalbrokerImportIntoEDMV1Request from a dict
externalbroker_import_into_edmv1_request_from_dict = ExternalbrokerImportIntoEDMV1Request.from_dict(externalbroker_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


