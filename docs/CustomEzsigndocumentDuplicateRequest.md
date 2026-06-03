# CustomEzsigndocumentDuplicateRequest

An Ezsigndocument Object in the context of a duplicate path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**e_ezsigndocument_version** | **str** | Which version of the Ezsigndocument you would like to copy | 

## Example

```python
from eZmaxApi.models.custom_ezsigndocument_duplicate_request import CustomEzsigndocumentDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsigndocumentDuplicateRequest from a JSON string
custom_ezsigndocument_duplicate_request_instance = CustomEzsigndocumentDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEzsigndocumentDuplicateRequest.to_json())

# convert the object into a dict
custom_ezsigndocument_duplicate_request_dict = custom_ezsigndocument_duplicate_request_instance.to_dict()
# create an instance of CustomEzsigndocumentDuplicateRequest from a dict
custom_ezsigndocument_duplicate_request_from_dict = CustomEzsigndocumentDuplicateRequest.from_dict(custom_ezsigndocument_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


