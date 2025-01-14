# EzsignfolderReorderV2Request

Request for POST /2/object/ezsignfolder/{pkiEzsignfolderID}/reorder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezsignfolder_documentdependency** | [**FieldEEzsignfolderDocumentdependency**](FieldEEzsignfolderDocumentdependency.md) |  | [optional] 
**a_obj_ezsigndocument** | [**List[CustomEzsigndocumentRequest]**](CustomEzsigndocumentRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_reorder_v2_request import EzsignfolderReorderV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderReorderV2Request from a JSON string
ezsignfolder_reorder_v2_request_instance = EzsignfolderReorderV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderReorderV2Request.to_json())

# convert the object into a dict
ezsignfolder_reorder_v2_request_dict = ezsignfolder_reorder_v2_request_instance.to_dict()
# create an instance of EzsignfolderReorderV2Request from a dict
ezsignfolder_reorder_v2_request_from_dict = EzsignfolderReorderV2Request.from_dict(ezsignfolder_reorder_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


