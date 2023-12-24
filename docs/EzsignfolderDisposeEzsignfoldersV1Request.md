# EzsignfolderDisposeEzsignfoldersV1Request

Request for POST /1/object/ezsignfolder/disposeEzsignfolders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignfolder_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_dispose_ezsignfolders_v1_request import EzsignfolderDisposeEzsignfoldersV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderDisposeEzsignfoldersV1Request from a JSON string
ezsignfolder_dispose_ezsignfolders_v1_request_instance = EzsignfolderDisposeEzsignfoldersV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderDisposeEzsignfoldersV1Request.to_json()

# convert the object into a dict
ezsignfolder_dispose_ezsignfolders_v1_request_dict = ezsignfolder_dispose_ezsignfolders_v1_request_instance.to_dict()
# create an instance of EzsignfolderDisposeEzsignfoldersV1Request from a dict
ezsignfolder_dispose_ezsignfolders_v1_request_form_dict = ezsignfolder_dispose_ezsignfolders_v1_request.from_dict(ezsignfolder_dispose_ezsignfolders_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


