# InscriptionImportIntoEDMV1Request

Request for POST /1/report/accountspayable/accountspayable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_import_into_edmv1_request import InscriptionImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionImportIntoEDMV1Request from a JSON string
inscription_import_into_edmv1_request_instance = InscriptionImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptionImportIntoEDMV1Request.to_json())

# convert the object into a dict
inscription_import_into_edmv1_request_dict = inscription_import_into_edmv1_request_instance.to_dict()
# create an instance of InscriptionImportIntoEDMV1Request from a dict
inscription_import_into_edmv1_request_from_dict = InscriptionImportIntoEDMV1Request.from_dict(inscription_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


