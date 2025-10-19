# InscriptiontempImportIntoEDMV1Request

Request for POST /1/object/inscriptiontemp/{pkiInscriptiontempID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_import_into_edmv1_request import InscriptiontempImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempImportIntoEDMV1Request from a JSON string
inscriptiontemp_import_into_edmv1_request_instance = InscriptiontempImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempImportIntoEDMV1Request.to_json())

# convert the object into a dict
inscriptiontemp_import_into_edmv1_request_dict = inscriptiontemp_import_into_edmv1_request_instance.to_dict()
# create an instance of InscriptiontempImportIntoEDMV1Request from a dict
inscriptiontemp_import_into_edmv1_request_from_dict = InscriptiontempImportIntoEDMV1Request.from_dict(inscriptiontemp_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


