# EzsignfolderReorderV1Request

Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/reorder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigndocument_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_reorder_v1_request import EzsignfolderReorderV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderReorderV1Request from a JSON string
ezsignfolder_reorder_v1_request_instance = EzsignfolderReorderV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderReorderV1Request.to_json())

# convert the object into a dict
ezsignfolder_reorder_v1_request_dict = ezsignfolder_reorder_v1_request_instance.to_dict()
# create an instance of EzsignfolderReorderV1Request from a dict
ezsignfolder_reorder_v1_request_from_dict = EzsignfolderReorderV1Request.from_dict(ezsignfolder_reorder_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


