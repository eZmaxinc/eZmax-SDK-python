# CustomEzsigndocumentRequest

Request for POST /2/object/ezsignfolder/{pkiEzsignfolderID}/reorder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**a_obj_ezsigndocumentdependency** | [**List[EzsigndocumentdependencyRequestCompound]**](EzsigndocumentdependencyRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezsigndocument_request import CustomEzsigndocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsigndocumentRequest from a JSON string
custom_ezsigndocument_request_instance = CustomEzsigndocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEzsigndocumentRequest.to_json())

# convert the object into a dict
custom_ezsigndocument_request_dict = custom_ezsigndocument_request_instance.to_dict()
# create an instance of CustomEzsigndocumentRequest from a dict
custom_ezsigndocument_request_from_dict = CustomEzsigndocumentRequest.from_dict(custom_ezsigndocument_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


